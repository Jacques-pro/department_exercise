
#school will be the parent class 
# department child class of parent class( school)
#course child class of parent class
#How can I receive the input and consider it regardless it's uppercase,lowercase, or mixed letter?


class school:
    def __init__(self,student,coding):

        self.student=student
        self.coding=["HTML$CSS","python","JavaScript"]

    def setdepartment(self,lists):

        if self.coding==lists:
            return "Enroll"

        if self.coding!=lists:
            del self.coding

sc1= school ("Jc",["HTML$CSS","python","JavaScript"])

#print (sc1.setdepartment(["HTML$CSS","python","JavaScript"]))


class department(school):
    def __init__(self,student,coding):
        super().__init__(student,coding)
        

    def takecourses(self, course):
        self.coding=["HTML$CSS","python","JavaScript"]
        if course=="HTML&CSS":
            return f"{self.coding[0]} is the first course to take"
        elif course=="JavaScript":
            return f"{self.coding[1]} is the third course to take"

        elif course=="Python":
            return f"{self.coding[2]}is the second course to take"
        
departs= department("James",["HTML$CSS","python","JavaScript"])

#print(departs.takecourses("HTML&CSS"))

class course(department):
    def __init__(slef,student,coding):
        super().__init__(student,coding)

        def pre_requisite(self):

          self.coding=["HTML$CSS","python","JavaScript"]
          pre_requisite=["English","basic computer skills","HTML&CSS"]

          input1=input("Enter your pre-requesite here:")


          for i in input1:
                if i=="English":
                    return self.coding[0]
                elif i=="basic computer skills":
                    return self.coding[1]
                elif i=="HTML&CSS":
                    return self.coding[2]
                else:
                    return "you're not qualified"

courses= course("James",["English","basic computer skills","HTML&CSS"])

print(courses.pre_requisite())
                

        
     
