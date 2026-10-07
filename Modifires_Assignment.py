# Assignment : Take a class Sample, add 3methods m1(),_m2(),__m3()
# And Try To access Them.

class Sample: 

    def m1(self):
        print("This Is Public Methods ")

    def _m2(self):
        print("This Is Private Methods ")

    def __m3(self):
        print("This Is Procted Methods ")

s1=Sample()
s1.m1()
s1._m2()
print(s1._Sample__m3())