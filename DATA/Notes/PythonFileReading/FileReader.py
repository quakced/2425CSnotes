'''
    Flat File Database - txt, csv, xlsx - one file for your entire db
    Relational Database - multiple tables and/or multiple files
    
    Text File Extension - you will see the word text file, it means a file of text
     - txt - literally a file full of text with no set formating
     - csv - comma seperated version - each column of data is seperated by a ,
     - tsv - tab seperated version - \t
     - json - java script object notation - key word to value
     - xlsx - Excel or big bloated version of a csv file
     
    Delineator - the thing that seperates the columns in your file - , \t | space
    
    CRUD - Acronym for 4 basic functions of database
        C - Create
        R - Read
        U - Update
        D - Delete
'''
##### CREATE A TEXT FILE  ##########
#with open(FILENAME,mode) as alias
with open("Classroom.txt","w+") as file:
    students=["Mike","Riley","Ezra","Eggvin","Johana"]
    out=""
    for eachNames in students:
        out+=eachNames+"\n"
    
    file.write(out)
    file.close()  #If you do not close your file, you could potentially corrupt your file

##### CREATE Multiple TEXT FILE  ##########    
students=["Mike","Riley","Ezra","Eggvin","Johana"]
for eachStud in students:
    with open(f"{eachStud}.txt","w+") as file:
        file.write(f"{eachStud}'s Profile\n")
        file.close()

##### WRITING TO A TEXT FILE  ##########
with open("Classroom.txt","w") as file:
    #data to write 
    students=["Mike","Riley","Ezra","Eggvin","Johana"]
    id=["01110","00111","10001","00101","00110"]
    out=""
    for i in range(len(id)):
        out+=f"{id[i]},{students[i]}\n"
    
    #writing the data
    file.write(out)
    file.close()  #If you do not close your file, you could potentially corrupt your file
    
##### READING A TEXT FILE  ##########
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines()   #other ways to read to, just Google it
    print(theWholeFile)
    file.close()    

##### APPEND TO A TEXT FILE  #########
with open("Classroom.txt","a") as file:
    newStudent = "00000,Bander\n"
    file.write(newStudent)
    file.close()

##### UPDATE A TEXT FILE  ##########
colors=["green","Chartreuse","Purple","Blue","Red","Silver"]
#Pull data from sheet
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines()   #other ways to read to, just Google it
    print(theWholeFile)
    file.close()    

#Clean Your Data
cleanData=[]
for eachLine in theWholeFile:
    cleanData.append(eachLine.rstrip())   #rstrip removes the \n at the end of a str

print(50*"\n")
# for eachLine in cleanData:
#     print(eachLine)

#Update data
for i in range(len(colors)):
    cleanData[i]+=f",{colors[i]}\n"
print(cleanData)

#Rewrite data
with open("Classroom.txt","w") as file:
    #data to write 
    out=""
    for i in range(len(cleanData)):
        out+=cleanData[i]
    
    #writing the data
    file.write(out)
    file.close()  #If you do not close your file, you could potentially corrupt your file

##### DELETE Info from A TEXT FILE  ##########
#Pull data from sheet
print(50*"\n")
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines()   #other ways to read to, just Google it
    print(theWholeFile)
    file.close()
#Delete data
idToDelete="00110"
for i in range(len(theWholeFile)-1):
    if theWholeFile[i].__contains__(idToDelete):
        theWholeFile.pop(i)
print(theWholeFile)

#Rewrite data
#Rewrite data
with open("Classroom.txt","w") as file:
    #data to write 
    out=""
    for i in range(len(theWholeFile)):
        out+=theWholeFile[i]
    
    #writing the data
    file.write(out)
    file.close()  #If you do not close 

#deleting files
import os
file_path = "path/to/your/file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
else:
    print(f"File '{file_path}' does not exist.")