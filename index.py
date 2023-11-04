import pymysql

# creating connection with database

def createConn():
     return pymysql.connect(host='localhost',database='learnvern',user='root',password='',port=3306)

# create table
# def createTable():
#      conn=createConn()
#      cursor=conn.cursor() #helping to execute query
#      query="create table students(sid int primary key auto_increment,name varchar(50),email varchar(50), address varchar(50))"
#      cursor.execute(query)
#      conn.commit()
#      print("Table created succesfully")
#      conn.close()
# createTable()

# #Insert record in databases
# def insertData(name,email,address):
#      conn=createConn()
#      cursor=conn.cursor()
#      args=(name,email,address)
#      query="insert into students(name,email,address)values(%s,%s,%s)"
#      cursor.execute(query,args)
#      conn.commit()
#      print("Data Inseted")
#      conn.close()
# n=input("Enter Your Name")
# e=input("Enter Your Email")
# a=input("Enter Your Address")
# insertData(n,e,a)

  # fetchAll data
# def showAll():
#      conn=createConn()
#      cursor=conn.cursor()
#      sql="select * from students"
#      cursor.execute(sql)
#      results=cursor.fetchall()
#      for i in results:
#           print(i)
# showAll()
    # fetch all data by single
def singleId(sid):
     conn=createConn()
     cursor=conn.cursor()
     args=(sid)
     query="select * from students where sid=%s"
     cursor.execute(query,args)
     results=cursor.fetchall()
     for i in results:
          print(i)

sid=int(input("Enter your Id"))
singleId(sid) 
