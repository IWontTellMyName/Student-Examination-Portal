from matplotlib import pyplot
from prettytable import PrettyTable as PT
import pandas
df=pandas.read_csv("Department.csv") 

def createDept() :
	with open("Department.csv", "a") as file :
		file.write(input("Enter Department ID : ")+",")
		file.write(input("Enter Department Name : ")+",\n")
	print("Department created")

def viewBatch() :
	for i in range (len(df)) :
		print("Enter",i+1,"to choose",df.iat[i,1])
	i=int(input("Select a department : "))-1
	print("These are the batches in",df.iat[i,1],end=" are ")
	print(str(df.iat[i,2]).replace(":", ", "))

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
	df=pandas.read_csv("Department.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a department : ")) -1
	batchList=df.iat[i,2].split(":")
	dfb=pandas.read_csv("Batch.csv")
	Table=PT(["Batch ID","Batch Name"," Average Percentage"])
	
	df=pandas.read_csv("Student.csv")
	for g in range(len(batchList)) :
		for h in range(len(dfb)) :
			if (dfb.iat[h,0]==batchList[g]) :
				BatchTotal=0
				courseList=dfb.iat[h,3].split(":")
				studentList=dfb.iat[h,4].split(":")
				for j in range (len(studentList)) :
					for i in range (len(df)) :
						if (df.iat[i,0]==studentList[j]) :
							BatchTotal+=(Percentage (studentList[j], courseList))
				Table.add_row([dfb.iat[h,0], dfb.iat[h,1], str(int(BatchTotal/len(studentList)))+"%"])
	print (Table)

def LinePlot() :
	df=pandas.read_csv("Department.csv")
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a department : ")) -1
	DeptID=df.iat[i,0]
	batchList=df.iat[i,2].split(":")
	dfb=pandas.read_csv("Batch.csv")
	list=[]
	
	df=pandas.read_csv("Student.csv")
	for h in range(len(dfb)) :
		if (dfb.iat[h,2]==DeptID) :
			BatchTotal=0
			courseList=dfb.iat[h,3].split(":")
			studentList=dfb.iat[h,4].split(":")
			for j in range (len(studentList)) :
				for i in range (len(df)) :
					if (df.iat[i,0]==studentList[j]) :
						BatchTotal+=(Percentage (studentList[j], courseList))
			list.append(BatchTotal//len(studentList))
	#print (list)
	#print (batchList)
	pyplot.plot(list, batchList)
	pyplot.show


print("Enter 1 to create a new department")
print("Enter 2 to view all batches in a department")
print("Enter 3 to average performance for batches in a department")
print("Enter 4 to view average performance as a line plot")
i=int(input("Enter your choice : "))
print()
if (i==1) :
	createDept()
elif (i==2) :
	viewBatch()
elif (i==3) :
	BatchPerf()
elif (i==4) :
	LinePlot()
else :
	print("Invalid Choice")
