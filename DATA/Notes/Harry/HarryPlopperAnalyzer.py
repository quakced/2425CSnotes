import glob #a module that can obtain multiple files at the same time
import matplotlib.pyplot as plt
#find the names of all of the books
# with open("OriginalData/Book 1 - The Philosopher's Stone.txt","r", encoding="utf8") as file:
 #   file=file.readlines()
  #  print(file)
books = glob.glob("OriginalData/*.txt")
for eachBook in books:
    print(eachBook)

bookshelf=[]
for eachBook in books:
    name=eachBook[eachBook.index("B"):eachBook.index(".")]
    bookshelf.append(name)
print(bookshelf)
#remove the blank lines
amountComp=[]
for i in range(7):
    with open(f"OriginalData/{bookshelf[0]}.txt","r", encoding="utf8") as file:
        f = file.readlines()
        print(file)
        file.close()
    
    out=[]
#remove the lines with just \n

    for eachLine in f:
        if not eachLine == "\n":
            out.append(eachLine)
            
        print(len(out))
        print(len(f))
        print(f"Reduced by: {(1-len(out)/len(f))*100:.1f}%")
        amountComp.append((1-len(out)/len(f))*100)
    #write out to a clean data to a new folder in utf8 formatting
    cleanFile=open(f"CleanData/{bookshelf[i]}.txt","w+",encoding="utf8")
    for eachLine in out:
        cleanFile.write(eachLine)
    cleanFile.close()

for i in range(7):
    print(f"{bookshelf[i]} reduced by {amountComp[i]:.1f}%")
    
#reduce all 7 books and save the amount of reduction into a list

#plot and graph comparrison of compression
plt.bar(range(1,8),amountComp)
plt.ylim(31,34)
plt.ylabel("% reduced")
plt.xlabel("Book #")
plt.title("Amount of Lines Reuduced")
plt.show()
#find some people