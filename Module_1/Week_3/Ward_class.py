from abc import ABC, abstractmethod


class People(ABC):
    def __init__(self, name : str, yob : int):
        self._name = name
        self._yob = yob
    
    def get_yob(self):
        return self._yob


    @abstractmethod
    def describe(self):
        pass

class Student(People):
    def __init__(self, name : str, yob : int, grade : str):
        super().__init__(name, yob)
        self.__grade = grade
    def describe(self):
        print (f"Name student: {self._name} - Year of birth: {self._yob} - Grade: {self.__grade}")

class Teacher(People):
    def __init__(self, name : str, yob : int, subject : str):
        super().__init__(name, yob)
        self.__subject = subject 

    def describe(self):
        print (f"Name teacher: {self._name} - Year of birth: {self._yob} - Subject: {self.__subject}")

class Doctor(People):
    def __init__(self, name : str,  yob : int, specialist : str):
        super().__init__(name, yob)
        self.__specialist = specialist
    
    def describe(self):
        print (f"Name doctor: {self._name} - Year of birth: {self._yob} - Specialist: {self.__specialist}")

class Ward():
    def __init__(self, name : str):
        self.__name = name
        self.__dict = []
    
    def add_person(self, data):
       self.__dict.append(data)
    
    def describe(self):
        print (f"Ward name: {self.__name}")
        for data in self.__dict:
            data.describe()
    
    def count_doctor(self):
        count = 0
        for data in self.__dict: 
            if isinstance(data, Doctor):
                count += 1
        return count

    def sort_by_age(self):
        self.__dict = sorted(self.__dict, key = lambda x : x.get_yob())
    
    def compute_average(self):
        total = 0
        count = 0
        for data in self.__dict:
            if isinstance(data, Teacher):
                total += data.get_yob()
                count += 1
        print (total / count)
        
    

student1 = Student (name="studentA", yob=2010 , grade="7")
student1.describe()    

teacher1 = Teacher (name="teacherA", yob=1969 , subject="Math")
teacher1.describe ()

doctor1 = Doctor (name="doctorA", yob=1945 , specialist ="Endocrinologists")
doctor1.describe ()

teacher2 = Teacher (name="teacherB", yob=1995 , subject="History")
doctor2 = Doctor (name="doctorB", yob=1975 , specialist="Cardiologists")

ward1 = Ward (name="Ward1")
ward1.add_person ( student1 )
ward1.add_person ( teacher1 )
ward1.add_person ( teacher2 )
ward1.add_person ( doctor1 )
ward1.add_person ( doctor2 )
ward1.describe ()
print (f"\nNumber of doctors : {ward1.count_doctor()}")

ward1.sort_by_age()
ward1.describe ()

ward1.compute_average()