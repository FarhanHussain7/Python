class RailwayForm:# class is define the blue print or templates
    formtype = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")# they are objects (names of person,train,ticket price)
        print(f"train is {self.train}")

harrysApplication = RailwayForm()# application in oops
harrysApplication.name = "harry"
harrysApplication.train = "rajdhani express"
harrysApplication.printData()

