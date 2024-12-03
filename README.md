# Pokémon Inventory Management Toolkit

A robust and extensible Python toolkit for managing inventory data through parsing, filtering, and conversion processes. This repository includes tools to:

1. Parse YAML-based schema and search rules.
2. Process and filter inventory based on user-defined rules.
3. Summarize unique values in inventory fields.
4. Convert CSV files into JSON with parsed fields for structured output.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Scripts Overview](#scripts-overview)
  - [Example Workflow](#example-workflow)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Schema-Driven Inventory Processing**: Parses `dictionary.yaml` to apply type conversions and validations to `inventory.csv`.
- **Ownership Rules Application**: Filters inventory based on rules defined in `rules.yaml`.
- **Field Summarization**: Retrieves unique values for specified fields in inventory.
- **CSV-to-JSON Conversion**: Converts inventory data from CSV to JSON with parsed and normalized fields.

---

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `pandas`
  - `PyYAML`

Install dependencies via pip:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Installation

Clone this repository:

```bash
git clone https://github.com/josephbharrison/inventory-management-toolkit.git
cd inventory-management-toolkit
```

---

## Usage

### Scripts Overview

1. **`search.py`**
   - Parses schema and ownership rules.
   - Processes inventory data and applies filtering rules.

2. **`field_summary.py`**
   - Lists unique values for specified fields in the inventory.

3. **`csv_to_json.py`**
   - Converts inventory CSV files to JSON format with normalized fields.

### Example Workflow

1. Prepare the following files:
   - **`dictionary.yaml`**: Defines schema for inventory fields.
   - **`inventory.csv`**: Raw inventory data.
   - **`rules.yaml`**: Ownership rules for filtering inventory.

2. Parse inventory and apply search rules:

```bash
python search.py
```

3. Summarize unique field values:

```bash
python field_summary.py
```

4. Convert inventory CSV to JSON:

```bash
python csv_to_json.py inventory.csv inventory.json
```

---

## File Descriptions

### `search.py`

The core script for inventory processing:
- Parses schema from `dictionary.yaml`.
- Applies search and ownership rules from `rules.yaml`.
- Outputs filtered inventory as `filtered_inventory.csv`.

### `field_summary.py`

A utility script to retrieve unique field values:
- Lists unique values for any valid field in `inventory.csv`.

### `csv_to_json.py`

A script to convert CSV files to JSON:
- Parses serialized fields (e.g., lists or dictionaries) into structured JSON.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## License

This project is licensed under the [MIT License](LICENSE).
