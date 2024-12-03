import yaml
import pandas as pd
import ast  # To safely evaluate strings into Python objects


def parse_dictionary(dictionary_file):
    """
    Parse the schema dictionary from a YAML file.
    :param dictionary_file: Path to the dictionary.yaml file.
    :return: Parsed schema as a dictionary.
    """
    with open(dictionary_file, "r") as file:
        schema = yaml.safe_load(file)
    return {field: details["type"] for field, details in schema.items()}


def process_inventory(inventory_file, schema):
    """
    Process the inventory CSV to align data with the schema.
    :param inventory_file: Path to the inventory.csv file.
    :param schema: Schema dictionary parsed from the dictionary.yaml file.
    :return: Processed pandas DataFrame.
    """
    df = pd.read_csv(inventory_file)
    for field, field_type in schema.items():
        if field in df.columns:
            if "stored as Python list" in field_type:
                df[field] = df[field].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
            elif "stored as Python dictionary" in field_type:
                df[field] = df[field].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
            elif "float64" in field_type:
                df[field] = pd.to_numeric(df[field], errors="coerce")
            elif "date" in field_type:
                df[field] = pd.to_datetime(df[field], errors="coerce")
    return df


def parse_rules_yaml(rules_file):
    """
    Parse and validate the rules.yaml file.
    :param rules_file: Path to the rules.yaml file.
    :return: List of ownership rules.
    """
    with open(rules_file, "r") as file:
        rules = yaml.safe_load(file)

    required_keys = {"name", "owned", "searchStrategy"}
    valid_strategies = {"first", "last", "all"}

    for rule in rules:
        if not required_keys.issubset(rule):
            raise ValueError(f"Missing required keys in rule: {rule}. Required keys: {required_keys}")
        if not isinstance(rule["owned"], int) or rule["owned"] < 0:
            raise ValueError(f"Invalid 'owned' value in rule: {rule}. Must be a non-negative integer.")
        if rule["searchStrategy"] not in valid_strategies:
            raise ValueError(f"Invalid 'searchStrategy' in rule: {rule}. Must be one of: {valid_strategies}")
        if "fields" in rule:
            if not isinstance(rule["fields"], dict):
                raise ValueError(f"Invalid 'fields' value in rule: {rule}. Must be a dictionary.")
    return rules


def apply_rules(inventory_df, rules):
    """
    Apply ownership rules to the inventory DataFrame.
    :param inventory_df: Pandas DataFrame of inventory.
    :param rules: List of ownership rules from rules.yaml.
    :return: Filtered DataFrame with `owned` field reflecting matches.
    """
    # Normalize inventory for case-insensitive matching
    inventory_df["name_normalized"] = inventory_df["name"].str.lower()

    filtered_rows = []  # Rows matching `rules.yaml` rules

    for rule in rules:
        # Extract basic rule details
        card_name = rule["name"].lower()
        qty_owned = rule["owned"]
        search_strategy = rule["searchStrategy"]
        fields = rule.get("fields", {})

        # Start filtering matches with card name
        matches = inventory_df[inventory_df["name_normalized"].str.contains(card_name, na=False)]

        # Apply additional field filters, if specified
        for field, value in fields.items():
            if field in matches.columns:
                if isinstance(value, str):
                    matches = matches[matches[field].str.lower().str.contains(value.lower(), na=False)]
                else:
                    matches = matches[matches[field] == value]

        # Apply search strategy to determine which matches to keep
        if not matches.empty:
            if search_strategy == "first":
                matches = matches.iloc[:1]
            elif search_strategy == "last":
                matches = matches.iloc[-1:]
            elif search_strategy == "all":
                matches = matches.copy()  # No slicing needed for "all"

            # Add the `owned` field to matched rows
            matches = matches.copy()
            matches["owned"] = qty_owned
            filtered_rows.append(matches)
        else:
            print(f"[WARNING] No matches found for rule: {rule}")

    # Concatenate matched rows to form the filtered DataFrame
    if filtered_rows:
        filtered_df = pd.concat(filtered_rows).drop_duplicates()
    else:
        filtered_df = pd.DataFrame(columns=inventory_df.columns)  # Empty DataFrame if no matches

    # Drop normalized columns
    filtered_df = filtered_df.drop(columns=["name_normalized"], errors="ignore")

    return filtered_df


def main():
    """
    Main function to process the dictionary, inventory, and rules files.
    """
    dictionary_file = "dictionary.yaml"
    inventory_file = "inventory.csv"
    rules_file = "rules.yaml"

    print("Parsing dictionary...")
    schema = parse_dictionary(dictionary_file)

    print("Parsing rules...")
    rules = parse_rules_yaml(rules_file)

    print("Processing inventory...")
    inventory_df = process_inventory(inventory_file, schema)

    print("Applying ownership rules...")
    updated_inventory_df = apply_rules(inventory_df, rules)

    processed_file = "filtered_inventory.csv"
    if not updated_inventory_df.empty:
        updated_inventory_df.to_csv(processed_file, index=False)
        print(f"Filtered inventory saved to {processed_file}")
    else:
        print("No filtered inventory to save.")


if __name__ == "__main__":
    main()
