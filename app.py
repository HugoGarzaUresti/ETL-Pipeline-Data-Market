import pandas as pd
import pyodbc

# Load your data and perform necessary transformations
# This is an example, replace this with your actual data loading and transformation code
data = pd.read_csv('Original_data.csv')

bins = [0, 18, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['<18', '18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
data['Age Group'] = pd.cut(data['AGE'], bins=bins, labels=labels)

transformed_data = data # Replace with actual transformation logic

# Then, the part where you connect to the database and insert data
server = 'financialetl.database.windows.net'
database = 'ETL Pipeline'
username = 'HugoGarza'
password = 'Medicina_84'
conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
table_name = "FinanceT"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Inserting data into the Azure SQL Database
for index, row in transformed_data.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (Gender, Age, InvestInInvestmentAvenues, PreferredInvestmentAvenue, SavingsObjectives, AgeGroup) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, 
        row['GENDER'], row['AGE'], row['Do you invest in Investment Avenues?'], 
        row['Which investment avenue do you mostly invest in?'], 
        row['What are your savings objectives?'], row['Age Group'])

    conn.commit()
# Don't forget to close your connection
cursor.close()
conn.close()
