class Employee:
    def __init__(self, salary):
        self._salary = salary 

    @property
    def salary(self):
        return self._salary
    
    @salary.setter 
    def salary(self, value):
        if(value<0):
            print("Hey please dont set a negative value for salary")
        else:
            self._salary = value

    

e = Employee(3)
e.salary = 67
print(e.salary)