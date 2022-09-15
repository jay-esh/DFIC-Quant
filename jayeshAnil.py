# BankAccount class formation
class BankAccount:

    # initialzation function or a constructor function
    # it takes in 3 attributes: username, age and subAccounts
    # all these attributes/properties are assigned according to the user input
    # the subAccounts attribute has a default value but can also be assigned by the user input
    def __init__(self, username: str, age: int, subAccounts: dict = None) -> None:
        self.username = username
        self.age = age
        if (age <= 0):
            raise ValueError("Age cannot be negative or zero!")
        if (subAccounts == None):
            self.subAccounts = {"savings": 0}
        else:
            # the balance of a sub-account cannot be negative!
            for value in subAccounts.items():
                if (value[1] < 0):
                    print(value)
                    raise ValueError(
                        "An account cannot have a negative balance!")
            self.subAccounts = subAccounts

    ##########################################################################

    # getIdentity() is a method that prints out the username and the age properties of this Bank Account (class)
    def getIdentity(self) -> None:
        print("username: "+self.username)
        print("age: " + str(self.age))

    ##########################################################################

    # getBalance() is a public method that prints the usernames and the balances of all sub-accounts in this Bank Account (class)

    def getBalance(self) -> None:
        # this `for` loop loops over all the items in the subAccounts: dictionary attribute
        print("Sub-Accounts: ")
        for key, value in self.subAccounts.items():
            print(key + " : " + str(value))

    ##########################################################################

    # addSubAccount() is a public method that adds a sub-account to the bank account instance
    # and prints out all the sub-accounts after the side-effect

    def addSubAccount(self, subAccountName: str, balance: int) -> None:
        # this if statement checks if the sub-account already exists in the instance of the bank account or not
        if (self.__checkAccountName(subAccountName) == True):
            raise ValueError(
                "Sub-Account with this name already exists, pls use a new name!")
        elif (balance > 0):
            self.subAccounts[subAccountName] = balance
        else:
            # a negative number cannot be used as a balance for the sub-account!
            raise ValueError("cannot deposit negative amount!")

    ##########################################################################

    # deposit() is a public method that deposits/adds money into the specified sub-account of the particular bank account instance

    def deposit(self, subAccountName: str, depositAmount: int) -> None:
        # this if statement checks if the sub-account already exists in the instance of the bank account
        if (self.__checkAccountName(subAccountName) == True):
            if (depositAmount > 0):
                self.subAccounts[subAccountName] += depositAmount
            else:
                # cannot deposit a negative number into the balance!
                raise ValueError("cannot deposit negative amount!")

        else:
            raise ValueError(
                "Sub-account does not exist, pls create a new one!")

    ##########################################################################

    # __checkAccountName() is a private method
    # this is used as a helper function to check if the sub-account already exists or not

    def __checkAccountName(self, subAccountName: str) -> bool:
        accountNameList = []
        for key in self.subAccounts.items():
            accountNameList.append(key[0])
        if (subAccountName in accountNameList):
            return True

    ##########################################################################

    # withdraw() is a public method that is used to withdraw/subtract money from the given sub-account
    def withdraw(self, subAccountName: str, withdrawalAmount: int) -> None:
        if (self.__checkAccountName(subAccountName) == True):
            if (self.subAccounts[subAccountName] >= withdrawalAmount & withdrawalAmount >= 0):
                self.subAccounts[subAccountName] -= withdrawalAmount
            else:
                # cannot withdraw more than present in the account, since the balance cannot be a negative number
                # also the withdrawing amount cannot be negative
                raise ValueError(
                    "Withdrawing more than available in the account, or withdrawing amount cannot be negative!")

        else:
            raise ValueError(
                "Sub-account does not exist, pls create a new one!")

    ##########################################################################

    # printSummary is a public method
    # this is used to just print the name of the bank, the user, their sub-account and their respective balances
    def printSummary(self) -> None:
        print("Bank Name: CIBC; " + "username: " +
              self.username + "; Sub-Accounts:" + str(self.subAccounts))

    ##########################################################################


# Test Case
print("Test Case")
###########################################
cibc = BankAccount("jayesh", 10)
cibc.addSubAccount("checking", 10)
cibc.deposit("savings", 100)
cibc.deposit("savings", 100)
cibc.withdraw("checking", 5)
cibc.withdraw("checking", 2)
print("-------------------------------------------------")
cibc.printSummary()
print("-------------------------------------------------")
