class StringVar:
    string = ""

    def __init__(self, string):
        self.string = string
        print(self.string)

    def setString(self, newString):
        self.string = newString

    def getString(self):
        return  self.string

s1 = StringVar("Привет")
s1.setString("Пока")
print(s1.getString())



