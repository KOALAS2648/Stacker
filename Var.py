class Variable:
    def __init__(self, typE, value):
        self.type = typE
        self.value = value
        self.turnToType()
    def val(self):
        return self.value
    def turnToType(self):
        match self.type.upper():
            case "INTEGER" | "INT":
                try:
                    self.value = int(self.value)
                except ValueError:
                    print(f"cannot convert {self.value} to int")
    def type(self): 
        return self.type