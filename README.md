# ETL Project: Finance Data Pipeline
## Project Description
This ETL (Extract, Transform, Load) project aims to streamline the process of extracting financial survey data, transforming it for clarity and improved usability, and loading it into a Microsoft Azure SQL database for further analysis. The project addresses the challenge of working with raw survey data, focusing on demographic information and investment preferences.

## Features
Extraction: Pulls data from a CSV file containing responses from a financial survey.
Transformation: Cleanses and normalizes data, including handling missing values, encoding categorical variables, and normalizing numerical values.
Loading: Inserts the transformed data into a specifically designed table in a Microsoft Azure SQL database.

## Prerequisites
Python 3.x
pandas
scikit-learn
pyodbc
An active Azure SQL database with the required schema setup

## Installation
Clone the repository:

bash
`git clone https://yourrepositorylink.com/yourproject.git`
`cd yourproject`
Set up a virtual environment (optional):
bash
`python -m venv venv
source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

Install required packages:
bash
`pip install -r requirements.txt`

Configure Database Connection:
Update database_config.py with your Azure SQL database connection details.
Prepare your data file:
Place your Original_data.csv file in the project directory or update the script with the correct file path.
Usage
Run the ETL script:

bash
`python app.py`
This will execute the extraction, transformation, and loading process.

Verify the Data:

Check your Azure SQL database to confirm that the data has been loaded correctly.
Project Structure
app.py: The main ETL script.
requirements.txt: Lists all the Python packages that the project depends on.
database_config.py: Contains the database connection configuration (template provided, actual values needed).
Original_data.csv: The source data file (example/template provided).
Contributing
We welcome contributions! Please feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions, please open an issue in the project repository.
