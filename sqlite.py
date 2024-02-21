import sqlite3

def createStudent():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()

    #create the table
    table_info = """
        Create table Student(Id Int, Name Varchar(50), Class varchar(50), Section varchar(50),Marks Int);
    """
    cursor.execute(table_info)

    #Insert students
    cursor.execute("""Insert into Student values(1,'Jack','Data Science','A',90)""")
    cursor.execute("""Insert into Student values(2,'Madan','Data Science','B',100)""")
    cursor.execute("""Insert into Student values(3,'Matt','Data Science','A',86)""")
    cursor.execute("""Insert into Student values(4,'Harry','DevOPS','A',50)""")
    cursor.execute("""Insert into Student values(5,'Ben','DevOPS','A',35)""")

    #Display records
    print("The inserted records are")
    data = cursor.execute("""Select * from student""")
    for row in data:
        print(row)

    connection.commit()
    connection.close()

def createFee():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    
    table_info = """
    Create table Fees(StudentId int, Month varchar(50), Amount decimal);
    """

    cursor.execute("""Insert into Fees values(1,'Baishak',2000)""")
    cursor.execute("""Insert into Fees values(1,'Jesth',3000)""")
    cursor.execute("""Insert into Fees values(2,'Ashad',5000)""")

    #Display records
    print("The inserted records are")
    data = cursor.execute("""Select * from Fees""")
    for row in data:
        print(row)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    createStudent()
    createFee()

