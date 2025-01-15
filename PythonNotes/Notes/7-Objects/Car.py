'''
    Classes... It is like defining your own data type
        Strings have attributes and methods
            string.lower  string.upper  string.index  string.title
        Buttons in MIT
            btn.onclick  btn.onhold
        ImageSprites in MIT
            sprite.drag  sprite.collision  sprite.moveto
            
        Variable that you define the attributes and methods for 
            attribute = adjective
            method = verb
            
        grandpri.go(100)
        eliCar.revEngine()
        print(theBlueBerry.horsepower)
        
        Good rule of thumb - keep all Class in seperate files*
            
'''
#define the class
class Car:

    #define the constructor - what it takes to build an object
    #def initializationFunction(self,attributesOfThatObject)
    def _init_(self, make, model, year, color):
        #these are the attributes of each car
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        #self.object's attribute = passedInAttribute
    
    #define getters and setters
    
    #define additional f(x)
    
    #define toString / description
    def description(self):
        return f'''
    make:  {self.make}
    model: {self.model}
            '''