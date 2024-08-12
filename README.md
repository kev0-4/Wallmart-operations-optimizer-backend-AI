
---

# Walmart AI Training Data Generator

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This project generates training data for an AI model designed to optimize Walmart's operations. It analyzes product trends, inventory management, sales predictions, and customer behavior insights based on provided datasets.
After data processing model for fine-tuned using google's AI studio
![image](https://github.com/user-attachments/assets/ff62b694-8ab1-4651-9925-3ad64fea4760)

## Features

- Generates diverse prompts for various retail scenarios.
- Creates data-driven answers based on actual Walmart data.
- Performs correlation analysis across different datasets.
- Exports training data in both JSON and CSV formats.

## Prerequisites

- Python 3.x
- Pandas library
- NumPy library
- Google genai library

## Installation

1. Clone the repository: `git clone [repository-url]`
2. Install required libraries: `pip install -r requirements.txt`

## Usage

1. Ensure your Walmart datasets are in the appropriate directory.
2. Run the main script: `python generate_training_data.py`
3. Find the generated training data in the `../data/processed/` directory.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── raw            <- Contains raw datasets for analysis.
│   │    ├── df_Trends.csv
│   │    ├── df_customerSegmentation.csv
│   │    └── df_WallmartSales.csv
│   ├── processed      <- The final, canonical data sets for modeling.
│        ├── walmart_training_data1.json
│        └── walmart_training_data1.csv
├── models             <- Contains script to test tuned model.
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         wallmart and configuration for tools like black.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── setup.cfg          <- Configuration file for flake8.
```

## Output

- **walmart_training_data1.json**: Contains the generated prompts and answers in JSON format.
- **walmart_training_data1.csv**: Contains the generated prompts and answers in CSV format.

## Notes

- Ensure that your input datasets are up-to-date for accurate insights.
- The generated training data can be used to fine-tune language models for retail-specific tasks.

## Contributors

- **[kev0-4]** 



--- 
