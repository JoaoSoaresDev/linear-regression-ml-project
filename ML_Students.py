import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean

def convertList(old_list):
    map_list = map(int, old_list)
    result_list = list(map_list)
    return (result_list)


def removeFirstElement(list):
    del list[0]
    
def linear_regression(x, y):
    N = len(x)
    x_mean = mean(x)
    y_mean = mean(y)
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    B1_num = sum(( x_arr - x_mean) * (y_arr - y_mean))
    B1_den = sum((x_arr - x_mean) **2)
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    return (B0, B1)

def result(B0, B1, x):
    return (B0 + (B1 * float(x)))

def plot_regression_line(x, y, b0, b1):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b0 + b1 * np.array(x)
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()



student_list = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu",
                "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "failures", 
                "schoolsupm", "famsup", "paid", "activities", "nursery", "higher", "internet", 
                "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", 
                "absences", "G1", "G2", "G3"]

file_reader = pd.read_csv("students-mat.csv", names=student_list)

study_list = file_reader.studytime.tolist()
removeFirstElement(study_list)
study_time = convertList(study_list)

grade1_list = file_reader.G1.tolist()
removeFirstElement(grade1_list)
grade1 = convertList(grade1_list)

grade2_list = file_reader.G2.tolist()
removeFirstElement(grade2_list)
grade2 = convertList(grade2_list)

grade3_list = file_reader.G3.tolist()
removeFirstElement(grade3_list)
grade3 = convertList(grade3_list)

B0, B1 = linear_regression(study_time, grade3)

val = 1

plot_regression_line(study_time, grade3, B0, B1)

while val != 0:
    val = input("Enter a study time: ")
    res = result(B0, B1, val)

    print("Your grade for ", val, "hours of study will be: ", res)

