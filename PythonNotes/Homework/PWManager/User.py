class User:
     
     #Constructor
     def __init__(self,username,password,first,last):
          self.username = username
          self.password = password
          self.firstName = first
          self.lastName = last
          
     #toString          
     def __str__(self):
          out=f"{self.username},{self.password},{self.lastName},{self.firstName}\n"
          #for localVariable in list
          # for c in self.categories:
          #      #concat to the out variable
          #      out+=f"\t{c}\n"
          return out
     
     #getters
     def getUsername(self):
         return self.username
     
     def getPassword(self):
        return self.password
    
     def getFirstName(self):
          return self.firstName
     
     def getLastName(self):
          return self.lastName
          
     
     #setter
     def addCategory(self,newCategory):
          self.courses.append(newCategory)