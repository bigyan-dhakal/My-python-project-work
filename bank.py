#Atm mechince

def show_balance():
    print("*****************************")
    print(f"your balance is {balance:.2f}")
    print("*****************************")

def deposit():
    amount=float(input("Enter amount to deposit:"))
    if amount< 0:
        print("That is not valid amount")
        return 0
    else:
      return amount
        

def withdraw():
   amount=float(input("Enter the amount to withdraw:"))
   if amount>balance:
    print("INSOFICIENT amount")
    return 0
   else:
    return amount

balance = 0
is_working = True


while is_working:
    print("*****************************")
    print("Banking program for chads")
    print("*****************************")

    print("1.show balance")
    print("2.Deposit")  
    print("3.Withdraw")      
    print("4.Exit")

    print("*****************************")      
    choice=input("Enter your choice: ")
    print("*****************************")

    match choice:
        case "1":
            show_balance()
        case "2":
           balance +=deposit()
        case "3":
            balance -=withdraw()
        case "4":
            is_working=False
        case _:
         print("*****************************")
         print("That is not the valid choice")
         print("*****************************")   

print("*****************************")
print("Thank you! Have a nice day!! ")
print("*****************************")