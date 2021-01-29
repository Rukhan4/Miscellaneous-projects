"""
Create a class called Account which will be an abstract class for three other classes
called CheckingAccount, SavingsAccount and BusinessAccount.
Manage credits and debits from these accounts through an ATM style program.
"""


class Account:
    def __init__(self, customer_id):
        self.customer_id = customer_id


class CheckingAccount(Account):
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_dec = 0

        # returns a string, formatted to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_all = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_dec = int(self.numstr[self.numstr.find('.')+1])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):

        # separate the whole number from decimal number of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_dec = int(numstr[numstr.find('.')+1:])

        # If the amount in the account > requested amount, proceed with withdrawal
        if self.amount > float(withdraw_amount):
            self.amount_all -= self.withdraw_whole

    # if the decimal value of requested amount is  greater than the decimal value of the amount in the account,
    # 1 dollar is taken out and then the remaining decimal value is calculated

            if self.withdraw_dec > self.amount_dec:
                self.amount_dec = self.withdraw_dec - self.amount_dec
                self.amount_all -= 1
                self.amount_dec = 100 - self.amount_dec
            else:
                self.amount_dec -= self.withdraw_dec

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_all) + "." + str(self.amount_dec)

            # Cast the value back to a floating point
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw more than what is present in the account.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


class SavingsAccount(Account):
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_dec = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_all = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_dec = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # separates the whole number from decimal of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_dec = int(numstr[numstr.find('.') + 1:])

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_all -= self.withdraw_whole

        # if the decimal value of requested amount is greater than the
        # decimal value of the amount in the account, then 1 dollar is taken out
        # and then calculates the remaining decimal value
            if self.withdraw_dec > self.amount_dec:
                self.amount_dec = self.withdraw_dec - self.amount_dec
                self.amount_all -= 1
                self.amount_dec = 100 - self.amount_dec
            else:
                self.amount_dec -= self.withdraw_dec

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_all) + "." + str(self.amount_dec)

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw more than what is present in the account.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


class BusinessAccount(Account):
    def __init__(self, customer_id, deposit_amount):
        Account.__init__(self, customer_id)
        self.amount = deposit_amount
        self.withdraw_whole = 0
        self.withdraw_dec = 0

        # returns a string, formatted up to 2 decimal places
        self.numstr = "%.2f" % deposit_amount

        # pulls the whole number from amount as integer
        self.amount_all = int(self.numstr[:self.numstr.find('.')])

        # pulls the decimal value from amount as integer
        self.amount_dec = int(self.numstr[self.numstr.find('.') + 1:])

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        # separates the whole number from decimal of the amount to withdraw
        self.withdraw_whole = int(withdraw_amount[:withdraw_amount.find('.')])
        numstr = str(withdraw_amount)
        self.withdraw_dec = int(numstr[numstr.find('.') + 1:])

        # if the amount in the account is greater than the requested amount,
        # then it is allowed to withdraw that amount
        if self.amount > float(withdraw_amount):
            self.amount_all -= self.withdraw_whole

        # if the decimal value of requested amount is greater than the
        # decimal value of the amount in the account, then 1 dollar is taken out
        # and then calculates the remaining decimal value
            if self.withdraw_dec > self.amount_dec:
                self.amount_dec = self.withdraw_dec - self.amount_dec
                self.amount_all -= 1
                self.amount_dec = 100 - self.amount_dec
            else:
                self.amount_dec -= self.withdraw_dec

            # puts back together the whole number and decimal value as one but as a string
            new_amount = str(self.amount_all) + "." + str(self.amount_dec)

            # type cast the value back to floating point value
            self.amount = round(float(new_amount), 2)
        else:
            print("Error! Cannot withdraw more than what is present in the account.")

    def display_amount(self):
        print(self.amount)

    def get_amount(self):
        return self.amount


if __name__ == "__main__":
    isSessionON = True
    isCustomer = False

    def initialize_objects():
        global x_checking, y_savings, z_business, master_list

        x_checking = CheckingAccount(1, 3422.50)
        y_savings = SavingsAccount(2, 14500.40)
        z_business = BusinessAccount(3, 49834.90)

        master_list = [[x_checking, 1, 1], [y_savings, 2, 2], [z_business, 3, 3]]

        return None

    initialize_objects()

    while isSessionON is True:
        print("Welcome to 24 hour online ATM services.")
        print("Please Insert your card chip side down.")

        # Card reading customer info
        customer_id = input("Enter your customer id number: ")
        print("\n")

        customer_accounts = []
        for i in master_list:
            if i[1] == customer_id:
                customer_accounts.append(i[2])
                isCustomer = True

        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:
                print("Enter 1 for checking account")
                print("Enter 2 for savings account")
                print("Enter 3 for business account")
                account_type = input("Enter which account to use: ")

                if account_type in customer_accounts:
                    for x in master_list:
                        if account_type == x[2]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 for deposits")
                        print("Press 4 to exit.")
                        action = input("Please enter your choice: ")

                    if action == 1:
                        objectName.display_amount()
                        print("\n")

                    if action == 2:
                        amount_to_withdraw = input("Enter amount to withdraw: ")
                        temp_str = str(amount_to_withdraw)

                        adjusted_amount = "%.2f" % amount_to_withdraw
                        objectName.withdraw(adjusted_amount)

                        print("Current balance is:", objectName.get_amount())
                        print("\n")

                    if action == 3:
                        amount_to_deposit = input("Enter amount to deposit: ")
                        temp2_str = str(amount_to_deposit)

                        adjusted_amount = "%.2f" % amount_to_deposit
                        objectName.deposit(adjusted_amount)

                        print("Current balance is:", objectName.get_amount())
                        print("\n")

                    if action == 4:
                        isAccountSessionOn = False
                        print("Thank for using the 24-hour ATM service.")
                        print("Have a pleasant day.")
                        print("\n\n")

                else:
                    print("You do not have that account")
                    print("Please try again. \n")

        else:
            print("Cannot find your record")
            print("Please get your card.")
            print("Exiting this session...")
