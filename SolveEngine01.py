import math
import numpy as np
import os
from numpy.linalg import inv, det

def Read_data(keyword):
    
    if keyword == "nodes":
        with open('Node_data.txt','r') as data_file:
            coordinate = []
            data = data_file.readlines()
            data.remove(data[0])
            data.remove(data[0])
            for i in data:
                # node_number = int(i.split(' '*22)[0].split('node')[1])
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
                # loaded_node = corespond_letter[node_number]
                Force_X = float(i.split(' '*16)[1])
                Force_Y = float(i.split(' '*16)[2])
                load.append((node_number, Force_X, Force_Y))
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


def arrange_value_to_global_matrix(sub_matrix, position_index_set, size):
    global_matrix = np.zeros(size)
    for i in range(sub_matrix.shape[0]):
        for j in range(sub_matrix.shape[1]):
            global_matrix[position_index_set[i], position_index_set[j]] = sub_matrix[i,j]
            # print("#"*20)
            # print([position_index_set[i], position_index_set[j]])
            # print(sub_matrix[i,j])
            # print("#"*20)
    return(global_matrix)


def SolveEngine01():
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
        K_sub = (A*E/L) * np.array([[c**2, c*s, -c**2, -c*s],
                          [c*s, s**2, -c*s, -s**2],
                          [-c**2, -c*s, c**2, c*s],
                          [-c*s, -s**2, c*s, s**2]])
        Global_k.append(K_sub)
    
    Total_stiffness_matrix = np.zeros((len(Node_data*2), len(Node_data*2)))
    Element_index_set_list = []
    
    for i in range(len(Element_data)):
        Element_index_set_list.append(compability_indexing(Element_data[i], Global_index))
    
    for i in range(len(Element_data)):
        # print(Global_k[i])
        # print(Element_index_set_list[i])
        temp = arrange_value_to_global_matrix(Global_k[i], Element_index_set_list[i], Total_stiffness_matrix.shape)
        Total_stiffness_matrix += temp
        # print(Total_stiffness_matrix)
        # print("*"*20)
    
    # K_det = det(Total_stiffness_matrix)
    F_matrix = np.zeros(len(Node_data)*2)
    
    for i in Load_data:
        node_id = i[0]
        position = Global_index[node_id]
        Fx = i[1]
        Fy = i[2]
        F_matrix[position[0]] = Fx
        F_matrix[position[1]] = Fy
        
    reduce_target= []
    oppose_target = []
    Displacment_matrix = np.zeros(len(Node_data)*2)
    for i in Support_data:
        node_id = i[0]
        position = Global_index[node_id]
        if i[1] == "V":
            reduce_target.append(position[1])
        elif i[1] == "H":
            reduce_target.append(position[0])
        elif i[1] == "P":
            reduce_target.append(position[0])
            reduce_target.append(position[1])
    
    reduce_matrix = np.delete(Total_stiffness_matrix, reduce_target, 0)
    reduce_matrix = np.delete(reduce_matrix, reduce_target, 1)
    
    reduce_inv = inv(reduce_matrix)
    F_matrix = np.delete(F_matrix, reduce_target, 0)
    temp_disp = np.dot(reduce_inv, F_matrix)
    j = 0
    for i in range(len(Support_data)*2):
        if i not in reduce_target:
            oppose_target.append(i)
            Displacment_matrix[i] = temp_disp[j]
            j+=1
    reduce_matrix = np.delete(Total_stiffness_matrix, oppose_target, 0)
    Reaction_force = np.dot(reduce_matrix, Displacment_matrix)
    
    Element_displacement = []
    for i in Element_index_set_list:
        temp = []
        for j in i:
            temp.append(Displacment_matrix[j])
        Element_displacement.append(temp)
    
    Stress_matrix = []
    for i in range(len(Element_data)):
        s = element_sines_and_cosines[i][0]
        c = element_sines_and_cosines[i][1]
        cosine_matrix = [-c, -s, c, s]
        L = element_lenght[i]
        sub_displacement = Element_displacement[i]
        temp = (E/L) * np.dot(cosine_matrix, sub_displacement)
        Stress_matrix.append(temp)
    
    Full_Result = [Displacment_matrix, Reaction_force, Stress_matrix, Total_stiffness_matrix]

    return Full_Result
    with open("Result_log.txt", 'w') as f:
        f.write('*'*100)
        f.write('\n')
        text = "Total Displacement on Each Node in Meters (m)"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('*'*100)
        f.write('\n'*2)
        index = 1
        for i in Full_Result[0]:
            f.write(" "*10 + "Node " + str(index) + ": ")
            f.write(str(i))
            f.write('\n')
            index +=1
        f.write('\n')
        f.write('$'*100)
        
        f.write('\n'*4)
        f.write('*'*100)
        f.write('\n')
        text = "Reaction Force on Constrain Node in Newton (N)"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('*'*100)
        f.write('\n'*2)
        index = 1
        for i in Full_Result[1]:
            f.write(" "*10 + "Node " + str(index) + ": ")
            f.write(str(i))
            f.write('\n')
            index +=1
        f.write('\n')
        f.write('$'*100)
        
        f.write('\n'*4)
        f.write('*'*100)
        f.write('\n')
        text = "Stress on Each Element in Pascal (Pa) "
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('*'*100)
        f.write('\n')
        index = 1
        for i in Full_Result[2]:
            f.write(" "*10 + "Element " + str(index) + ": ")
            f.write(str(i))
            f.write('\n')
            index +=1
        f.write('\n')
        f.write('$'*100)
        
        f.write('\n'*4)
        f.write('*'*100)
        f.write('\n')
        text = "Global Stiffness Matrix "
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('*'*100)
        f.write('\n')
        index = 1
        f.write(str(Total_stiffness_matrix))
        f.write('\n'*2)
        f.write('$'*100)
    
    os.startfile("Result_log.txt")