import random

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    '''Getters'''       
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    
    '''Setters'''
    def setAge(self,newage):
        self.age = newage
    def setName(self,newname = ""):
        self.name = newname
        
    def __str__(self):
        return "Animal: " + str(self.name) + ":" + str(self.age)
    
    
    
class Cat(Animal):
    '''Subclass Cat'''
    def speaks(self):
        print("meowww...")
    def __str__(self):
        return("Cat: " + str(self.name) + ":" + str(self.age))
    
    
class Rabbit(Animal):
    tag = 1
    
    def __init__ (self, age, ParentM = None, ParentD = None):
        Animal.__init__(self,age)
        self.ParentM = ParentM
        self.ParentD = ParentD
        self.rID = Rabbit.tag
        Rabbit.tag += 1
        
    def get_rID(self):
        return str(self.rID).zfill(3)
    
    def getParentM (self):
        return self.ParentM
    def getParentD (self):
        return self.ParentD
    
    def __add__ (self,other):
        #returning obj of same type as the class
        return(Rabbit(0,self,other))
    def __eq__(self,other):
        #comparing if parents are same
        parent_same = self.ParentD == other.ParentD and self.ParentM == other.ParentM
        parent_opp =  self.ParentD == other.ParentM and self.ParentM == other.ParentD    
        return parent_same or parent_opp
    
    def speaks(self):
        print("meepp...")
    def __str__(self):
        return("Rabbit: " + str(self.name) + ":" + str(self.age))
    
class Person (Animal):
    def __init__(self, name,age):
        Animal.__init__(self,age)
        Animal.setName(self,name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello!!")
    
    def ageDiff(self,other):
        diff = self.getAge() - other.getAge()
        
        if self.age > other.age:
            print(self.name, "is", diff , "years older") 
        elif self.age < other.age:
            print(self.name, "is", diff , "years younger")
        else:
            print("Age of both", self.name,"and", other.name, "is same")
    def __str__(self):
        return "Person: " + str(self.name) + ":" + str(self.age) 


class Student(Person):
        def __init__(self, name, age, major = None):
            Person.__init__(self,name,age)
            self.major = major
        def changeMajor(self,newmajor):
            self.major = newmajor
            
        def speaks(self):
            r = random.random()

            if r<0.25:
                print("I have homework to finish!")
            elif 0.25<=r<0.5:
                print("I am sleeping bye!!")
            elif 0.5 <= r < 0.75:
                print("I should eat")
            else:
                print("I am watching TV")
        def __str__(self):
            return "Student: " + str(self.name) + ":" + str (self.age) + ":" + str(self.major)
        