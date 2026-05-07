from pyscript import display,document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return(f"Hi! My name is {self.name}. I am from section {self.section}, and my favorite subject is {self.favorite_subject}.")

classmates = [ 
    Classmate("Mauri", "Ruby", "Math"), 
    Classmate("Yaniszolt", "Ruby", "Social Studies"), 
    Classmate("Queeny", "Ruby", "English"), 
    Classmate("Samantha", "Ruby", "Math"), 
    Classmate("Meyer", "Ruby", "PE") 
    ]

def add_classmate(e): # for adding a classmate
    document.getElementById("output").innerHTML = "" 
    name = document.getElementById("name").value 
    section = document.getElementById("section").value 
    subject = document.getElementById("favorite_subject").value 

    if name == "" or section == "" or subject == "": # says to fill in the fields if it is incomplete
        display("Please fill in all fields.", target="output") 
        return

    classmates.append(Classmate(name, section, subject)) # adds new classmate 

    for c in classmates: # displays the classmate list using loops
        display(c.introduce(), target="output") 

def show_list(e): # for showing the classmate list
    document.getElementById("output").innerHTML = "" 
    name = document.getElementById("name").value 
    section = document.getElementById("section").value 
    subject = document.getElementById("favorite_subject").value 

    for c in classmates: # displays the classmate list using loops
        display(c.introduce(), target="output")

    if name == "" or section == "" or subject == "": # says to fill in the fields if it is incomplete
        display("Please fill in all fields.", target="output") 
        return
    