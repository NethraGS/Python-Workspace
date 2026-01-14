# ATM Withdrawal Program
# Demonstrates that the 'finally' block ALWAYS executes

balance = 5000

def withdraw_money(amount):
    global balance
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise RuntimeError("Insufficient balance")

    balance -= amount
    return balance


try:
    print("Welcome to the ATM")

    user_input = input("Enter amount to withdraw: ")
    amount = float(user_input)

    remaining_balance = withdraw_money(amount)
    print(f"Withdrawal successful!")
    print(f"Remaining balance: ₹{remaining_balance}")

except ValueError as ve:
    print("Input Error:", ve)

except RuntimeError as re:
    print("Transaction Error:", re)

except Exception as e:
    print("Unexpected Error occurred.")

else:
    print("Transaction completed without errors.")

finally:
    print("\n--- SESSION CLOSED ---")
    print("Thank you for using the ATM!")