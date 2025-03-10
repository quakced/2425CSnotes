import glob  #a module that can obtain multiple files at the same time
import matplotlib.pyplot as plt

#find the names of all of the books
books = glob.glob("OriginalData/*.txt")
# for eachBook in books:
#     print(eachBook)

bookshelf=[]
for eachBook in books:
    name=eachBook[eachBook.index("B"):eachBook.index(".")]
    bookshelf.append(name)
# print(bookshelf)

#remove the blank lines
amountComp=[]
for i in range(7):
    with open(f"OriginalData\OriginalData-{bookshelf[i]}.txt","r",encoding="utf8") as file:
        f = file.readlines()
        file.close()

    out=[]
    # remove the lines with just \n
    for eachLine in f:
        if not eachLine == "\n":
            out.append(eachLine)

    print(len(f))
    print(len(out))
    print(f"Reduced by: {((1-len(out)/len(f))*100):.1f}%")
    amountComp.append((1-len(out)/len(f))*100)
    
    #write out to a clean data to a new folder in utf8 formatting
    cleanFile = open(f"CleanData/Clean-{bookshelf[i]}.txt","w+",encoding="utf8")
    for eachLine in out:
        cleanFile.write(eachLine)
    cleanFile.close()
    

for i in range(7):
    print(f"{bookshelf[i]} reduced by {amountComp[i]:.1f}")

#plot and graph comparrison of compression
#plot a pie chart of the amountComp
#plt.pie(data,labels for the data,colors,explode, size)
# plt.pie(amountComp,labels=bookshelf)

plt.bar(range(1,8),amountComp)
plt.title("Amount of Lines Reduced")
plt.xlabel("Book #")
plt.ylabel("% reduced")
plt.ylim(31,34)
plt.show()
#find some people
# Go find how many times Harry is mentioned
    # in all 7 books. And tell me which books he was mentioned
    # the most and least.  Use a graph or chart to support your
    # answer
#find some people
wordsToFind={  #Python Dictionary or JSON
    #"key":value
    "Harry":0,
    "Ron":0,
    "Ronald":0,
    "Hermione":0,
    "Albus":0,
    "Hagrid":0,
    "wizard":0,
    "witch":0,
    "Wizard":0,
    "Witch":0,
    "Snake":0,
    "snake":0,
    "Voldemort":0,
    "Tom Marvolo Riddle":0,
    "You-Know-Who":0,
    "The Dark Lord":0,
    "He-Who-Must-Not-Be-Named":0,
}
for i in range(7):
    file = open(f"CleanData/Clean-{bookshelf[i]}.txt","r",encoding="utf8")
    for eachLine in file:
        for eachName in wordsToFind:
            if not "Rowling" in eachLine:   #skip page title at bottom
                wordsInALine = eachLine.split(" ")
                for eachWord in wordsInALine:
                    if eachName in eachWord:
                        wordsToFind[eachName]+=1
    file.close()
    for name, instances in wordsToFind.items():
        print(f"Total instances of {name}:{instances}")