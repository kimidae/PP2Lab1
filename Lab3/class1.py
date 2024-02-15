class String2:
    def init(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Your input: ")
    
    def printString(self):
        print(self.string.upper())

processor = String2()
processor.getString()
processor.printString()