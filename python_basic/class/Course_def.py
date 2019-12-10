#class
#define Course class
class Course:
    # construtor
    def __init__(self, name, hrs):
        self.name = name
        self.hrs = hrs
    # method
    def display_course(self):
        print('name =',self.name)
        print('hours =',self.hrs)
        
    def show_course(self):
        return self.name