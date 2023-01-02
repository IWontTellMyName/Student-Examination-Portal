import matplotlib.pyplot
from prettytable import PrettyTable as PT
import pandas
df=pandas.read_csv("Course.csv") 

def enterMarks() :
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1],"exam")
	i=int(input("Select a exam : ")) -1
	courseID=df.iat[i,0]
	
	mf=100/(int(input("Enter full marks : "))) #multiplicating factor
	print("\nEnter the marks corresponding to the student IDs")
	print("Press Enter if absent or exam invalidated")
	s=""
	dfb=pandas.read_csv("Batch.csv")
	for j in range(len(dfb)) :
		if(courseID in dfb.iat[j,3]) :
			studentList=dfb.iat[j,4].split(":")
			for studentID in studentList :
				inp=input(studentID+" :")
				if inp!="":
					s+=studentID+":"+str(int(int(inp)*mf))+"-"
	df.iat[i,2]=s[0:-1]
	df.to_csv("Course.csv", index=False)
	print("Examination marks has been stored for all students")

def viewPerf() :
	df=pandas.read_csv("Course.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1],"exam")
	i=int(input("Select a exam : ")) -1
	courseID=df.iat[i,0]
	studentMarks=df.iat[i,2].split("-")
	df=pandas.read_csv("Student.csv")
	Table=PT(["Student ID","Student Name","Percentage","Grade"])
	for element in studentMarks :
		pair=element.split(":")
		for i in range(len(df)) :
			if (pair[0]==df.iat[i,0]) :
				Table.add_row([df.iat[i,0], df.iat[i,1], pair[1]+"%",gradeFunction(int(pair[1]))])
	print (Table)

def showStat() :
	df=pandas.read_csv("Course.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1],"exam")
	i=int(input("Select an exam : ")) -1
	courseID=df.iat[i,0]
	studentMarks=df.iat[i,2].split("-")
	print(len(studentMarks),"students appeared for the exam last time")
	
	df=pandas.read_csv("Student.csv")
	total=0
	for element in studentMarks :
		pair=element.split(":")
		total+=int(pair[1])
	print ("The average performance was "+str(total//len(studentMarks))+"%")
	
def gradeFunction(marks) :
	if marks>=90 :
		return "A"
	elif marks>=80 :
		return "B"
	elif marks>=70 :
		return "C"
	elif marks>=60 :
		return "D"
	elif marks>=50 :
	 	return "E"
	else :
	 	return "F"

def scatterPlot() :
	dfs=pandas.read_csv("Student.csv")
	for i in range (len(df)) :
		courseID=df.iat[i,0]
		studentMarks=df.iat[i,2].split("-")
		xlist=[]
		ylist=[]
		for i in range (len(studentMarks)) :
			pair=studentMarks[i].split(":")
			for j in range (len(dfs)) :
				if (dfs.iat[j,0]==pair[0]) :
					xlist.append(int(pair[1]))
					ylist.append(dfs.iat[j,3])
		#print(xlist)
		#print(ylist)
		#print(list(df["Course Name"]))
		pyplot.scatter(xlist, ylist)
	pyplot.legend(list(df["Course Name"]))
	pyplot.show()

print("Enter 1 to enter marks")
print("Enter 2 to view performance")
print("Enter 3 to show exam statistics")
print("Enter 4 to view scatter plot")
i=int(input("Enter your choice : "))
print()
if (i==1) :
	enterMarks()
elif (i==2) :
	viewPerf()
elif (i==3) :
	showStat()
elif (i==4) :
	scatterPlot()
else :
	print("Invalid Choice")