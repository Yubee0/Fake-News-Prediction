"""class student:
    collage="GLOBSL COLLAGE"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new students")

    def welcome(self):
        print("welcome",self.name)
s1=student("kuldip",99)
print("welcome to global collage")
print(s1.name,s1.marks)"""




#create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("welcoming new student")

    def average(self):
        print("average",self.average)
s1=student("kuldip",98)
s2=student("sumit",88)
s3=student("sumitra",88)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)
average=s1.marks+s2.marks+s3.marks/3
print("the average of new class is :",average)"""

#arko tarika 
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
            print("hello",self.name,"your avg score is:",sum/3)


s1=student("kuldip",[98,99,100])
s1.avg()"""


#Create Accunt class with 2 attributes - balance &acc no. Create methods for debit,credit &printing the balance
"""
class account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
# debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"has been debited from your acc")
        print("the total balnce of account is :",self.balance)
#credit method
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"has been credited to your acc")
#printing the remaining balance
    def balance(self):
        return self.balance       
        


a1=account(82338,62828181)
a1.debit(122222)
a1.credit(39388393)
a1.credit(26276276262)
a1.debit(722872)
"""