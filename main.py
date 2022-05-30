import sqlite3

conn = sqlite3.connect("DBname.db")
c = conn.cursor()
count = 0

#The following are a list of functions that are called at the bottom of this page, and relate directly to the menu items first displayed.

#Function 1. This function creates the table and populates it with some default values (primarily for testing). The first time it is run it will create the table, and subsequent times will display an error. 

def create_table_first():
  global count 
  if count == 0:
    c.execute("CREATE TABLE IF NOT EXISTS EmployeeUOB(EmployeeID INT, empTitle TEXT, forename TEXT, surname TEXT, email TEXT, salary REAL)")
    print("\nTable created successfully.")

    c.execute("INSERT INTO EmployeeUOB VALUES (101, 'Mr', 'Philip', 'Read', 'philipread10@gmail,com', 40000)")
    c.execute("INSERT INTO EmployeeUOB VALUES (201, 'Mrs', 'Sarah', 'Goad', 'SarahGoad110@gmail,com', 41000)")  
    c.execute("INSERT INTO EmployeeUOB VALUES (301, 'Mr', 'Andrew', 'Read', 'AndrewRead12@gmail,com', 42000)")
    c.execute("INSERT INTO EmployeeUOB VALUES (401, 'Mrs', 'Kim', 'Read', 'KimRead@gmail,com', 43000)")  
    c.execute("INSERT INTO EmployeeUOB VALUES (501, 'Mr', 'Chris', 'Read', 'ChrisRead@gmail,com', 80000)")   
    #default table value to be removed
    
    conn.commit()
  else:
    print("\nThis table is already created.")

  count = count+1

#Function 2. This function allows input of new records from the user. It gives a prompt for each field, and assigns each as a variable. It then uses INSERT to populate the table with these variables on a new line.

def input_data():
  employeeID = (input("Enter New Employee ID: "))
  title = (input("Enter New Employee Title: "))
  forename = (input("Enter New Employee Forename: "))
  surname = (input("Enter New Employee Surname: "))
  email = (input("Enter New Employee Email Address: "))
  salary = (input("Enter New Employee Salary: "))

  c.execute("INSERT INTO EmployeeUOB (EmployeeID, empTitle, forename, surname, email, salary) VALUES (?, ?, ?, ?, ?, ?)", (employeeID, title, forename, surname, email, salary))
  conn.commit()

  print("\nNew Employee information added successfully.")

#Function 3. This simply displays all data currently in the table

def show_all_data():
  c.execute("SELECT * FROM EmployeeUOB")
  for row in c.fetchall():
    print(row)

#Function 4. This allows the user to search via Employee ID, and prints the results of the search.

def search_data():
  SearchEmployeeID = (input("Enter Employee ID to search: "))
  data = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
  for row in data:
    print(row)

#Function 5. This allows data currently in the table to be updated. Users are prompted to enter the employee ID of the record they wish to update. They are then asked which field associated with that ID they would like to change. Finally, they are asked what they would like the new value to read. The updated record is then displayed as confirmation.

def update_data():
  SearchEmployeeID = (input("Please enter the employee ID for the record you wish to update: "))
  print ("\nCurrent Employee Data : \n")
  data = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
  for row in data:
    print(row)

  print ("\n 1. Employee ID")
  print (" 2. Title")
  print (" 3. First Name")
  print (" 4. Surname")
  print (" 5. Email")
  print (" 6. Salary")
  print (" 7. Return to main menu\n")
  UpdateField = int(input("Which field would you like to update? Please select a number from the list: "))
  if UpdateField == 1:
    NewVar1 = (input("Enter New EmployeeID: "))
    c.execute("UPDATE EmployeeUOB SET EmployeeID = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("\nThe record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (NewVar1,))
    for row in data2:
      print(row)

  if UpdateField == 2:
    NewVar1 = (input("Enter New Title: "))
    c.execute("UPDATE EmployeeUOB SET empTitle = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("The record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data2:
      print(row)
    
  if UpdateField == 3:
    NewVar1 = (input("Enter New First Name: "))
    c.execute("UPDATE EmployeeUOB SET forename = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("The record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data2:
      print(row)
    
  if UpdateField == 4:
    NewVar1 = (input("Enter New Surname: "))
    c.execute("UPDATE EmployeeUOB SET surname = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("The record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data2:
      print(row)
    
  if UpdateField == 5:
    NewVar1 = (input("Enter New Email: "))
    c.execute("UPDATE EmployeeUOB SET email = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("The record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data2:
      print(row)

  if UpdateField == 6:
    NewVar1 = (input("Enter New Salary: "))
    c.execute("UPDATE EmployeeUOB SET salary = ? WHERE EmployeeID = ?", (NewVar1, SearchEmployeeID,))
    
    conn.commit()

    print("The record has been successfully updated. The new record is : \n")
    data2 = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data2:
      print(row)

  if UpdateField == 7:
    pass

#Function 6. This allows whole records to be deleted. Users search for the ID of the record they wish to delete. Users are asked to confirm whether they are happy to proceed, as it will be a permanent change. 

def delete_data():
  SearchEmployeeID = (input("Enter Employee ID to delete: "))
  print ("\nEmployee Data to be deleted : \n")
  data = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
  for row in data:
    print(row)
  print("\nThis record will be permanently deleted. Are you sure you would like to continue?")
  Confirmation = (input("\nPlease type 'Yes' to confirm: "))
  if Confirmation == 'Yes':
    c.execute("DELETE FROM EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    conn.commit()
    print("\nThe record has been deleted.")
  else:
    print("\nDelete command cancelled.")

#Function 7. Advanced Search. This allows users to search the database based on other criteria. A direct match from the search is required, and will display all results that match the search for a given field. The exception to this is salary, which has the additional functionality of less than, greater than, or equal to.

def advanced_search():
  print ("\n 1. Employee ID")
  print (" 2. Title")
  print (" 3. First Name")
  print (" 4. Surname")
  print (" 5. Email")
  print (" 6. Salary")
  print (" 7. Return to main menu\n")
  SearchBy = int(input("What would you like to search by? Please enter a number from the list above. "))
  if SearchBy == 1:
    SearchEmployeeID = (input("Enter Employee ID to search: "))
    data = c.execute("SELECT * From EmployeeUOB WHERE EmployeeID = ?", (SearchEmployeeID,))
    for row in data:
      print(row)
  if SearchBy == 2:
    Search = (input("Enter Title to search: "))
    data = c.execute("SELECT * From EmployeeUOB WHERE EmpTitle = ?", (Search,))
    for row in data:
      print(row)
  if SearchBy == 3:
    Search = (input("Enter First Name to search: "))
    data = c.execute("SELECT * From EmployeeUOB WHERE forename = ?", (Search,))
    for row in data:
      print(row)
  if SearchBy == 4:
    Search = (input("Enter Surname to search: "))
    data = c.execute("SELECT * From EmployeeUOB WHERE surname = ?", (Search,))
    for row in data:
      print(row)
  if SearchBy == 5:
    Search = (input("Enter email to search: "))
    data = c.execute("SELECT * From EmployeeUOB WHERE forename = ?", (Search,))
    for row in data:
      print(row)
  if SearchBy == 6:
    print ("\n 1. Salary equal to")
    print (" 2. Salary greater than or equal to")
    print (" 3. Salary less than or equal to")
    SearchMaths = int(input("\nHow would you like to filter your search? Please choose a number from the list "))
    if SearchMaths == 1:
      Search = (input("\nSalary equal to : "))
      data = c.execute("SELECT * From EmployeeUOB WHERE salary = ?", (Search,))
      for row in data:
        print(row)
    if SearchMaths == 2:
      Search = (input("\nSalary greater than or equal to : "))
      data = c.execute("SELECT * From EmployeeUOB WHERE salary >= ?", (Search,))
      for row in data:
        print(row)
    if SearchMaths == 3:
      Search = (input("\nSalary less than or equal to : "))
      data = c.execute("SELECT * From EmployeeUOB WHERE salary <= ?", (Search,))
      for row in data:
        print(row)
  if SearchBy == 7:
    pass

#This is where the code initialises, and loops. The menu is displayed, and depending on the selection, will run a particular function from the list above..  

while True:
  print ("\n Menu:")
  print ("**********")
  print (" 1. Create the table 'EmployeeUoB'")
  print (" 2. Insert data into EmployeeUoB")
  print (" 3. Display all data in EmployeeUoB")
  print (" 4. Search for an employee using employee ID")
  print (" 5. Update data (to update a record)")
  print (" 6. Delete data (to delete a record)")
  print (" 7. Advanced Search")
  print (" 8. Exit\n")

  __choose_menu = int(input("What would you like to do? Enter a number from above : "))

  if __choose_menu == 1:
    create_table_first()
  elif __choose_menu == 2:
    input_data()
  elif __choose_menu == 3:
    show_all_data()
  elif __choose_menu == 4:
    search_data()
  elif __choose_menu == 5:
    update_data()
  elif __choose_menu == 6:
    delete_data() 
  elif __choose_menu == 7:
    advanced_search()
  elif __choose_menu == 8:
    print("Goodbye!")
    exit(0)
  else:
    print ("Invalid Choice")
