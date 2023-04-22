import math
import numpy as np
import os
from tkinter import *

def Read_data(keyword):
    corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if keyword == "nodes":
        with open('Node_data.txt','r') as data_file:
            coordinate = []
            data = data_file.readlines()
            data.remove(data[0])
            data.remove(data[0])
            for i in data:
                node_number = int(i.split(' '*22)[0].split('node')[1])
                x_coordinate = float(i.split(' '*22)[1])
                y_coordinate = float(i.split(' '*22)[2])
                coordinate.append((x_coordinate, y_coordinate))
        return coordinate
    elif keyword == "elements":
        with open('Element_data.txt','r') as data_file:
            element = []
            data = data_file.readlines()
            data.remove(data[0])
            data.remove(data[0])
            for i in data:
                node_number = int(i.split(' '*19)[0].split('element')[1])
                begin_node = int(i.split(' '*19)[1]) - 1
                end_node = int(i.split(' '*19)[2]) - 1
                element.append((begin_node, end_node))
        return element
    elif keyword == "loads":
        with open('Load_data.txt','r') as data_file:
            load = []
            data = data_file.readlines()
            data.remove(data[0])
            data.remove(data[0])
            for i in data:
                node_number = int(i.split(' '*16)[0].split('node')[1]) - 1
                loaded_node = corespond_letter[node_number]
                Force_X = float(i.split(' '*16)[1])
                Force_Y = float(i.split(' '*16)[2])
                load.append((loaded_node, Force_X, Force_Y))
        return load
    elif keyword == "supports":
        with open('support_data.txt','r') as data_file:
            support = []
            data = data_file.readlines()
            data.remove(data[0])
            data.remove(data[0])
            for i in data:
                node_number = int(i.split(' '*19)[0].split('node')[1]) - 1
                support_type = str(i.split(' '*22)[1][0])
                support.append((node_number, support_type))
        return support
    elif keyword == "properties":
        with open('Properties_data.txt','r') as data_file:
            data = data_file.readlines()
            Unit_sys = (data[2].split(':')[1]).replace(' ','')
            Area = float((data[3].split(':')[1]).replace(' ',''))
            Young_modulus = (data[4].split(':')[1]).replace(' ','')
            Young_data = Young_modulus.split('e')
            Young_modulus = float(Young_data[0]) * (10**int(Young_data[1]))
        return (Area, Young_modulus)

def compability_indexing(index_couple, index_list):
    first_index_set = index_list[index_couple[0]]
    second_index_set = index_list[index_couple[1]]
    index_set = []
    for i in first_index_set:
        index_set.append(i)
    for i in second_index_set:
        index_set.append(i)
    return index_set

Node_data = Read_data("nodes")
Properties_data = Read_data("properties")
Element_data = Read_data("elements")
Support_data = Read_data("supports")
Load_data = Read_data("loads")

element_lenght = []
element_sines_and_cosines = []
for i in range(len(Element_data)):
    begin_node = Element_data[i][0]
    end_node = Element_data[i][1]
    lenght = math.sqrt(((Node_data[end_node][0] - Node_data[begin_node][0])**2) + ((Node_data[end_node][1] - Node_data[begin_node][1])**2))
    element_lenght.append(lenght)
    element_cosine = round((Node_data[end_node][0] - Node_data[begin_node][0])/lenght, 6)
    element_sine = round((Node_data[end_node][1] - Node_data[begin_node][1])/lenght, 6)
    element_sines_and_cosines.append((element_sine, element_cosine))

Global_k = []
Global_index = []
temp_index = []

for i in range(len(Element_data)*2):
    temp_index.append(i)
condition = len(temp_index)
while condition >= 4:
    condition = len(temp_index)
    Global_index.append((temp_index[0], temp_index[1]))
    temp_index.remove(temp_index[0])
    temp_index.remove(temp_index[0])
    
for i in element_lenght:
    A = Properties_data[0]
    E = Properties_data[1]
    L = i
    
    index = element_lenght.index(i)
    c = element_sines_and_cosines[index][1]
    s = element_sines_and_cosines[index][0]
    K_sub = np.array([[c**2, c*s, -c**2, -c*s],
                      [c*s, s**2, -c*s, -s**2],
                      [-c**2, -c*s, c**2, c*s],
                      [-c*s, -s**2, c*s, s**2]])
    Global_k.append(K_sub)

Total_stiffness_matrix = np.ones((len(Element_data), len(Element_data)))
Element_index_set_list = []
for i in range(len(Element_data)):
    Element_index_set_list.append(compability_indexing(Element_data[i], Global_index))