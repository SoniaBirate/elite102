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
         cursor = cnx.cursor()
      except Error as e:
         print("Error while connecting to MySQL", e)


class customer():
   def __init__(self, LastName, FirstName, City, State, MaritalStatus, DOB, PersonID=None):
      self.LastName = LastName
      self.FirstName = FirstName
      self.City = City
      self.State = State
      self.DOB = DOB
      self.MaritalStatus = MaritalStatus
      if PersonID is None:
          PersonID = random.randint(1111,9999)
      self.PersonID = PersonID

class account():
    def __init__(self, AccountType, AccountBalance, AccountID=None):
        if AccountID is None:
          AccountID = random.randint(1111,9999)
        self.AccountID = AccountID
        self.AccountType = AccountType
        self.AccountBalance = AccountBalance

class bankDataAcess():
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

            except Exception as ex:
                # Rolling back in case of error
                print(ex)
                cnx.rollback()

            # Closing the connection
            cnx.close()
        except: 
            print ("ERROR")


connection1 = customer ("Jones", "Tom", "Austin", "Texas", "Single", "2007-05-01")
print (connection1)
connection2 = account ("Savings" , 20000.00)
connection3 = bankDataAcess (connection1,connection2)
connection3.accessBank()




