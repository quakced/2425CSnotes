
# set the levels of scoring
bronzeScore = 15
silverScore = 20
goldScore = 25

# return names in the leaderboard file
def getNames(fileName):
    leaderboardFile = open(fileName, "r")  # be sure you have created this

    # use a for loop to iterate through the content of the file, one line at a time
    # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
    names = []
    for line in leaderboardFile:
        leaderName = ""
        index = 0

        # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while(line[index]!=","):
            character=line[index]
            leaderName+=character
            index+=1
        # TODO 2: add the player name to the names list
        names.append(leaderName)

    leaderboardFile.close()

    #  TODO 6: return the names list in place of the empty list
    return names


# return scores from the leaderboard file
def getScores(fileName):
    leaderboardFile = open(fileName, "r")  # be sure you have created this

    scores = []
    for line in leaderboardFile:
        leaderScore = ""
        index = 0

        # TODO 3: use a while loop to index beyond the comma, skipping the player's name
        while(line[index]!=","):
            index+=1
        # TODO 4: use a while loop to get the score
        index+=1
        personScore=""
        while(line[index].isnumeric()):
            character=line[index]
            personScore+=character
            index+=1
            
        # TODO 5: add the player score to the scores list
        scores.append(personScore)
    leaderboardFile.close()

    # TODO 7: return the scores in place of the empty list
    return scores


# update leaderboard by inserting the current player and score to the list at the correct position
def updateLeaderboard(fileName, leaderNames, leaderScores, playerName, playerScore):
    whereToInsert=0
    # TODO 8: loop through all the scores in the existing leaderboard list
    for eachScore in range(len(leaderScores)):
        # TODO 9: check if this is the position to insert new score at
        if (playerScore>eachScore):
            
            break
        else:
            whereToInsert += 1


    # TODO 10: insert new player and score
    leaderNames.insert(whereToInsert,playerName)
    leaderScores.insert(whereToInsert,playerScore)
    # TODO 11: keep both lists at 5 elements only (top 5 players)
    if len(leaderNames)>5:
        leaderNames.pop()
        leaderScores.pop()
    # TODO 12: store the latest leaderboard back in the file
    print(leaderNames,leaderScores)
    
    leaderboardFile = open(fileName, "w")  # this mode opens the file and erases its contents for a fresh start

    # TODO 13 loop through all the leaderboard elements and write them to the the file
    for index in range(5):
        leaderboardFile.write(leaderNames[index].upper() + "," + str(leaderScores[index]) + "\n")

    leaderboardFile.close()
    


# draw leaderboard and display a message to player
def drawLeaderboard(areYouAHighScorer,highScorer, leaderNames, leaderScores, turtleObject, playerScore):

    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    fontSetup = ("Arial", 20, "normal")
    turtleObject.clear()
    turtleObject.penup()
    turtleObject.goto(-160, 100)
    turtleObject.hideturtle()
    turtleObject.down()

    # TODO 14: loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'


    # move turtle to a new line
    turtleObject.penup()
    turtleObject.goto(-160, int(turtleObject.ycor()) - 50)
    turtleObject.pendown()

    # TODO 15: display message about player making/not making leaderboard

    turtleObject.write("Congratulations!\nYou made the leaderboard!", font=fontSetup)
    turtleObject.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=fontSetup)
    

    # move turtle to a new line
    turtleObject.penup()
    turtleObject.goto(-160, int(turtleObject.ycor()) - 50)
    turtleObject.pendown()

    # TODO 16: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal

    turtleObject.write("You earned a gold medal!", font=fontSetup)
    turtleObject.write("You earned a silver medal!", font=fontSetup)
    turtleObject.write("You earned a bronze medal!", font=fontSetup)
     
    print(getNames("db.txt"))
    print(getScores("db.txt"))
    updateLeaderboard("db.txt",getNames("db.txt"),getScores("db.txt"),"Riley",7)