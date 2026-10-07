"""class Test:
    a=100


    def item(self):
        print('Item method')

    def m1(self):
        b=200
        print(self.a,b)
        self.item()

t1=Test()
t1.m1()"""

'''name = 'AXIS Bank'
IFSC = 'AXIS123456'
class Bank:
    # class level/static variable
    name = 'SBI'
    IFSC = 'sbi123123'
    
    def online(self):
        # # local variables
        name = 'ABC Bank'
        # IFSC = 'sbi123123'
        print('Bank name:',self.name)
        print('Bank :', name)
        print('IFSC is:',self.IFSC)
b1 = Bank()
b1.online()'''

"""class Bank:
    # class level/static variable
    name = 'SBI'
    IFSC = 'sbi123123'
    name1 = 'hdfc'
    
    def online(self):
        # # local variables
        # name = 'SBI'
        # IFSC = 'sbi123123'
        print('Bank name:',self.name)
        print('IFSC is:',self.IFSC)
        
        def on(): # it is working like a normal function
            print('bank is:',self.name1)
            # self is active as this calling is inside a method
        on()


b1 = Bank()
b1.online()"""

def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # 4 * factorial(3)*factorial(2)*factorial(1)
result = factorial(5)
print(result)