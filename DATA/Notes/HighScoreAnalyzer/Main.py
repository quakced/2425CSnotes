with open("hightscore.csv","r") as file:
    theWholeFile=file.readlines()
file=[]
for eachLine in theWholeFile:
    file.append(eachLine.rstrip().split(","))
names=[]
scores=[]

for i in range(len(file)):
    eachLine=file[i]
    try:
        names.append(file[0])
        scores.append(int(file[i][1]))
    except:
        print(f"bad data: {eachLine}")
    
print(scores)

print(f'''
      max: {max(scores)}
      min:   {min(scores)}
      range:  {max(scores)- min(scores)}
      mean:   {sum(scores)/ len(scores)}
      median: {[int(len(scores)/2)]}
      mode 
      std
      ''')