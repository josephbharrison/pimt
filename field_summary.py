import pandas as pd
import yaml

def load_dictionary(dictionary_file):
    """
    Load the dictionary YAML file to get valid field names.
    
    :param dictionary_file: Path to the dictionary.yaml file.
    :return: List of valid field names.
    """
    try:
        with open(dictionary_file, "r") as file:
            schema = yaml.safe_load(file)
        return list(schema.keys())
    except Exception as e:
        print(f"An error occurred while loading the dictionary: {e}")
        return []

def list_unique_values(inventory_file, field_name):
    """
    List all unique values for a specified field in the inventory CSV.
    
    :param inventory_file: Path to the inventory.csv file.
    :param field_name: The field/column name to retrieve unique values for.
    :return: List of unique values for the specified field.
    """
    try:
        # Load the inventory CSV into a DataFrame
        inventory_df = pd.read_csv(inventory_file)
        
        # Check if the specified field exists
        if field_name not in inventory_df.columns:
            raise ValueError(f"Field '{field_name}' does not exist in the inventory.")
        
        # Get unique values and return as a sorted list
        unique_values = inventory_df[field_name].dropna().unique()
        return sorted(unique_values)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    """
    Main function for listing unique values in a specified field.
    """
    # File paths
    inventory_file = "inventory.csv"
    dictionary_file = "dictionary.yaml"
    
    # Load valid field names from the dictionary
    valid_fields = load_dictionary(dictionary_file)
    
    if not valid_fields:
        print("No valid field names could be loaded from the dictionary. Exiting.")
        return
    
    print("\nValid field names:")
    for field in valid_fields:
        print(f"- {field}")
    
    # Specify the field name to get unique values for
    field_name = input("\nEnter the field name to list unique values: ").strip()
    
    # Check if the field name is valid
    if field_name not in valid_fields:
        print(f"Invalid field name. Please choose a valid field from the list above.")
        return
    
    # Get unique values
    unique_values = list_unique_values(inventory_file, field_name)
    
    if unique_values:
        print(f"\nUnique values for field '{field_name}':")
        for value in unique_values:
            print(value)
    else:
        print(f"No unique values found for field '{field_name}' or an error occurred.")

if __name__ == "__main__":
    main()
