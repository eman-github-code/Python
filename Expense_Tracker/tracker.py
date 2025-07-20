import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

CSV_FILE = 'expenses.csv'

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added.")

def show_summary():
    df = pd.read_csv(CSV_FILE)
    print("\n📊 Expense Summary by Category:")
    print(df.groupby("Category")["Amount"].sum())

def visualize_expenses():
    df = pd.read_csv(CSV_FILE)
    category_totals = df.groupby("Category")["Amount"].sum()
    
    # Pie Chart
    category_totals.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Expenses by Category")
    plt.ylabel("")  # Hide y-label
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Visualize Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    menu()
