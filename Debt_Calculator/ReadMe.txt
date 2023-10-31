---


# Financial Transaction Management System


## Overview


This Python program is a simple command-line interface (CLI) application that allows users to manage financial transactions between individuals. The program can process transactions, provide insights into financial relationships, and save transaction data to a CSV file for future reference.


## Features


1. **Add Transaction**: Users can add financial transactions by specifying the lender, borrower, and the amount involved.


2. **Query Debt Owed by Person**: Users can query how much debt a specific person owes to all other users.


3. **Query Money Owed to Person**: Users can query how much money is owed to a specific person by all other users.


4. **Query Person with Most Money Owed**: The system identifies the person to whom the most money is owed and displays their name along with the total amount.


5. **Query Person with Most Debt**: The system identifies the person who owes the most money to others and displays their name along with the total amount.


6. **Save Data to CSV**: Users can save all the transaction data to a CSV file for record-keeping.


7. **Quit**: Users can exit the program.


## Usage


1. Run the program by executing the `main.py` script.


2. Follow the on-screen prompts to perform actions such as adding transactions, querying debts, and more.


3. Use numeric choices (e.g., 1 for "Add Transaction") to select menu options.


4. Enter the required information when prompted, such as names of individuals, transaction amounts, and file names for data storage.


5. The executable file is in the dist folder, named as main.exe.


## Requirements


- Python 3.x (https://www.python.org/downloads/)


## Getting Started


1. Clone this repository to your local machine.


2. Open a terminal or command prompt.


3. Navigate to the project directory.


4. Run the program by executing the following command:


   ```
   python main.py
   ```


5. Follow the on-screen instructions to interact with the program.


## Example Usage


Here are some example commands and their expected outputs:


- Adding a transaction:
  ```
  1. Add Transaction
  Enter lender (single character or string without commas): Alice
  Enter borrower (single character or string without commas): Bob
  Enter amount (non-negative integer): 100
  ```


- Querying debt owed by a person:
  ```
  2. Query Debt Owed by Person
  Enter the person's name: Alice
  Alice owes 100 to all other users.
  ```


- Querying money owed to a person:
  ```
  3. Query Money Owed to Person
  Enter the person's name: Bob
  All other users owe Bob a total of 100.
  ```


- Querying person with most money owed:
  ```
  4. Query Person with Most Money Owed
  The person with the most money owed is Bob (100).
  ```


- Querying person with most debt:
  ```
  5. Query Person with Most Debt
  The person who owes the most money is Alice (100).
  ```


- Saving data to a CSV file:
  ```
  6. Save Data to CSV
  Enter CSV file name to save data (e.g., 'transactions.csv'): transactions.csv
  Transactions have been written to transactions.csv.
  ```