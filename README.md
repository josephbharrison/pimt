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

```json
[
    {
        "id": "base4-4",
        "set": "Base Set 2",
        "series": "Base",
        "publisher": "WOTC",
        "generation": "First",
        "release_date": "2000-02-24",
        "artist": "Mitsuhiro Arita",
        "name": "Charizard",
        "set_num": "4",
        "types": [
            "Fire"
        ],
        "supertype": "Pokémon",
        "subtypes": [
            "Stage 2"
        ],
        "level": 76,
        "hp": 120.0,
        "evolvesFrom": "Charmeleon",
        "evolvesTo": null,
        "abilities": [
            {
                "name": "Energy Burn",
                "text": "As often as you like during your turn (before your attack), you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is Asleep, Confused, or Paralyzed.",
                "type": "Pokémon Power"
            }
        ],
        "attacks": [
            {
                "name": "Fire Spin",
                "cost": [
                    "Fire",
                    "Fire",
                    "Fire",
                    "Fire"
                ],
                "convertedEnergyCost": 4,
                "damage": "100",
                "text": "Discard 2 Energy cards attached to Charizard in order to use this attack."
            }
        ],
        "weaknesses": [
            {
                "type": "Water",
                "value": "×2"
            }
        ],
        "retreatCost": [
            "Colorless",
            "Colorless",
            "Colorless"
        ],
        "convertedRetreatCost": 3.0,
        "rarity": "Rare Holo",
        "flavorText": "Spits fire that is hot enough to melt boulders. Known to unintentionally cause forest fires.",
        "nationalPokedexNumbers": [
            6
        ],
        "legalities": {
            "unlimited": "Legal"
        },
        "resistances": [
            {
                "type": "Fighting",
                "value": "-30"
            }
        ],
        "rules": null,
        "regulationMark": null,
        "ancientTrait": null,
        "owned": 2
    }
]
```
---

## Contributing

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---
### Acknowledgment

This project utilizes data from the [Pokemon TCG All Cards 1999 - 2023](https://www.kaggle.com/datasets/adampq/pokemon-tcg-all-cards-1999-2023) dataset provided by **AdamPQ** on Kaggle. We greatly appreciate the effort in compiling and maintaining this comprehensive dataset for the Pokémon TCG community.

## License

This project is licensed under the [MIT License](LICENSE).
