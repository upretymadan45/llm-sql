
import sqlite3

##connect to SQLite
connection = sqlite3.connect("student.db")

#Create a cursor object to insert record,create table
cursor = connection.cursor()

##create the table
# table_info = """
#     Create table Student(Name Varchar(50), Class varchar(50), Section varchar(50),
#     Marks Int);
# """

# table_info = """
#     Create table Fees(StudentId int, Month varchar(50), Amount decimal);
# """

table_info = """
    Alter table Student add column Id int;
"""

cursor.execute(table_info)

# cursor.execute("""Insert into Student values('Manju','Data Science','A',90)""")
# cursor.execute("""Insert into Student values('Madan','Data Science','B',100)""")
# cursor.execute("""Insert into Student values('Ambika','Data Science','A',86)""")
# cursor.execute("""Insert into Student values('Kushal','DevOPS','A',50)""")
# cursor.execute("""Insert into Student values('Sangita','DevOPS','A',35)""")


# cursor.execute("""Insert into Fees values(1,'Baishak',2000)""")
# cursor.execute("""Insert into Fees values(1,'Jesth',3000)""")
# cursor.execute("""Insert into Fees values(2,'Ashad',5000)""")

cursor.execute("""Update Student set Id = 1 where name = 'Manju'""")
cursor.execute("""Update Student set Id=2 where name='Madan'""")
cursor.execute("""Update Student set Id=3 where name='Ambika'""")
cursor.execute("""Update Student set Id=4 where name='Kushal'""")
cursor.execute("""Update Student set Id=5 where name='Sangita'""")


#Display all the records
print("The inserted records are")
data = cursor.execute("""Select * from student""")
for row in data:
    print(row)

#Commit your changes to database
connection.commit()
connection.close()
