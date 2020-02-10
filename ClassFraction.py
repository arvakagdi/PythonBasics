'''
Class Fraction
input: 2 fractions
output: add and substraction capabilities using the function

'''

class fraction(object):
    def __init__(self, num,deno):
        self.num = num
        self.deno = deno
    def __str__ (self):
        return str(self.num) + '/' + str(self.deno)
    
    def getnum (self):
        return self.num
    def getdeno (self):
        return self.deno
    
    def __add__(self, other):
        newnum = self.getnum() * other.getdeno() + self.getdeno() + other.getnum()
        newdeno = self.getdeno() + other.getdeno()
        return fraction (newnum,newdeno)   
    def __sub__ (self,other):
        newnum = self.getnum() * other.getdeno() - self.getdeno() + other.getnum()
        newdeno = self.getdeno() + other.getdeno()
        return fraction (newnum,newdeno)   
    
    def convert(self):
        return self.getnum() / self.getdeno()
    
    
onehalf = fraction(1,2)
twothird = fraction (2,3)
    
newfrac = onehalf + twothird
newfrac2 = onehalf - twothird
print(newfrac)
print(newfrac2)

print(newfrac2.convert())
    
    
    