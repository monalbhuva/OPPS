class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000  
        self.designation = "SDE"

    def travel(self,destination):
        print(f"Employee now traveling to {destination}")

# create a object/instance of the class
sam = employee()

print(sam.id)
sam.travel("dubai")
