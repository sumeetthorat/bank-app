'''
x = 10 #Global Var

def fun1():
    y = 20 #Local Var
    print("Inside fun1, locally x=", x)
    print("Inside fun1, locally y=", y)
    #print("Inside fun1, locally z=", z)

def fun2():
    z = 30 #Local Var
    print("Inside fun2, locally x=", x)
    print("Inside fun2, locally z=", z)
    #print("Inside fun1, locally y=", y)

fun1()
fun2()
print("Globally, x=", x)
#print("Globally, y=", y)
#print("Globally, z=", z)
'''

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


















