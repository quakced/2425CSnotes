'''
    Flat file database - txt, csv, xlsx - one file for your entire db
    Retional Database - multiple tables and/or multiple files
    
    Text File  - you will see the word text file, it means a file of text
    -txt - literally is a file full of text with no set formating
    -csv - comma seperated version - each column of data is seperated by a ,
    -tsv - tab seperated version - \t
    -json - java script object notation - key work to value
    -xlsx - Excel or big bloated version of a csv file
    
    Delineator - the thing that seperates the columns in your file - , \t | \s
    
    CRUD - Acronym for 4 basic functions of database
        C - Create
        R - Read
        U - Update
        D - Delete
'''


###### Reading a text File #########
#with open (FILENAME,mode) as alias
with open("Classroom.txt","w+") as file:
    students=["Mike","Riley","Ezra","Eggvin","Johana"]
    out=""
    for eachNames in students:
        out+=eachNames+"\n"
    
    file.write(out)
    file.close() #If you do not close your file, you could potentially corrupt your file
###### Create A text file ########
students=["Mike","Riley","Ezra","Eggvin","Johana"]
for eachStud in students:
    with open(f"{eachStud}.txt","w+") as file:
        file.write(f"{eachStud}'s Profile\n")
        file.close()

####### Writing to a text file ######
with open("Classroom.txt","w") as file:
    students=["Mike","Riley","Ezra","Eggvin","Johana"]
    id=["01110","00111","10001","01001","00110"]
    out=""
    for i in range(len(id)):
        out+=f"{id[i]},{students[i]}\n"
    
    file.write(out)
    file.close() #If you do not close your file, you could potentially corrupt your file

###### Append to a text file ######
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines() #Other ways to read to, just google it
    print(theWholeFile)
    file.close()

####### Update a text file #######
with open("Classroom.txt","a") as file:
    newStudent = "00000, Bander\n"
    file.write(newStudent)
    file.close()

####### Create a text file ########

###### Delete a text file #######