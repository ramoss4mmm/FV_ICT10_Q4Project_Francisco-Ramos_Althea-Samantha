from pyscript import display,document
import numpy as np
# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

attendance = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0
    } # stores the attendance for the week

def show_graph(e):
    document.getElementById('output').innerHTML = "" # makes sure there is only one output
    day = document.getElementById("day").value # gets selected day
    absence_input = document.getElementById("absences").value # gets the number of absences

    if day == "": # checks if they selected a day
        document.getElementById("output").innerText = "Please select a valid day"
        return

    if absence_input == "": # checks if input is empty
        document.getElementById("output").innerText = "Please enter absences"
        return
    
    absences = int(absence_input) # converts the string to an integer
    attendance[day] = absences # saves the values for the day
    days = list(attendance.keys()) # gets the list of days
    values = list(attendance.values()) # gets the list of absences 
    y = np.array(values) # converts values to numpy 
    plt.clf() # makes only one graph instead of multiple overlapping
    plt.plot(days, y, marker='o') # plots the graph 
    plt.xlabel("Days") # label for the x axis
    plt.ylabel("Number of Absences") # label for the y axis
    plt.title("Weekly Attendance (Absences)") # title for the graph
    plt.grid() # adds a grid
    plt.show() # shows graph in browser