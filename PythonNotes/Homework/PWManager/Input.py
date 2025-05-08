class Input:
    
    @staticmethod #decorator
    def getCorrectInput(listOfAnswers,question):
        userInput=""
        while userInput not in listOfAnswers:
            userInput = input(question)
        return userInput