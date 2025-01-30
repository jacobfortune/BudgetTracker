def session():
    BudgetFile = open("Budget.txt", "a")
    BudgetFile.close()

    IndexFile = open("Index.txt", "a")
    IndexFile.close()

    EXPENSES = open("Expenses.txt", "a")
    EXPENSES.close()

    INCOMES = open("Income.txt", "a")
    INCOMES.close()

def welcome():
    print("\n" + "\n"
      "1. Add Expense " + "\n"
      "2. Add Income " + "\n"
      "3. View Summary Report " + "\n"
      "4. View Expense by Category " + "\n"
      "5. View Top 3 Highest Expenses " + "\n"
      "6. Show Bar Chart " + "\n"
      "7. Receive Budget Tracker logs" + "\n"
      "8. Quit" + "\n")

def isdigit(id):
    id = str(id)
    if id.isdigit() == True:
        id = int(id)
        if 1 <= id <= 7:
            tr = True
            return tr
        else:
            tr = False
            return tr
    else:
        tr = False
        return tr

def cat(string):
    if string == "food":
        Fair =  True
    elif string == "entertainment":
        Fair =  True
    elif string == "transport":
        Fair =  True
    elif string  == "other":
        Fair = True
    else:
        Fair = False
    return(Fair)

session()

amountrack = ""
track = True
trid = 0
food = ""
entertainment = ""
transport = ""
Budget = ""
longterm = ""
other = ""
top3 = [["", "", ""],[
    0, 0, 0
]]

# This allows the information of the budget checker to be saved past memory.
EXPENSES = open("Expenses.txt", "r")
expense = EXPENSES.read()
EXPENSES.close()

INDEX = open("Index.txt", "r")
index = INDEX.read()
if len(index) == 0:
    index = 1
INDEX.close()

Budgetcheck = open("Budget.txt", "r")
TRACKER = Budgetcheck.read()
TRACKER = str(TRACKER)
Budgetcheck.close()

INCOMES = open("Income.txt", "r")
income = INCOMES.read()
INCOMES.close()

if len(income) > 0:
    Balance = float(income) - float(expense)
    income = float(income)
    expense = float(expense)
elif len(income) < 0:
    Balance = 0.00
    expense = 0.00
    income = 0.00

print("Welcome to Budget Tracker! ")

while track:
    welcome()
    trid = str(input("What would you like to do? | "))
    track = isdigit(trid)
    if track == True:
        trid = int(trid)
        if trid == 1:
            trides = input("Enter description... | ")
            triamount = input("Enter amount... | ")
            onwards = triamount.isnumeric()
            while onwards:
                tricat = input("Enter category... | ")
                tricat = tricat.lower()
                amountrack = amountrack + str(triamount) + "\n"
                valid = cat(tricat)
                if valid:
                    IndexFile = open("Index.txt", "w")
                    IndexFile.write(str(index))
                    index = int(index) + 1
                    IndexFile.close
                    longterm = longterm + "\n" + "Expense no: " + str(index) + "\n" + "Description: " + trides + "\n" + "Amount: " + triamount + "\n" + "Category: " + tricat + "\n"
                    if triamount.isnumeric() == True:
                        expense = expense + float(triamount)
                        Balance = Balance - float(triamount)
                        if float(triamount) > top3[1][2]:
                            if float(triamount) > top3[1][1]:
                                if float(triamount) > top3[1][0]:
                                    top3[0][0] = trides
                                    top3[1][2] = top3[1][1]
                                    top3[1][1] = top3[1][0]
                                    top3[1][0] = float(triamount)
                                else:
                                    top3[0][1] = trides
                                    top3[1][2] = top3[1][1]
                                    top3[1][1] = float(triamount)
                            else:
                                top3[0][2] = trides
                                index = index + 1
                                top3[1][2] = float(triamount)
                        onwards = False
                        tricat = str(tricat)
                        if tricat == "food":
                            food = food + "*"
                        elif tricat == "entertainment":
                            entertainment = entertainment + "*"
                        elif tricat == "transport":
                            transport = transport + "*"
                        elif tricat == "other":
                            other = other + "*"
                else:
                    print("Category was invalid! Please try again... Category can be food, entertainment, transport or other.")
            if triamount.isnumeric() == False:
                print("Amount was invalid! Please try again... ")
        elif trid == 2:
            trides = input("Enter description... | ")
            triamount = input("Enter amount... | ")
            onwards = triamount.isnumeric()
            if onwards == False:
                print("Amount was invalid! Please try again... ")
            while onwards:
                IndexFile = open("Index.txt", "w")
                IndexFile.write(str(index))
                index = int(index) + 1
                IndexFile.close
                income = income + float(triamount)
                Balance = Balance + float(triamount)
                onwards = False
        elif trid == 3:
            print("Total Expenses: " + str(expense))
            print("Total Incomes: " + str(income))
            print("Balance: " + str(Balance))
        elif trid == 4:
            print("Expenses by Category: " + "\n")
            print("Food: " + food)
            print("Transport: " + transport)
            print("Entertainment: " + entertainment)
            print("Other: " + entertainment)
        elif trid == 5:
            print("BIGGEST EXPENSE")
            print(top3[0][0])
            print("SECOND-BIGGEST EXPENSE")
            print(top3[0][1])
            print("THIRD-BIGGEST EXPENSE")
            print(top3[0][2])
            print("")
        elif trid == 6:
            expense1 = expense
            income1 = income
            Balance = balance
            balance1 = balance
            if len(income) > 1 and len(expense) > 1:
                undone = True
                while undone == True:
                    index2 = 2
                    if len(income) > index2 and len(expense) > index2:
                        number = 1 + "0" * index2
                        index2 = index2 + 1
                    elif len(income) < index2 and len(expense) < index2:
                        undone = False
                        income1 = income / int(number)
                        expense1 = expense1 / int(number)
                        balance1 = balance1 / int(number)

            print("E | " + "*" * int(expense1))
            print("X | " + "*" * int(expense1))
            print("P | " + "*" * int(expense1))
            print("E | " + "*" * int(expense1))
            print("N | " + "*" * int(expense1))
            print("S | " + "*" * int(expense1))
            print("E | " + "*" * int(expense1))
            print("")
            print("")
            print("I | " + "*" * int(income1))
            print("N | " + "*" * int(income1))
            print("C | " + "*" * int(income1))
            print("O | " + "*" * int(income1))
            print("M | " + "*" * int(income1))
            print("E | " + "*" * int(income1))
            print("  | " + "*" * int(income1))
            print("")
            print("")
            print("B | " + "*" * int(balance1))
            print("A | " + "*" * int(balance1))
            print("L | " + "*" * int(balance1))
            print("A | " + "*" * int(balance1))
            print("N | " + "*" * int(balance1))
            print("C | " + "*" * int(balance1))
            print("E | " + "*" * int(balance1))
            print("")
        elif trid == 7:
            TRACKER = TRACKER + longterm
            print(TRACKER)
        elif trid == 8:
            track = False

print("Goodbye! ")
EXPENSES = open("Expenses.txt", "w")
EXPENSES.write(str(expense))
EXPENSES.close()

INCOMES = open("Income.txt", "w")
INCOMES.write(str(income))
INCOMES.close()

FINAL = open("Budget.txt", "w")
FINAL.write(TRACKER)
FINAL.close()
