import matplotlib.pyplot as plt
from prettytable import PrettyTable as PT
import pandas
df=pandas.read_csv("Course.csv") 

def createCourse() :
	index=len(df)
	courseID=int(df.iat[index-1,0][-3:])+1
	if courseID<10 :
		courseID="C00"+str(courseID)
	elif courseID<100 :
		courseID="C0"+str(courseID)
	else :
		courseID="C"+str(courseID)
	df.at[index]=[courseID,input("Enter Course Name : "),""]
	df.to_csv("Course.csv", index=False)
	print("Course added with Course ID "+courseID)

def viewPerf() :
	df=pandas.read_csv("Course.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a course : ")) -1
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

def viewHistogram() :
	df=pandas.read_csv("Course.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a course : ")) -1
	courseID=df.iat[i,0]
	studentMarks=df.iat[i,2].split("-")
	df=pandas.read_csv("Student.csv")
	list=[]
	for i in range (len(studentMarks)) :
		pair=studentMarks[i].split(":")
		list.append(gradeFunction(int(pair[1])))
	pandas.Series(list).value_counts().plot(kind='bar')
	#print(list)
	plt.show()

print("Enter 1 to create a new Course")
print("Enter 2 to see marks of all students in a course")
print("Enter 3 to view histogram of number of students in each grade")
i=int(input("Enter your choice : "))
print()
if (i==1) :
	createCourse()
elif (i==2) :
	viewPerf()
elif (i==3) :
	viewHistogram()
else :
	print("Invalid Choice")