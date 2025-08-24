import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# File to store expenses
DATA_FILE = "expenses.csv"


# Load data or create new
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=["Amount", "Category", "Description", "Date"])


def save_data(df):
    df.to_csv(DATA_FILE, index=False)


# Auto categorize based on keywords
def auto_categorize(description):
    description = description.lower()
    if "food" in description or "restaurant" in description:
        return "Food"
    elif "rent" in description or "house" in description:
        return "Rent"
    elif "uber" in description or "bus" in description or "taxi" in description:
        return "Transport"
    elif "movie" in description or "netflix" in description:
        return "Entertainment"
    else:
        return "Other"


# Add new expense
def add_expense(df):
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")

    category = auto_categorize(description)

    new_entry = pd.DataFrame([[amount, category, description, date]],
                             columns=["Amount", "Category", "Description", "Date"])
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    print("✅ Expense added successfully!")
    return df


# Show all expenses
def view_expenses(df):
    if df.empty:
        print("No expenses yet.")
    else:
        print("\nAll Expenses:")
        print(df)


# Show charts
def show_charts(df):
    if df.empty:
        print("No expenses to plot.")
        return

    # Pie chart by category
    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="pie", autopct='%1.1f%%', figsize=(6, 6))
    plt.title("Expenses by Category")
    plt.show()

    # Line chart by date
    df["Date"] = pd.to_datetime(df["Date"])
    daily_sum = df.groupby("Date")["Amount"].sum()
    daily_sum.plot(kind="line", marker="o", figsize=(8, 4))
    plt.title("Daily Spending")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.show()


# Predict future spending
def predict_future(df):
    if df.empty:
        print("Not enough data to predict.")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.dayofyear
    X = df[["Day"]]
    y = df["Amount"]

    model = LinearRegression()
    model.fit(X, y)

    future_day = [[df["Day"].max() + 7]]  # Predict for 1 week later
    prediction = model.predict(future_day)[0]

    print(f"📈 Predicted spending in 7 days: ${prediction:.2f}")


# Main menu
def main():
    df = load_data()

    while True:
        print("\n💰 Smart Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Charts")
        print("4. Predict Future Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            df = add_expense(df)
        elif choice == "2":
            view_expenses(df)
        elif choice == "3":
            show_charts(df)
        elif choice == "4":
            predict_future(df)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
