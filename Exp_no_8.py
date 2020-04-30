class ATM:
    def __init__(self, name, ac_no, mob_no, addr, pin, bal):
        self.name = name
        self.ac_no = ac_no
        self.mob_no = mob_no
        self.addr = addr
        self.pin = pin
        self.bal = bal

    def Acc_info(self):
        print("Name : ", self.name)
        print("Account Number : ", self.ac_no)
        print("Balance (in Rs) : ", self.bal)
        print("Address : ", self.addr)
        print("Mobile Number : ", self.mob_no)

    def Bal_inq(self):
        print("Name : ", self.name)
        print("Account Number : ", self.ac_no)
        print("Balance (in Rs) : ", self.bal)

    def deposit(self, amt):
        self.bal += amt
        print(amt, " successfully deposited.")
        print("Updated Account Balance : ", self.bal)

    def withdrawal(self, amt):
        if(self.bal >= amt):
            self.bal -= amt
            print(amt, " successfully withdrawed.")
            print("Updated Account Balance : ", self.bal)
        else:
            print("Insufficient balance")
        
    def pin_change(self,ac_n):
        i = 0
        while(i < 3):
            old_pin = int(input("Enter old pin - "))
            if(user[ac_n].pin == old_pin):
                new_pin = int(input("Enter new pin - "))
                self.pin = new_pin
                break
            else:
                print("Incorrect info, try again")
                i += 1
        if i == 2:
            blocked_acc.append(ac_n)

user = ({1000: ATM("abc",1000,9988776655,"Mumbai",190,10000), 1001: ATM("def",1001,9911754565,"Mumbai",745,20000),
        1002: ATM("ghi",1002,7688344123,"Mumbai",439,5000),1003: ATM("jkl",1003,9879567123,"Mumbai",875,30000),
        1004: ATM("mno",1004,1356095686,"Mumbai",243,35000)})

blocked_acc = []

def New_user():
    name = input("Enter name - ")
    mob_no = int(input("Enter your mobile number - "))
    addr = input("Enter address - ")
    pin = int(input("Enter 3 digit pin - "))
    balance = 0
    ac_no = 1000 + len(user)
    user[ac_no] = ATM(name,ac_no,mob_no,addr,pin,balance)

bcnt = 0

while(True):
    count = int(input("Enter choice\n0.Quit\n1.New user\n2.Account Info\n3.Pin change\n4.Balance Enquiry\n5.Withdrawal\n6.Deposit"))
    if count == 1:
        New_user()
    elif count == 2:
        ac = int(input("Enter account number - "))
        if ac in blocked_acc:
            print("Your Account has been blocked")
            break
        pin = int(input("Enter pin - "))
        if user[ac].pin == pin:
            user[ac].Acc_info()
            if bcnt > 0:
                bcnt = 0
        else:
            bcnt += 1
            print("Invalid pin, try again")
    elif count == 3:
        ac = int(input("Enter account number - "))
        if ac in blocked_acc:
            print("Your Account has been blocked")
            break
        user[ac].pin_change(ac)
    elif count == 4:
        ac = int(input("Enter account number - "))
        if ac in blocked_acc:
            print("Your Account has been blocked")
            break
        pin = int(input("Enter pin - "))
        if user[ac].pin == pin:
            user[ac].Bal_inq()
            if bcnt > 0:
                bcnt = 0
        else:
            bcnt += 1
            print("Invalid pin, try again")
    elif count == 5:
        ac = int(input("Enter account number - "))
        if ac in blocked_acc:
            print("Your Account has been blocked")
            break
        pin = int(input("Enter pin - "))
        if user[ac].pin == pin:
            amt = int(input("Enter amount - "))
            user[ac].withdrawal(amt)
            if bcnt > 0:
                bcnt = 0
        else:
            bcnt += 1
            print("Invalid pin, try again")
    elif count == 6:
        ac = int(input("Enter account number - "))
        if ac in blocked_acc:
            print("Your Account has been blocked")
            break
        pin = int(input("Enter pin - "))
        if user[ac].pin == pin:
            amt = int(input("Enter amount - "))
            user[ac].deposit(amt)
            if bcnt > 0:
                bcnt = 0
        else:
            bcnt += 1
            print("Invalid pin, try again")
    else:
        break
    if bcnt == 2 and count != 1:
        blocked_acc.append(ac)