class Entry:
         #Constructor
     def __init__(self,account,username,password,category,firstName,lastName):
          self.account = account
          self.username = username
          self.password = password
          self.category = category
          self.firstName = firstName
          self.lastName = lastName
          

     #toString          
     def __str__(self):
          out=f"{self.account},{self.username},{self.password},{self.category},{self.lastName},{self.firstName}\n"
          #for localVariable in list
          # for c in self.categories:
          #      #concat to the out variable
          #      out+=f"\t{c}\n"
          return out
     
     #getters
     def getAccount(self):
        return self.account
        
     def getUsername(self):
        return self.username
     
     def getPassword(self):
        return self.password
     
     def getCategory(self):
        return self.category
    
     def getFirstName(self):
          return self.firstName
     
     def getLastName(self):
          return self.lastName
     
     def getFileName(self):
          out = f"{self.lastName}_{self.firstName}_entries.txt"
          return out
     
     
     #setter
     def addCategory(self,newCategory):
          self.courses.append(newCategory)