# Expense Tracker Project - Hex Softwares Internship
# Author: NADAPANA YASWANTH SRI NAGA VENAKT

# Store expenses as a list of dictionaries
expenses = []

def add_expense():
    """Add a new expense"""
    date = input("Enter the date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = float(input("Enter the amount: ₹"))
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def view_expenses():
    """Display all expenses"""
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n📋 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")
    print()

def view_summary():
    """Show total and category-wise summary"""
    if not expenses:
        print("No data available.\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total:.2f}")

    # Category summary
    category_summary = {}
    for exp in expenses:
        category = exp["category"]
        category_summary[category] = category_summary.get(category, 0) + exp["amount"]

    print("\n📊 Category-wise Summary:")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt:.2f}")
    print()

def main():
    print("=== Welcome to Expense Tracker ===")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        print()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("👋 Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
