class Animal(object):
    def __init__(self, startname, age):
        self.name = startname #attribute1
        self.age = age #attribut2
    def description(self): #Method1
        print("This is" + self.name)
        print("She/it is  " + str(self.age))
