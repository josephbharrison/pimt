import csv
import json
import sys
from ast import literal_eval  # To safely evaluate string representations of Python literals


def parse_serialized_fields(row):
    """
    Parse specific fields in the row that are serialized as strings (e.g., lists or dictionaries).
    Converts them to actual JSON structures.

    :param row: A dictionary representing a single row of data.
    :return: A dictionary with parsed fields.
    """
    fields_to_parse = [
        "types",
        "subtypes",
        "abilities",
        "attacks",
        "weaknesses",
        "retreatCost",
        "resistances",
        "legalities",
        "nationalPokedexNumbers",
        "rules"
    ]

    for field in fields_to_parse:
        if field in row and row[field]:
            try:
                # Convert serialized field to Python literal (list, dict, etc.)
                row[field] = literal_eval(row[field])
            except (ValueError, SyntaxError):
                print(f"[WARNING] Failed to parse field '{field}' in row: {row['id']}")

    # Convert numeric fields to proper types where applicable
    for num_field in ["hp", "level", "convertedRetreatCost", "owned"]:
        if num_field in row and row[num_field]:
            try:
                row[num_field] = float(row[num_field]) if "." in row[num_field] else int(row[num_field])
            except ValueError:
                print(f"[WARNING] Failed to convert field '{num_field}' to number in row: {row['id']}")

    # Replace empty strings with None (null in JSON)
    row = {k: (v if v != "" else None) for k, v in row.items()}

    return row


def csv_to_json(csv_file, json_file):
    """
    Convert a CSV file to a JSON file with parsing of specific fields.

    :param csv_file: Path to the input CSV file.
    :param json_file: Path to the output JSON file.
    """
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvf:
            # Read the CSV file
            reader = csv.DictReader(csvf)
            rows = [parse_serialized_fields(row) for row in reader]

        # Write JSON file
        with open(json_file, 'w', encoding='utf-8') as jsonf:
            json.dump(rows, jsonf, indent=4, ensure_ascii=False)

        print(f"CSV successfully converted to JSON and saved to '{json_file}'")

    except FileNotFoundError:
        print(f"[ERROR] The file '{csv_file}' was not found.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


def main():
    """
    Main function to execute the CSV to JSON conversion.
    """
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]

    csv_to_json(csv_file, json_file)


if __name__ == "__main__":
    main()
