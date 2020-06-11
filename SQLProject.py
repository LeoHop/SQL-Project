#Here I import the nessasary library for this code

import sqlite3

# Establishing a connection to a 
# document that will hold my new database
connection = sqlite3.connect("ScheduleV2.db") #Delete any document that may have this name before running

# A cursor containes information that
# adds information to my connected database
crsr = connection.cursor()
  
#All code until line 131 are SQL
#commands that are building my desired database.
#the crsr.execute commmand is used so that I can add 
#thing to my connected database
sql_command = """CREATE TABLE IF NOT EXISTS Sports (
    Sport_id int PRIMARY KEY,
    Sport_name text not null,
    Start_date text not null,
  	End_date text not null,
   	Avg_length_of_practice int not null
); """

crsr.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Activities(
    Activity_id int PRIMARY KEY,
    Activity_name text not null,
    Start_time text not null,
  	End_time text not null,
 	Day_of_the_week text not null,
		foreign key (Activity_id) References Sports(Sport_id)
  		foreign key (Activity_name) References Sports(Sport_name)
);  """

crsr.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Materials(
    Activity_id int PRIMARY KEY,
    Activity_name text not null,
    Materials_needed text not null,
    	FOREIGN KEY (Activity_id) REFERENCES Activities(Activity_id)
      	FOREIGN KEY (Activity_name) REFERENCES Activities(Activity_name)
); """

crsr.execute(sql_command)

sql_command = """INSERT INTO Sports(Sport_id, Sport_name, Start_date, End_date, Avg_length_of_practice)
VALUES 
 (1, "Water Polo", "2/19/19", "5/19/19", 3)
; """

crsr.execute(sql_command)

sql_command = """INSERT INTO Sports(Sport_id, Sport_name, Start_date, End_date, Avg_length_of_practice)
VALUES 
 (2, "Swimming", "10/15/18", "5/19/19", 3)
; """

crsr.execute(sql_command)

sql_command = """INSERT INTO Sports(Sport_id, Sport_name, Start_date, End_date, Avg_length_of_practice)
VALUES 
 (3, "Golf", "8/15/18", "6/17/19", 2)
; """

crsr.execute(sql_command)

sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 (1, "Water Polo", "3:30", "6:30 PM", "Monday"); """

crsr.execute(sql_command)

sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 (2, "Swimming", "3:30", "6:30 PM", "Tuesday"); """

crsr.execute(sql_command)

sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 (3, "Golf", "3:30", "6:30 PM", "Wednesday"); """

crsr.execute(sql_command)

sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 (4, "Piano", "8", "9:30 PM", "Wednesday"); """

crsr.execute(sql_command)

sql_command = """INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week)
VALUES 
 (5, "Tutoring", "6:45", "7:45 AM", "Thursday, Friday"); """

crsr.execute(sql_command)

sql_command = """ INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
VALUES 
 (1, "Water Polo", "Speedo, Towl"); """

crsr.execute(sql_command)

sql_command = """ INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
VALUES 
 (2, "Swimming", "Speedo, Towl"); """

crsr.execute(sql_command)

sql_command = """ INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
VALUES 
 (3, "Golf", "Golf Bag, Golf Shoes, Towel, Sunglasses"); """

crsr.execute(sql_command)

sql_command = """ INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
VALUES 
 (4, "Piano", "Piano Book, Pencil"); """

crsr.execute(sql_command)

sql_command = """ INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
VALUES 
 (5, "Tutoring", "Pencil, School Bag, Laptop"); """

crsr.execute(sql_command)

#A function that prompts the user bases on weather
#they want to add a sport or an activity. 
def addValues(table):
	Id = input(table + " Id? ")
	Name = input(table + " Name? ")
	MaterialsNeeded = input("What materials do you need? (please use commas between materials) ")
	if table == "Sport":
		StartDate = input("Start Date? ")
		EndDate = input("End Date? ")
		AvgLengthOfPractice = int(input("Average length of practices? (unit is hours, please enter a singular number) "))

		crsr.execute("""INSERT INTO Sports(Sport_id, Sport_name, Start_date, End_date, Avg_length_of_practice) 
	    VALUES ({}, "{}", "{}", "{}", "{}");
	    """.format(Id, Name, StartDate, EndDate, AvgLengthOfPractice))

		crsr.execute("""INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
						VALUES 
						({}, "{}", "{}"); """.format(Id, Name, MaterialsNeeded))

	elif table == "Activity":				#There are diffrent options for the sports table versus the activities table. 
		StartTime = input("Start Time? ")
		EndTime = input("End Time? ")
		DayOfTheWeek = input("Day of week of the activity? ")

		crsr.execute("""
		INSERT INTO Activities(Activity_id, Activity_name, start_time, end_time, day_of_the_week) 
		VALUES ({}, "{}", "{}", "{}", "{}");
		""".format(Id, Name, StartTime, EndTime, DayOfTheWeek))

		crsr.execute("""INSERT INTO Materials(Activity_id, Activity_name, Materials_needed)
						VALUES 
						({}, "{}", "{}"); """.format(Id, Name, MaterialsNeeded))

#User can view all of the sports in the database
crsr.execute("""SELECT Sport_name FROM Sports""")

result = crsr.fetchall() 

print("These are the sports you play:")
for r in result: 
    for c in r:
        print(c, end = ', ')
    
#User can add sports
questionSports = input("Would you like to add a sport? yes/no ")

if questionSports == "yes":
	numb = int(input("How many sports do you want to input? "))
	for i in range(numb):		#This loops the code below so that the user can input multiple tuples at once
		print("New Sport: ")
		addValues("Sport")

#This code is the same format from when I
#showed the user their sports. 
crsr.execute("""SELECT Activity_name FROM Activities""")

result = crsr.fetchall() 

print("These are your activities:")
for r in result: 
    for c in r:
        print(c, end = ', ')

#User can add activities
questionActivities = input("Would you like to add an activity? yes/no ")

if questionActivities == "yes":
	numb = int(input("How many activities do you want to input? "))
	for i in range(numb):
		print("New Activity: ")
		addValues("Activity")

#User can drop a sport
questionDelete = input("Would you like to quit a Sport? yes/no ")

if questionDelete == "yes":
	whichSport = input("Which sport would you like to quit? ")

	crsr.execute("""
	DELETE FROM Sports
	WHERE Sport_name = "{}";""".format(whichSport))

	crsr.execute("""DELETE FROM Materials
					WHERE Activity_name = "{}" """.format(whichSport))

	crsr.execute("""DELETE FROM Activities
					WHERE Activity_name = "{}" """.format(whichSport)) 

# User can drop a sport and add a new one in its place
questionUpdate = input("Would you like to substitue a sport for another? yes/no ")

if questionUpdate == "yes":
	originalSport = input("What is the original sport that you will be replacing? ")
	newSportName = input("What is the name of the new sport you will be substituting? ")
	newID = int(input("What will the new id of the sport be? "))
	newSD = input("What will the new start date be? ")
	newED = input("What will the new end date be? ")
	newST = input("What will the new Start time be? ")
	newET = input("What will the new End time be? ")
	newDOTW = input("What day of the week does your sport practice? (singular day) ")
	newAvg = input("What will the new average length of practice be? (Unit is hours, please enter a singuler number) ")
	newMaterials = input("What are the new materials you will be needing for thsi sport? (please use commas between materials) ")

	crsr.execute(""" UPDATE Sports
				SET Sport_id = {0},
					Sport_name = "{1}",
					Start_date = "{2}",
					End_date = "{3}",
					Avg_length_of_practice = {4}
				WHERE Sport_name = "{5}"  """.format(newID, newSportName, newSD, newED, newAvg, originalSport))

	crsr.execute(""" UPDATE Materials
				Set Materials_needed = "{0}",
					Activity_id = {1},
					Activity_name = "{2}"
				WHERE Activity_name = "{3}" """.format(newMaterials, newID, newSportName, originalSport))

	crsr.execute(""" UPDATE Activities
					Set Activity_id = {0},
						Activity_name = "{1}",
						Start_time = "{2}",
						End_time = "{3}",
						Day_of_the_week = "{4}"
					WHERE Activity_name = "{5}" """.format(newID, newSportName, newST, newET, newDOTW, originalSport))

# User can view all of the activities that they have on a specific day
questionDay = input("Would you like to view all of the activities for a specific day? yes/no ")


if questionDay == "yes":
	whichDay = input("Which day would you like to see all of the activities for? ")

	crsr.execute("""SELECT Activity_name FROM Activities
					WHERE Day_of_the_week = "{}" """.format(whichDay))

	result = crsr.fetchall() 
							#Same format as my code earlier where all of the Activites or Sports are shown
	print("Activities:")
	for r in result: 
	    for c in r:
	        print(c, end = ', ')

#This section of code comits my results

connection.commit()

#This closes the connection between my code and the document

connection.close()
