class Cars:
    def __init__(self, modelname, color, year, capacity):
        self.model = modelname
        self.color = color
        self.year = year
        self.capacity = capacity

    def show(self):
        print(self.model, self.color, self.year, self.capacity)


# create an object
myobj = Cars("Toyota", "white", 2016, "1500cc")
myobj.show()
