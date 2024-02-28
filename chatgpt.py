class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hey", self.name , "your avg mark is : ",sum/2)


s1 = students("Saikat",[79,69])
s1.get_avg()