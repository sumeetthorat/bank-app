balance = 0
def check_balance():
    print("Total Balance:", balance)

def deposit(amt):
    global balance
    balance = balance + amt
    print(amt, "Rs. deposited.")

def withdraw(amt):
    global balance
    balance = balance - amt
    print(amt, "Rs. withdrawn.")

while True:
    choice = int(input("\nEnter Choice:\n1.Deposit Cash\t2.Withdraw Cash\n3.Check Balance\t4.Exit"))
    match choice:
        case 1:
            print("Deposit Cash")
            d_amt = int(input("Enter Amopunt to Deposit:"))
            deposit(d_amt)
        case 2:
            print("Withdraw Cash")
            w_amt = int(input("Enter Amopunt to Withdraw:"))
            withdraw(w_amt)
        case 3:
            print("Check Balance")
            check_balance()
        case 4:
            print("Exiting...")
            break
        case _:
            print("INVALID CHOICE...")


















