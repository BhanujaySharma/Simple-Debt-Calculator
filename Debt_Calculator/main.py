import csv
import sys

# Initialize data as a list of transactions
data = []

# Function to add a transaction
def add_transaction(lender, borrower, amount):
    data.append([lender, borrower, amount])

# Function to load data from a CSV file
def load_data(file_name):
    try:
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                data.append(row)
        print(f"Data loaded from {file_name}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty dataset.")

# Function to write data to a CSV file
def write_to_csv(file_name):
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Lender", "Borrower", "Amount"])  # Write header row
        csv_writer.writerows(data)  # Write data rows
    print(f"Transactions have been written to {file_name}.")

# Function to perform "Query Debt Owed by Person"
def query_debt(person_name):
    debt_owed = 0
    for row in data:
        if row[0] == person_name:
            debt_owed += int(row[2])
        elif row[1] == person_name:
            debt_owed -= int(row[2])
    print(f"{person_name} owes {debt_owed} to all other users.")

# Function to perform "Query Money Owed to Person"
def query_money_owed(person_name):
    money_owed = 0
    for row in data:
        if row[0] == person_name:
            money_owed += int(row[2])
        elif row[1] == person_name:
            money_owed -= int(row[2])
    print(f"All other users owe {person_name} a total of {money_owed}.")

# Function to perform "Query Person with Most Money Owed"
def query_most_money_owed():
    money_owed_dict = {}
    max_money_owed = 0

    for row in data:
        borrower = row[1]
        amount = int(row[2])
        if borrower in money_owed_dict:
            money_owed_dict[borrower] += amount
        else:
            money_owed_dict[borrower] = amount
        max_money_owed = max(max_money_owed, money_owed_dict[borrower])

    people_with_most_money_owed = [person for person, money_owed in money_owed_dict.items() if money_owed == max_money_owed]

    if people_with_most_money_owed:
        if len(people_with_most_money_owed) == 1:
            print(f"The person with the most money owed is {people_with_most_money_owed[0]} ({max_money_owed}).")
        else:
            print("The following people have the most money owed:")
            for person in people_with_most_money_owed:
                print(f"{person} ({money_owed_dict[person]})")
    else:
        print("No data available.")

# Function to perform "Query Person with Most Debt"
def query_most_debt():
    debt_dict = {}
    max_debt = 0

    for row in data:
        lender = row[0]
        amount = int(row[2])
        if lender in debt_dict:
            debt_dict[lender] += amount
        else:
            debt_dict[lender] = amount
        max_debt = max(max_debt, debt_dict[lender])

    people_with_most_debt = [person for person, debt in debt_dict.items() if debt == max_debt]

    if people_with_most_debt:
        if len(people_with_most_debt) == 1:
            print(f"The person who owes the most money is {people_with_most_debt[0]} ({max_debt}).")
        else:
            print("The following people owe the most money:")
            for person in people_with_most_debt:
                print(f"{person} ({debt_dict[person]})")
    else:
        print("No data available.")

def main():
    while True:
        print("\nAvailable commands:")
        print("1. Add Transaction")
        print("2. Query Debt Owed by Person")
        print("3. Query Money Owed to Person")
        print("4. Query Person with Most Money Owed")
        print("5. Query Person with Most Debt")
        print("6. Save Data to CSV")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            lender = input("Enter lender (single character or string without commas): ")
            borrower = input("Enter borrower (single character or string without commas): ")
            amount = input("Enter amount (non-negative integer): ")
            add_transaction(lender, borrower, amount)
        elif choice == '2':
            person_name = input("Enter the person's name: ")
            query_debt(person_name)
        elif choice == '3':
            person_name = input("Enter the person's name: ")
            query_money_owed(person_name)
        elif choice == '4':
            query_most_money_owed()
        elif choice == '5':
            query_most_debt()
        elif choice == '6':
            file_name = input("Enter CSV file name to save data (e.g., 'transactions.csv'): ")
            write_to_csv(file_name)
        elif choice == '7':
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
