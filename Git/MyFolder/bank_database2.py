import mysql.connector
from mysql.connector import Error
import random 

global cnx
global cursor

if  __name__ == '__main__':
      try:
         cnx = mysql.connector.connect(user='bank_app', password='04272004', host='Sonias-MacBook-Air.local', database='bank_database')
         print ("CONNECTED SUCCESSFULLY!")
         #Creating a cursor object using the cursor() method
         cursor = cnx.cursor(buffered=True)
      except Error as e:
         print("Error while connecting to MySQL", e)

class Customer():
   def __init__(self, PersonID=None):
       print ("WELCOME TO OUR BANKING DATABASE")
       self.LastName = input("Enter the customer's last name: ")
       self.FirstName = input("Enter the customer's first name: ")
       self.City = input("Enter the customer's city: ")
       self.State = input("Enter the customer's state: ")
       self.DOB = input("Enter the customer's DOB: ")
       self.MaritalStatus = input("Enter the customer's marital status: ")
       
       customer_id = '''SELECT max(PersonID) FROM customer_personal_info;'''
       cursor.execute(customer_id)
       result_1 = cursor.fetchone()
       print(result_1[0])
       print()
       if PersonID is None:
          PersonID = result_1[0]+111
       self.PersonID = PersonID

class Account():
    def __init__(self, AccountID=None, AccountBalance=None):
        account_id = '''SELECT max(AccountID) FROM customer_account;'''
        cursor.execute(account_id)
        result_2 = cursor.fetchone()
        print(result_2[0])
        print()
        if AccountID is None:
          AccountID = result_2[0]+211   
        self.AccountID = AccountID
        
        self.AccountType = input("Enter the customer's account type: [Enter Savings or Checking]  ")
        if AccountBalance is None:
          AccountBalance = random.randint(100.00,8000.00)
        self.AccountBalance = AccountBalance

class BankDataAcess():
    def __init__(self, customer_info, account_info):
        self.PersonID = customer_info.PersonID
        self.LastName = customer_info.LastName
        self.FirstName = customer_info.FirstName
        self.City = customer_info.City
        self.State = customer_info.State
        self.DOB = customer_info.DOB
        self.MaritalStatus = customer_info.MaritalStatus
        self.AccountID = account_info.AccountID
        self. AccountType = account_info.AccountType
        self.AccountBalance = account_info.AccountBalance
        print ("Your account balance is " + str(account_info.AccountBalance))
		
    def accessBank(self): 
        try: 
        # Preparing SQL query to INSERT a record into the database.
            insert_stmt_1= (
                "INSERT INTO customer_personal_info(PersonID, LastName, FirstName, City, State, MaritalStatus, DOB)" 
                "VALUES (%s, %s, %s,%s,%s,%s,%s)"
            )
            data_1 = (self.PersonID, self.LastName, self.FirstName, self.City, self.State, self.MaritalStatus, self.DOB)
            insert_stmt_2 = (
                "INSERT INTO customer_account(PersonID,AccountType,AccountBalance,AccountID)"
                "VALUES (%s, %s, %s,%s)"
            )
            data_2 = (self.PersonID, self.AccountType, self.AccountBalance, self.AccountID)

            try:
                # Executing the SQL command
                cursor.execute(insert_stmt_1, data_1)
                cursor.execute(insert_stmt_2, data_2)
                    
                    # Commit your changes in the database
                cnx.commit()
                print(cursor.rowcount, " was inserted.")

            except Exception as ex:
                # Rolling back in case of error
                print(ex)
                cnx.rollback()

            # Closing the connection
            cnx.close()
        except: 
            print ("ERROR")




while True:
    inp = input("Type 'Start' to Start and 'Done' to Stop ")
    if inp == "Done":
        break
    customer = Customer ()
    account = Account ()
    connection = BankDataAcess (customer,account)
    connection.accessBank()




