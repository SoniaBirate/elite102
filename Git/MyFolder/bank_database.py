import mysql.connector
class customer: 
   global PersonID
   global cnx
   global cursor
   if  __name__ == '__main__':
      try:
         cnx = mysql.connector.connect(user='bank_app', password='04272004', host='Sonias-MacBook-Air.local', database='bank_database')
         print ("this worked")
      except:
         print("something went wrong")

   #Creating a cursor object using the cursor() method
   cursor = cnx.cursor()
   
   PersonID = 5

   def __init__(self):
      global PersonID
      while True:
         inp = input("Type 'Start' to Start and 'Done' to Stop ")
         if inp == "Done":
            break
         self.LastName = input('Enter the customer last name: ')
         self.FirstName = input('Enter the customer first name: ')
         self.PersonID = PersonID + 1
         PersonID += 1

   def customer_account(self):
      global cnx 
      global cursor
      global PersonID 

      # Deleting row in the DataBase
      sql = "DELETE FROM customer_personal_info WHERE PersonID = '5'"
      cursor.execute(sql)
      cnx.commit()


      # Preparing SQL query to INSERT a record into the database.
      insert_stmt = (
         "INSERT INTO customer_personal_info(PersonID,LastName,FirstName)"
         "VALUES (%s, %s, %s)"
      )
      data = (self.PersonID, self.LastName,self.FirstName)

      try:
         # Executing the SQL command
         cursor.execute(insert_stmt, data)
            
            # Commit your changes in the database
         cnx.commit()

      except Exception as ex:
         # Rolling back in case of error
         print(ex)
         cnx.rollback()

      # Closing the connection
      cnx.close()

person1 = customer()
person1.customer_account()

