# Class Human
class Human:
    # This is the Property of the class
    def __init__(self, n, o): 
        '''init is special function it is going to initailize 
         properties that particular class after creating the instance
         Self : here is class itself
         '''
        self.name = n
        self.occupation = o
    
    #This is the Method of the class
    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name,"Playes Tennis")
        elif self.occupation == "Actor":
            print(self.name,"Shoots a film")

    #This is the Method of the class
    def speaks(self):
        print(self.name,"Says How are you?")

tom = Human("Tom Cruise","Actor")#This is the Instance of the class Human
tom.do_work()#This is the Object of class to access the methods of the class
tom.speaks()#This is the Object of class to access the methods of the class

maria = Human("Maria Sharapova", "Tennis Player") #This is the Instance of the class Human
maria.speaks() #This is the Object of class to access the methods of the class
maria.do_work()#This is the Object of class to access the methods of the class