'''
Creating a collection of Integers
A particular integer appears only once in a set

List - data representations

Interface:
insert()
member()
remove()
intersect()
len()
'''

class intSet (object):
    ''' intSet  is a set of int. Value is represented by list of ints, self.vals. Each int can occur only once'''

    def __init__ (self):
        ''' Creating an empty list of ints'''
        self.vals = []
        
    def insert(self,num):
        '''Assumes e as int and inserts it into self'''
        if  not num in self.vals:
            self.vals.append(num)
    
    def member(self,num):
        '''Returns True if num in list else false'''
        return num in self.vals
    
    def delete(self, num):
        '''Deletes num from list if present else raises Valuerror'''
        try:
            self.vals.remove(num)
        except:
            raise ValueError(str(num) + 'Not in the list')
    
    def __str__ (self):
        '''Returns string representation'''
        self.vals.sort()
        result = ''
        
        for num in self.vals:
            result = result + str(num) + ','
            
        return '{' + result[:-1] + '}'
    
    def intersect (self,other):
        '''finds common ints from both lists'''
        newset = intSet()
        for i in other.vals:
            if i in self.vals:
                newset.vals.append(i)  
           
        newset.vals.sort()
        
        newstr = ""
        for i in newset.vals:
            newstr += str(i) + ','
                
        return '{' + newstr[:-1] + '}'
        
    def __len__ (self):
        '''Length of the list'''
        return len(self.vals)
        
    
    
newstr = intSet()
    
newstr.insert(1)
newstr.insert(2)
print(newstr)
    
newstr.insert(5)
newstr.insert(10)
print(newstr)    
newstr.delete(1)
print(newstr)
print("5: " ,newstr.member(5))                     
print("15: " ,newstr.member(15))           

s1 = intSet()
s1.insert(11)
s1.insert(12)

print(s1)
snew = s1.intersect(newstr)
print(snew)

          
