import random
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

class Student(Person):
	Count = 0
	def __init__(self,name,age,score):
		super().__init__(name,age)
		self.score = score
		Student.Count+=1
	def displayCount(self):
		print ("Total Employee %d" % Student.Count)
	def displayStudent(self):
		print ("Name : ", self.name,  ",age: ", self.age, ",score: ",self.score)				

t = random.randrange(0,10)				
s1 = Student("Anh",21,t)
t2 = random.randrange(0,10)
s2 = Student("Bao",22,t2)

listStudent = []
listStudent.append(s1)
listStudent.append(s2)


for st in listStudent:
	st.displayStudent()
print("Total of student is : ",Student.Count)


				
						