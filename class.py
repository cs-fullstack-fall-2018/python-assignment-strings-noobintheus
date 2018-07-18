# class Student():
#     def __init__(self, name="", age=0, favoriteSubject=""):
#         self.name = name
#         self.age = age
#         self.favoriteSubject = favoriteSubject
#
#     def changeName(self, changedName):
#         self.name = changedName
#
#     def changeFavoriteSubject(self, newFavoriteSubject):
#         self.favoriteSubject = newFavoriteSubject
#
# def main():
#
#     #First example of a class
#     newStudent = Student("name2", 9, "subject0")
#     print(newStudent.name)
#     newStudent.changeName("Kenn")
#     print(newStudent.name)

    # # An array of objects of the Student Class
    # anArrayOfStudents = []
    #
    # onlyOneStudent = Student("name2", 9, "subject0")
    # anArrayOfStudents.append(onlyOneStudent)
    # print(anArrayOfStudents[0].name)

    # # Create an array
    # shouldTheyKeepGoing = input("Do you want to add another student? Press q to quit")
    # while (shouldTheyKeepGoing != 'q'):
    #
    #     # Creating an object by passing it values
    #     # studentName = input("What is their name? ")
    #     # studentAge = input("What is their age? ")
    #     # studentFavoriteSubject = input("What is their favorite subject? ")
    #     # newStudent = Student(studentName, studentAge, studentFavoriteSubject)
    #
    #     # Creating a blank object, then sending values.
    #     newStudent = Student()
    #     newStudent.name = input("What is their name? ")
    #     newStudent.age = input("What is their age? ")
    #     newStudent.favoriteSubject = input("What is their favorite subject? ")
    #
    #     shouldTheyKeepGoing = input("Do you want to add another student? Press q to quit")
    #     anArrayOfStudents.append(newStudent)
    #
    # #Print the second index of class object's name
    # print(anArrayOfStudents[1].name)
    #
    # # If you want to run information on a student by name
    # for itemInArray in anArrayOfStudents:
    #     print()
    #     if itemInArray.name == "name2":
    #         print("Name2 is", itemInArray.age, " years old.")

# if __name__ == '__main__':
#     main()

# class JobApplication():
#     name = "Temporary Name"
#     dob = "1/1/1900"
#
#     def printName(self):
#         print(self.name)
#
#     def returnTheDOB(self):
#         return "The DOB is: " + self.dob
#
#     def addTextToTheName(self, additonalText):
#         self.name = self.name + additonalText
#
# kennGibbs = JobApplication()
# kennGibbs.printName()
#
# print(kennGibbs.returnTheDOB())

# class JobApplication():
#     name = "Temporary Name"
#     dob = "1/1/1900"
#
#     def printName(self):
#         print(self.name)
#
#     def returnTheDOB(self):
#         return "The DOB is: " + self.dob
#
#     def addTextToTheName(self, additonalText):
#         self.name = self.name + additonalText
#
# kennGibbs = JobApplication()
# kennGibbs.printName()
#
# print(kennGibbs.returnTheDOB())

# class Pet():
#     # dog = Pet("Bob", 5, "Leprechan", "Green", "male", "small")
#     def __init__(self, name="placeholder", age=0, breed="NA", color="purple", gender="", size="shmedium"):
#         self.nameOfPet = name
#         self.ageOfPet = age
#         self.breed = breed
#         self.color = color
#         self.gender = gender
#         self.size = size

# def main():
#     dog = Pet("Bob", 5, "Leprechan", "Green", "male", "small")
#     cat = Pet("Jeff", 2, "bobcat", "black", "girl", "fat")
#
#     thisIsAnArray = []
#     thisIsAnArray.append(dog)
#     thisIsAnArray.append(cat)
#
#     dog = Pet("Midnight", 3, "yorkie", "brown", "dude", "medium")
#     thisIsAnArray.append(dog)
#
#     squirrel = Pet("Jimmy", 20, "Flying Squirrel", "yellow")
#     # print(squirrel.size)
#     # print(thisIsAnArray[0].size)
#
#     spoon = Pet()
#     print(spoon.color)
#
# if __name__ == '__main__':
#     main()

























