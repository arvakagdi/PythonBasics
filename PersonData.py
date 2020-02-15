'''
Class that organized info of people
'''

import datetime


class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]


    def getlastname (self):
        return self.lastname

    def setBirthday(self, month, day, year):
        '''sets self's birthday to birthdate'''
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        '''returns current age in days'''

        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        '''Returns ture if self's name is less than other's name else returns false'''
        if self.lastname == other.lastname:
            return self.name < other.name

        return self.lastname < other.lastname

    def __str__(self):
        """returns self's name"""
        return str(self.name)


class SUPerson(Person):
    IDnext = 0  # ID num to be assigned

    def __init__(self, name):
        Person.__init__(self, name)
        self.IDNo = SUPerson.IDnext
        SUPerson.IDnext += 1

    def getIDNum(self):
        return self.IDNo

    # sorting using ID num
    def __lt__(self, other):
        return self.IDNo < other.IDNo

    def speaks(self, utterance):
        return (self.name + " says: " + utterance)

class Student(SUPerson):
    pass

class UG(Student):
    def __init__ (self, name, classYear):
        SUPerson.__init__(self,name)
        self.year = classYear

    def getclass(self):
        return self.year

    def speak(self, utterance):
        return SUPerson.speaks(self, "Dude, ", utterance)


class Grads(Student):
    pass

class TransferStudent (Student):
    pass


class Professor(SUPerson):
    def __init__(self,name,dept):
        SUPerson.__init__(self,name)
        self.dept = dept

    def speaks (self, utterance):
        new  = ' In course ' + self.dept + ' we say '
        return SUPerson.speaks(self, new + utterance)

    def lecture (self, topic):
        return self.speaks (' it is obvious that ' + topic)

def isstudent(obj):
    return isinstance(obj,Student)


class Grades (object):
    '''A mapping from students to list of grades'''
    def __init__(self):
        '''Creates empty grade book'''
        self.ugstudents = []
        self.grades = {}
        self.isSorted = True

    def addStudent (self,UG):
        """Assumes: student is of type Student
          Add student to the grade book"""
        if UG in self.ugstudents:
            raise ValueError
        self.ugstudents.append(UG)
        self.grades[UG.getIDNum()] = []
        self.isSorted = False

    def addgrade (self, UG, grade):
        try:
            self.grades[UG.getIDNum()].append(grade)
        except KeyError:
            raise ValueError ("Student not in grade book")

    def getGrades(self, UG):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[UG.getIDNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        "Returns list of all the students present in gradebook"
        if not self.isSorted:
            self.ugstudents.sort()
            self.isSorted = True
        return self.students [:]   # returns copy of the list

p1 = SUPerson("Tash Na")
p1.setBirthday(7, 7, 1992)

p2 = SUPerson("Arva Kagdi")
p2.setBirthday(11, 4, 1991)

p3 = SUPerson("Mansoor Kagdi")
p3.setBirthday(9, 19, 1960)

p4 = SUPerson("Taha Kapadia")
p4.setBirthday(1, 21, 2015)

personlist = [p1, p2, p3, p4]

print("Unsorted List:")
for name in personlist:
    print(name)

personlist.sort()
print(" ")
print("Sorted List: ")
for name in personlist:
    print(name)

print(p1.speaks("HELLO There!!!"))


ug1 = UG("Ama", 2019)
ug2 = UG ("Gimmy", 2018)
ug3 = UG ("Alexa", 2020)
grad1 = Grads("Arva Kagdi")

#print(ug1.speaks())
#print(grad1.speaks())

#print(isstudent(ug1))
JimFawcett = Professor("Jim F", "CE")
print(JimFawcett.lecture ("Welcome to CE!!"))

