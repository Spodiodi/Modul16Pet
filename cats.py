class Cats:
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age

    def getCatName(self):
        return self.name
    def getCatGender(self):
        return self.gender
    def getCatAge(self):
        return self.age

    def getCat(self):
        catDef = self.getCatName() + " " + self.getCatGender() + " " + str(self.getCatAge())
        return catDef