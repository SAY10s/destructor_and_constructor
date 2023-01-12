class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def about(self, greeting="Hiii!"):
        print(f"{greeting}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\n")

kate = Human("Kate", "Bundy", 27)
niko = Human("Nikodem", "Majzner", 17)

people=[]


kate.about("Hello uwu")
niko.about("Yooo!")
