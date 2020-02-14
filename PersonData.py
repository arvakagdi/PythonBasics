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


class SUStudents(Person):
    IDnext = 0  # ID num to be assigned

    def __init__(self, name):
        Person.__init__(self, name)
        self.IDNo = SUStudents.IDnext
        SUStudents.IDnext += 1

    def getIDNum(self):
        return self.IDNo

    # sorting using ID num
    def __lt__(self, other):
        return self.IDNo < other.IDNo

    def speaks(self, utterance):
        return (self.getlastname() + "says: " + utterance)


p1 = SUStudents("Tash Na")
p1.setBirthday(7, 7, 1992)

p2 = SUStudents("Arva Kagdi")
p2.setBirthday(11, 4, 1991)

p3 = SUStudents("Mansoor Kagdi")
p3.setBirthday(9, 19, 1960)

p4 = SUStudents("Taha Kapadia")
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