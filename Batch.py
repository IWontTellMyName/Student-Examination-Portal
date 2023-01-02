from matplotlib import pyplot
from prettytable import PrettyTable as PT
import pandas
df=pandas.read_csv("Batch.csv") 

def createBatch() :
	with open("Batch.csv", "a") as file :
		df=pandas.read_csv("Department.csv")
		for i in range (len(df)) :
			print("Enter",(i+1),"to choose",df.iat[i,1])
		i=int(input("Select a department : ")) -1
		print()
		
		sy=input("Enter the starting year : ")
		BatchID=df.iat[i,0]+sy[2:]
		file.write("\n"+BatchID+","+df.iat[i,0]+" "+sy+"-")
		file.write(input("Enter the ending year : ")+","+df.iat[i,0]+",")
		
		if (str(df.iat[i,2])=="nan") :
			df.iat[i,2]=BatchID
		else :
			df.iat[i,2]=df.iat[i,2]+":"+BatchID
		df.to_csv("Department.csv", index=False)
		
		df=pandas.read_csv("Course.csv")
		nc=int(input("Enter the number of courses : "))
		for cc in range(nc) :
			print()
			for i in range (len(df)) :
				print("Enter",(i+1),"to choose",df.iat[i,1])
			j=int(input("Select a course : ")) -1
			file.write(df.iat[j,0])
			file.write(":" if cc<nc-1 else ",")
			df=df.drop(df.index[j])
		
	print("Batch created with BatchID",BatchID)

def viewCourse() :
	for i in range (len(df)) :
		print("Enter",i+1,"to choose",df.iat[i,1])
	i=int(input("Select a batch : "))-1
	print("The courses in",df.iat[i,1],end=" are ")
	print(str(df.iat[i,3]).replace(":", ", "))

def viewStudent() :
	for i in range (len(df)) :
		print("Enter",i+1,"to choose",df.iat[i,1])
	i=int(input("Select a batch : "))-1
	print("The students in",df.iat[i,1],end=" are ")
	print(str(df.iat[i,4]).replace(":", ", "))

def Percentage(studentID, courseList) :
	totalMarks=0
	dfc=pandas.read_csv("Course.csv")
	for j in range (len(courseList)) :
		for i in range (len(dfc)) :
			if (dfc.iat[i,0]==courseList[j]) :
				studentMarks=dfc.iat[i,2].split("-")
				for element in studentMarks :
					pair=element.split(":")
					if (pair[0]==studentID) :
						totalMarks+=int(pair[1])
	return int(totalMarks/len(courseList))

def BatchPerf() :
	df=pandas.read_csv("Batch.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a batch : ")) -1
	courseList=df.iat[i,3].split(":")
	studentList=df.iat[i,4].split(":")
	Table=PT(["Roll No","Student Name","Percentage"])
	
	df=pandas.read_csv("Student.csv")
	for j in range (len(studentList)) :
		for i in range (len(df)) :
			if (df.iat[i,0]==studentList[j]) :
				Table.add_row([df.iat[i,2], df.iat[i,1], str(Percentage (studentList[j], courseList))+"%"])
	print (Table)

def pieChart() :
	df=pandas.read_csv("Batch.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a batch : ")) -1
	courseList=df.iat[i,3].split(":")
	studentList=df.iat[i,4].split(":")
	list=[]
	
	df=pandas.read_csv("Student.csv")
	for j in range (len(studentList)) :
		for i in range (len(df)) :
			if (df.iat[i,0]==studentList[j]) :
				group=int((Percentage(studentList[j], courseList)-0.01)/10)*10
				list.append(str(group)+"%-"+str(group+10)+"%")
	pandas.Series(list).value_counts().plot(kind='pie')
	#print (list)
	pyplot.show()


print("Enter 1 to create a new batch")
print("Enter 2 to view all courses in a batch")
print("Enter 3 to view all students in a batch")
print("Enter 4 to view Batch performance")
print("Enter 5 to view pie chart")
i=int(input("Enter your choice : "))
print()
if (i==1) :
	createBatch()
elif (i==2) :
	viewCourse()
elif (i==3) :
	viewStudent()
elif (i==4) :
	BatchPerf()
elif (i==5) :
	pieChart()
else :
	print("Invalid Choice")
