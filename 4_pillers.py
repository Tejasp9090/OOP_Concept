"""
OOP pillers
1)Inheritance 
2)Encapsulation
3)Polymorphsim
4)Abstraction
"""
"""class Father:
    atm_pin=1234

    def car(self):
        print("Father Car Is BMW")

    def bike(self):
        print("Fathers Bike Is Bullet")
  



class Child(Father):
    atm_pin=5678

    def car(self):
        print("Childs car  Is Audi")
        super().car()
        new_pin=super().atm_pin
        print('####',new_pin)

    def bike(self):
        print("Childs Bike Is KTM")
        super().bike()
  
    

c1=Child()
print(c1.atm_pin)
c1.car()
c1.bike()
"""


"""class CentralGovt:
    def tax(self):
        print('Central govt tax is 10%')

class StateGovt(CentralGovt):
    
    #def tax(self):
    #    print('StateGovt govt tax is 5%')
    pass

class LocalGovt(CentralGovt):
    #def tax(self):
    #    print('StateGovt govt tax is 5%')
    
    pass

l1=LocalGovt()
l1.tax()"""

class Test:
    a=100
    _b=200
    __c=300

t1=Test()
print(t1.a)
print(t1._b)
print(t1._Test__c)
