# -*- coding: utf-8 -*-
"""Final Project 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/GeneralKoot/6630b5dde34f97e83a89a2e80dc13147/final-project-3.ipynb

# This project involves using SQLite and pandas in order to do some data analysis on the CTA data from 2001 to 2020.
"""

'''The first 4 functions required in this project are in the below cell'''

'''How to Call Functions(I put all the callings of the functions in the bottom 
    of the cell but just in case, here is how you can call it):
    1. In order to call the extract function, the grader needs to type
        'extract(name of csv file, name of db file)'. I personally did 
        'extract("/content/final_bus_data.csv", "bus_data.db")' but depending on
        what the file is called for the grader, this can vary. 
    2. In order to call the display_data function, the user simply needs to type
        'display_data()'
    3. In order to call the display_average_rides function, the user needs to 
        type 'display_average_rides()'
    4. In order to call the display_certain_average function, the user needs to
        type 'display_certain_average() and then feed in the daytype he wants 
        to choose. Example is 'display_certain_average(daytypes = ["A","W"])'. I
        included all possible options in the bottom of the cell.
    5. In order to call the update function, the user needs to type in 'update().
        It is also important to note that the display_data() function needs to be
        called as well in order to see the results of this function.'''



import pandas as pd
import sqlite3
import plotly.express as px

'''This function converts a csv file of CTA data into a SQLite data frame using
pandas, sqlite commands, and some python code. This is the first required function
of the project.'''
def extract(filename, dbname):
  #The csv file data is being read through pandas and is stored into the variable data
  #The names of headers are created using pandas code.
  data = pd.read_csv(filename, names = ["Route", "Date", "Daytype", "Rides"], skiprows = [0])

  #Establishing a connection to the sqlite database
  conn = sqlite3.connect(dbname)
  #Creating a cursor in order to execute commands
  cur = conn.cursor()
  #Creating a table called 'BusData" that stores the pandas data.
  #Has headers 'Route', 'Date', 'Daytype', 'Rides'
  cur.execute("CREATE TABLE BusData (Route text, Date text, Daytype text, Rides int)")

  #For loop to iterate over data, store the data into variables, and then insert
  #those variables into the empty sqlite table
  for i in range(len(data)):
    a = data["Route"][i]
    a = "'" + a + "'"
    b = data["Date"][i]
    b = "'" + b + "'"
    c = data["Daytype"][i]
    c = "'" + c + "'"

    d = data["Rides"][i]

    #Values of Route, Date, Daytype, and Rides are inserted into the sqlite table
    #using string formatting and sql commands
    cur.execute("INSERT INTO BusData VALUES (%s,%s,%s,%i)" % (a,b,c,d))

  #Committing the whole function's code
  conn.commit()
  #Closing the connection
  conn.close()

'''Function that displays the data in the SQL table that was created above. This
is technically still part of the first problem in the project'''
def display_data():
  #Connecting to the db database holding the data
  conn = sqlite3.connect("bus_data.db")
  #Creating a cursor to execute commands
  cur = conn.cursor()
  #Selecting everything from the BusData table
  sql = "SELECT * FROM BusData"
  #Executing the above command
  columns = cur.execute(sql)
  #Using the fetchall method to get all the data
  all_entries = columns.fetchall()
  #For loop to iterate over all the data and print
  for entry in all_entries:
    print(entry)


'''This is the second problem of the project description. It returns the average
of the entire Rides column in the database.'''
def display_average_rides():
  #Establishing a connection with db database
  conn = sqlite3.connect("bus_data.db")
  #Creating a cursor in order to execute commands
  cur = conn.cursor()
  #SQl command to get the average of all rides in the database
  sql3 = "SELECT AVG(Rides) FROM BusData"
  #Storing the execution of the above command into 'average' and then fetching
  #the 1 number(average)
  average = cur.execute(sql3).fetchone()[0]
  print("Overall Average: ", average)


'''This is the third problem in the project description. It returns the average
of certain daytypes(based off of what the user gives). For some reason, when
2 or more daytype arguments are given, it prints the total average twice. Not 
sure why...'''
def display_certain_average(**kwargs):
  #Establishing a connection with database
  conn = sqlite3.connect("bus_data.db")
  #Creating a cursor to execute commands
  cur = conn.cursor()
  #Iterating over the key,value pair of the **kwargs argument
  for key,value in kwargs.items():
    #Furthermore iterating over all the elements in the value(daytypes)
    for x in value:
      #If condition to check how many daytypes were given. If the number is 3, 
      #then simply do the same code as the previous function(return overall
      #average)
      if len(value) == 3:
        sql3 = "SELECT AVG(Rides) FROM BusData"
        average1 = cur.execute(sql3).fetchone()[0]
        print("Overall Average: ", average1)
        #If only 1 daytype value was given and it is 'U', then get the average
        #of rides from the BusData table where the DayType is 'U' using SQL commands
      if len(value) == 1 and x == "U":
        var1 = "SELECT AVG(Rides) FROM BusData WHERE DayType == 'U'"
        average2 = cur.execute(var1).fetchone()[0]
        print("Average for Daytype U: ", average2)
        #If only 1 daytype value was given and it is 'W', then get the average
        #of rides from the BusData table where the DayType is 'U' using SQL commands
      if len(value) == 1 and x == "W":
        var2 = "SELECT AVG(Rides) FROM BusData WHERE DayType == 'W'"
        average3 = cur.execute(var2).fetchone()[0]
        print("Average for Daytype W: ", average3)
        #If only 1 daytype value was given and it is 'A', then get the average
        #of rides from the BusData table where the DayType is 'U' using SQL commands
      if len(value) == 1 and x == "A":
        var3 = "SELECT AVG(Rides) FROM BusData WHERE DayType == 'A'"
        average4 = cur.execute(var3).fetchone()[0]
        print("Average for Daytype A: ", average4)
        #If 2 daytypes value were given and they are 'U' and 'W', then get the total
        #average of rides from the BusData table where the DayType is 'U' or 'W' using SQL commands
      if len(value) == 2 and "U" and "W" in x:
        var4 = "SELECT AVG(Rides) FROM BusData WHERE Daytype == 'U' or Daytype == 'W'"
        average5 = cur.execute(var4).fetchone()[0]
        print("Average for Daytype U and W: ", average5)
        #If 2 daytypes value were given and they are 'U' and 'A', then get the total
        #average of rides from the BusData table where the DayType is 'U' or 'A' using SQL commands
      if len(value) == 2 and "U" and "A" in x:
        var5 = "SELECT AVG(Rides) FROM BusData WHERE DayType == 'U' or Daytype == 'A'"
        average6 = cur.execute(var5).fetchone()[0]
        print("Average for Daytype U and A: ", average6)
        #If 2 daytypes value were given and they are 'A' and 'W', then get the total
        #average of rides from the BusData table where the DayType is 'A' or 'W' using SQL commands
      if len(value) == 2 and "A" and "W" in x:
        var6 = "SELECT AVG(Rides) FROM BusData WHERE DayType == 'A' or Daytype == 'W'"
        average7 = cur.execute(var6).fetchone()[0]
        print("Average for Daytype A and W: ", average7)

'''This is the fourth problem in the project description. It requires us to 
add 10 to the rides where the route is 3 and it is the first day of the month.
This function is really buggy for some reason. It will work for me once and then
stop working. I guess if you want to keep running the function over and over again,
it wont keep updating the rides(it only does it once).'''
def update():
  #Establishing a connection with the database
  conn = sqlite3.connect("bus_data.db")
  #Creating a connection in order to execute commands
  cur = conn.cursor()
  #SQL command to add 10 to the rides column of busdata only if the Route is 3 
  #and the substring of Date gives the number 1(first day of the month).
  # For example, running the substring method on '3/1/2020' will return '1/'
  #I had to do 2 substring method calls because the month column can either be 
  #1 character or 2 characters
  sql = "UPDATE BusData SET Rides = Rides + 10 WHERE Route == '3' and (SUBSTR(Date, 3, 4) == '1/' or SUBSTR(Date, 4, 5) == '1/')"
  #Command above is being executed
  var1 = cur.execute(sql)
  #Committing the changes
  conn.commit()
  #Closing the connection
  conn.close()

'''In case the function above for updating the ride values doesn't work, try this
one. It simply uses pandas instead of some of the SQL code in order to do the same
thing. In order to call it, simply do the same as the previous function but 
change the name of the call to backup_update()'''
def backup_update():
  #Establishing a connection
  conn = sqlite3.connect("bus_data.db")
  #Creating a cursor
  cur = conn.cursor()
  #Selecting all data from busdata
  query = "SELECT * FROM BusData"
  #Reading data using pandas sql reading function
  df = pd.read_sql(query, con=conn)
  #Creating the date column by using pandas 'to_datetime' method
  df['Date'] = pd.to_datetime(df.Date, format='%m/%d/%Y')
  #Using strftime to get just the days from the date column
  df['day'] = df['Date'].dt.strftime('%d')

  #Iterating through the days column
  for x in df['day']:
    #Checks to see if it is the first day
    if x == '01':
      #Adds 10 to the Rides if the if statement condition is met and the 
      #route is 3
      sql = "UPDATE BusData SET Rides = Rides + 10 WHERE Route = '3'"
      var1 = cur.execute(sql)
  conn.commit()
  conn.close()

'''These are all the sample callings of the above functions that works for this 
cell of code. Directions for how to call on your own is in the intro.'''
# extract("/content/final_bus_data.csv", "backup_bus_data.db")
extract("/content/final_bus_data.csv", "bus_data.db")
display_data()
# update()
# pandemic_effect()
# display_average_rides()
# display_certain_average(daytypes = ["A","U"])
# display_certain_average(daytypes = ["U","W"])
# display_certain_average(daytypes = ["W","A"])
# display_certain_average(daytypes = ["U"])
# display_certain_average(daytypes = ["A"])
# display_certain_average(daytypes = ["W"])

"""# This code below analyzes the effect of the pandemic on the CTA ridership and displays averages, graphs, etc..."""

'''This is the 5th problem on the project description. It uses pandas to make
data analysis on how the pandemic effected ridership. Graphs are also created
using plotly.'''
def pandemic_effect():
  #Establishing a connection with the database
  conn = sqlite3.connect("bus_data.db")
  #Creating a cursor for executing commands in SQL
  cur = conn.cursor()
  #Selecting everything from the BusData and storing it in a variable
  query = "SELECT * FROM BusData"
  #Reading the sql data back into pandas
  df = pd.read_sql(query, con=conn)
  #Using the to_datetime method in pandas to convert Date to datetime format
  df['Date'] = pd.to_datetime(df['Date'])
  #Setting a variable 'mask' to be all the dates before 3/11/2020 (lockdown date)
  mask = (df['Date'] >= '1/1/2001') & (df['Date'] < '3/11/2020')
  #Setting before_pandemic to be all the rows and columns of the mask values using df.loc
  before_pandemic = df.loc[mask]
  #Setting a variable 'mask2' to be all dates after 3/11/2020 (lockdown date)
  mask2 = (df['Date'] > '3/11/2020')
  #Using loc method to set after_pandemic to be all the rows and columns containing mask2 values
  after_pandemic = df.loc[mask2]

  #Using mean() pandas method to get the mean of rides before pandemic
  before_pandemic_avg = before_pandemic['Rides'].mean()
  print("Before Pandemic Average Rides: ", before_pandemic_avg)
  #Using mean() pandas method to get the mean of rides after pandemic
  after_pandemic_avg = after_pandemic['Rides'].mean()
  print("After Pandemic Average Rides: ", after_pandemic_avg)
  before_pandemic_max = before_pandemic['Rides'].max()
  print("Before Pandemic Maximum Rides: ", before_pandemic_max)
  #Using max() pandas method to get the max of rides after pandemic
  after_pandemic_max = after_pandemic['Rides'].max()
  print("After Pandemic Maximum Rides: ", after_pandemic_max)
  #Using sum() pandas method to get the sum of all rides before pandemic
  before_pandemic_sum = before_pandemic['Rides'].sum()
  print("Before Pandemic Total Rides: ", before_pandemic_sum)
  #Using the sum() pandas method to get the sum of all rides after pandemic
  after_pandemic_sum = after_pandemic['Rides'].sum()
  print("After Pandemic Total Rides: ", after_pandemic_sum)
  #Using plotly histogram to display rides before pandemic
  fig = px.histogram(before_pandemic, x="Rides",title="Countplot of Rides Before Pandemic")
  fig.show()
  #Using plotly histogram to display rides after pandemic
  fig2 = px.histogram(after_pandemic, x="Rides",title="Countplot of Rides After Pandemic")
  fig2.show()
  #Using plotly histogram to dislay the rides based on certain daytypes before pandemic
  fig3 = px.histogram(before_pandemic, x="Rides", color='Daytype',title="Countplot of Rides vs Daytype Before Pandemic")
  fig3.show()
  #Using plotly histogram to display rides based on certain daytypes after pandemic
  fig4 = px.histogram(after_pandemic, x="Rides", color='Daytype',title="Countplot of Rides vs Daytype After Pandemic")
  fig4.show()


pandemic_effect()
