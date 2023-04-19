# # from tkinter import *
# # from tkinter import ttk

# # root = Tk()
# # root.title('Test Notebook')
# # root.geometry("500x500")

# # my_notebook = ttk.Notebook(root)
# # my_notebook.pack(pady=15)

# # my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
# # my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

# # my_frame1.pack(fill="both", expand=1)
# # my_frame2.pack(fill="both", expand=1)
# # my_notebook.add(my_frame1, text="Blue Tab")
# # my_notebook.add(my_frame2, text="red tab")

# # root.mainloop()

# # from test_complete_examples import *
# from truss import Result, init_truss, plot_diagram
# import math

# def process_data(raw_data, mode):
#     if mode == 2:
#         Info = []
#         Value = []
#         for i in range(len(raw_data)):
#             if i%2 == 0:
#                 Info.append(raw_data[i])
#             else:
#                 Value.append(raw_data[i])
#         print(Info)
#         print(Value)
#         return Info, Value

#     if mode == 3:
#         Info=[]
#         Value1 = []
#         Value2 = []
#         for i in range(len(raw_data)):
#             try:
#                 Info.append(raw_data[0])
#                 raw_data.pop(0)
#                 Value1.append(raw_data[0])
#                 raw_data.pop(0)
#                 Value2.append(raw_data[0])
#                 raw_data.pop(0)
#             except:
#                 print("End of data")
#                 break
#         print(Info)
#         print(Value1)
#         print(Value2)
#         return Info, Value1, Value2

# def get_data(frame):
#     raw_data = []
#     for widget in frame.winfo_children():
#         if widget.winfo_class() == 'Entry':
#             raw_data.append[widget.get()]
#             # print(widget.get())
#     return raw_data

# # raw_data = [1,'P',3,'V',5,'P',7,'H']
# # data = process_data(raw_data, 2)
# # node_number = data[0]
# # type_of_support = data[1]
# # with open('support_data.txt', 'w+') as data_file:
# #     text = "Load"
# #     label_text = ' '*10 + "node number" + ' '*10 + "type of support" + ' '*10 + "\n"
# #     data_file.write(text)
# #     data_file.write("\n")
# #     data_file.write(label_text)
# #     for i in range(len(node_number)):
# #         data_text = ' '*10 + "node " + str(node_number[i]) + ' '*22 + str(type_of_support[i]) + ' '*10 + "\n"
# #         data_file.write(data_text)
# with open('Properties_data.txt','r') as data_file:
#     data = data_file.readlines()
#     Unit_sys = (data[2].split(':')[1]).replace(' ','')
#     Area = float((data[3].split(':')[1]).replace(' ',''))
#     Young_modulus = (data[4].split(':')[1]).replace(' ','')
#     Young_data = Young_modulus.split('e')
#     Young_modulus = int(Young_data[0]) * (10**int(Young_data[1]))

# with open('Node_data.txt','r') as data_file:
#     coordinate = []
#     data = data_file.readlines()
#     data.remove(data[0])
#     data.remove(data[0])
#     for i in data:
#        node_number = int(i.split(' '*22)[0].split('node')[1])
#        x_coordinate = float(i.split(' '*22)[1])
#        y_coordinate = float(i.split(' '*22)[2])
#        coordinate.append((x_coordinate, y_coordinate))
# # print(coordinate)

# corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# with open('Element_data.txt','r') as data_file:
#     element = []
#     element_data =  []
#     data = data_file.readlines()
#     data.remove(data[0])
#     data.remove(data[0])
#     for i in data:
#        node_number = int(i.split(' '*19)[0].split('element')[1])
#        begin_node = int(i.split(' '*19)[1]) - 1
#        end_node = int(i.split(' '*19)[2]) - 1
#        element_bar = corespond_letter[begin_node] + corespond_letter[end_node]
#        element.append(element_bar)
#        element_data.append((begin_node, end_node))
# # print(element)

# with open('support_data.txt','r') as data_file:
#     support = []
#     support_data = []
#     corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     data = data_file.readlines()
#     data.remove(data[0])
#     data.remove(data[0])
#     for i in data:
#        node_number = int(i.split(' '*19)[0].split('node')[1]) - 1 
#        supported_node = corespond_letter[node_number]
#        support_type = str(i.split(' '*22)[1][0])
#        support_data.append((node_number, support_type))
#        if support_type == 'P':
#            support_command = 'pin'
#            support.append((supported_node, support_command))
#        elif support_type == 'V':
#            support_command = 'roller'
#            angle = math.pi/2
#            support.append((supported_node, support_command, angle))
#        elif support_type == 'H':
#            support_command = 'roller'
#            angle = 0
#            support.append((supported_node, support_command, angle))
       
#     # print(support)


# with open('Load_data.txt','r') as data_file:
#     load = []
#     load_data = []
#     corespond_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     data = data_file.readlines()
#     data.remove(data[0])
#     data.remove(data[0])
#     for i in data:
#        node_number = int(i.split(' '*16)[0].split('node')[1]) - 1
#        loaded_node = corespond_letter[node_number]
#        Force_X = float(i.split(' '*16)[1])
#        Force_Y = float(i.split(' '*16)[2])
#        load.append((loaded_node, Force_X, Force_Y))
#        load_data.append((node_number, Force_X, Force_Y))


# # print(load)

# # my_truss = init_truss('My first truss')
# # my_truss.add_joints([(0, 0), (290, -90), (815, 127.5), (290, 345), (0, 255), (220.836, 127.5)])
# # my_truss.add_bars(['AB', 'BC', 'CD', 'DE', 'EF', 'AF', 'DF', 'BF'])
# # my_truss.add_loads([('C', 0, -0.675)])
# # my_truss.add_supports([('A', 'roller', math.pi/2), ('E', 'pin'), ('B', 'roller', -math.pi/2)])
# # my_truss.solve_and_plot()
# # results = Result(my_truss)
# # print(results)

# # *****************************************************************************************************************************

# import math
# import numpy

# numpy.set_printoptions(3, suppress=True)

# xco = [] #x co ordinate of nodes
# yco = [] #y co ordinate of nodes

# for i in coordinate:
#     xco.append(i[0])
#     yco.append(i[1])

# tn = len(xco)
# te = len(element_data)
# ##print(xco)
# ##print(yco)
    
# A = Area
# E = Young_modulus

# snofel = [] #start node of elements
# enofel = [] #end node of elements
# lenofel = [] #length of the element
# elcon = [] #constant of the element
# cosofel = [] #cos of element
# sinofel = [] #sin of element

# for i in range(te):  
#     a = element_data[i][0]
#     b = element_data[i][1]
#     x1 = float(xco[a-1])
#     y1 = float(yco[a-1])
#     x2 = float(xco[b-1])
#     y2 = float(yco[b-1])
#     l = math.sqrt((x2-x1)**2+(y2-y1)**2)
#     con = A*E/l
#     cos = (x2-x1)/l
#     sin = (y2-y1)/l
    
#     snofel.append(a)
#     enofel.append(b)
#     lenofel.append(l)
#     elcon.append(con)
#     cosofel.append(cos)
#     sinofel.append(sin)
    
# ##print(snofel)
# ##print(enofel)
# ##print(lenofel)
# ##print(elcon)
# ##print(cosofel)
# ##print(sinofel)

# elstmat = [] #element stiffness matrix

# for i in range(te):
#     cc = float(cosofel[i])**2
#     ss = float(sinofel[i])**2
#     cs = float(cosofel[i])*float(sinofel[i])
    
#     mat = elcon[i]*numpy.array([[cc, cs, -cc, -cs],
#                       [cs, ss, -cs, -ss],
#                       [-cc, -cs, cc, cs],
#                       [-cs, -ss, cs, ss]])

#     elstmat.append(mat)
# ##print(elstmat)


# gstmatmap = []                          ## Global stiffness matrix mapping, gstmatmap will be the sqare matrix of tn*
# for i in range(te):                     ## do this for each elements
#     m = snofel[i]*2                     ## taking the start node of element(i) and multiply by 2
#     n = enofel[i]*2                     ## taking the end node of element(i) and multiply by 2
#     add = [m-1, m, n-1, n]              ## Address of columns and rows of gstmatmap for elemet(i)
#                                             # if startnode is 1 and end node is 2 then add=[1,2,3,4]
#                                             # if startnode is 1 and end node is 3 then add=[1,2,5,6]
#     gmat = numpy.zeros((tn*2, tn*2))    ## global stiffness matrix loaded with zeros for element(i)
#     elmat = elstmat[i]                  ## taking the element stiffness matrix of element(i)
#     for j in range(4):                  
#         for k in range(4):              
#             a = add[j]-1                ## addressing row of GST matrix for element(i)
#             b = add[k]-1                ## addressing column of GST matrix for element(i)
#             gmat[a,b] = elmat[j,k]      ## updating the values in GST matrix with EST matrix of element(i)
#     gstmatmap.append(gmat)              ## storing the resultant matrix in gstmatmap list
# ##    print(numpy.around(gmat, 3))

# GSM = numpy.zeros((tn*2, tn*2))         ## creating an empyty GSM matrix
# for mat in gstmatmap:
#     GSM = GSM+mat                       ## adding all the matrix in the gstmatmap list
#                                             # this will result in assembled stiffness matrix of the truss structure

# with open('Result_log.txt', 'w') as result_log:
#     result_log.write('\nGlobal Stiffness Matrix of the Truss\n')
#     result_log.write(str(numpy.around(GSM, 3)))
# print('\nGlobal Stiffness Matrix of the Truss\n')
# print(numpy.around(GSM, 3))

# #-----------------------Boundry condition and Loading---------------------#

# displist = []
# forcelist = []
# for i in range(tn):
#     a = str('u')+str(i+1)
#     displist.append(a)
#     b = str('v')+str(i+1)
#     displist.append(b)
#     c = str('fx')+str(i+1)
#     forcelist.append(c)
#     d = str('fy')+str(i+1)
#     forcelist.append(d)

# ##print(displist)
# ##print(forcelist)
    
# print('\n\n________________Support Specifications______________\n')

# dispmat = numpy.ones((tn*2,1))
# tsupn = len(support) #total number of supported nodes
# supcondition = ['P = pinned',
#                 'H = Horizonal restrained (vertical is free to move)',
#                 'V = Vertical restrained (Horizontal is free to move)']
   
# for i in range(tsupn):
#     supn = support_data[i][0] #supported node
#     for a in supcondition:
#         print(a)
#     condition = support_data[i][1]
#     if condition in['P', 'p']:
#         dispmat[supn*2-2, 0] = 0
#         dispmat[supn*2-1, 0] = 0
#     elif condition in['H', 'h']:
#         dispmat[supn*2-2, 0] = 0
#     elif condition in['V', 'v']:
#         dispmat[supn*2-1, 0] = 0
#     else:
#         print('Please enter valid entries')
# ##print(dispmat)


# print('\n_________________Loading____________________\n')
# forcemat = numpy.zeros((tn*2,1))
# tlon = len(load) #total number of loaded nodes

# for i in range(tlon):
#     lon = load_data[i][0] #Loaded node
#     fx = load_data[i][1]
#     fy = load_data[i][2]
#     forcemat[lon*2-2, 0] = fx
#     forcemat[lon*2-1, 0] = fy

# ##print(forcemat)    


# ###_________________Matrix Reduction_________________###


# rcdlist = []
# for i in range(tn*2):
#     if dispmat[i,0] == 0:
#         rcdlist.append(i)

# rrgsm = numpy.delete(GSM, rcdlist, 0) #row reduction
# crgsm = numpy.delete(rrgsm, rcdlist, 1) #column reduction
# rgsm = crgsm #reduced global stiffness matrix
# rforcemat = numpy.delete(forcemat, rcdlist, 0) #reduced force mat
# rdispmat = numpy.delete(dispmat, rcdlist, 0) #reduced disp mat

# ###_______________Solving____________________###

# dispresult = numpy.matmul(numpy.linalg.inv(rgsm), rforcemat)
# rin = 0
# for i in range(tn*2):
#     if dispmat[i,0] == 1:
#         dispmat[i,0] = dispresult[rin,0]
#         rin = rin+1
# ##print(dispmat)

# forceresult = numpy.matmul(GSM, dispmat)
# ##print(forceresult)

# with open('Result_log.txt', 'a') as result_log:
#     result_log.write('\nGlobal Stiffness Matrix of the Truss\n')
#     result_log.write(str(GSM))
#     result_log.write('\n\nGlobal Stiffness Matrix of the Truss\n')
#     result_log.write(str(dispmat))
#     result_log.write('\n\nForce matrix of nodes\n')
#     result_log.write(str(forceresult))

# print('\n\nGlobal Stiffness Matrix of the Truss\n')
# print(GSM)
# print('\n\nDisplacement matrix of nodes\n')
# print(dispmat)
# print('\n\nForce matrix of nodes\n')
# print(forceresult)

# ##____________________new co ordinates of nodes____________####

# newxco = []
# newyco = []
# count = 0
# for i in range(tn):
#     k = xco[i]+dispmat[count,0]
#     newxco.append(k)
#     count = count+1
#     l = yco[i]+dispmat[count,0]
#     newyco.append(l)
#     count = count+1

# ###____________________new length of memebers______________####
    
# newlenofel = []
# for i in range(te):
#     a, b = snofel[i], enofel[i]
#     x1 = float(newxco[a-1])
#     y1 = float(newyco[a-1])
#     x2 = float(newxco[b-1])
#     y2 = float(newyco[b-1])
#     l = math.sqrt((x2-x1)**2+(y2-y1)**2)
#     newlenofel.append(l)

# ##print(newlenofel)
# ##print(lenofel)

# ###______________strain in elements_______________________###
    
# numpy.set_printoptions(3, suppress=False)

# elstrain = numpy.zeros((te,1))
# for i in range(te):
#     elstrain[i,0] = (newlenofel[i]-lenofel[i])/(lenofel[i])

# with open('Result_log.txt', 'a') as result_log:
#     result_log.write('\n***Positive is Tensile\nNegetive is Compressive***\n')
#     result_log.write('\n\nStrain in the elements')
#     result_log.write(str(elstrain))

# print('\n***Positive is Tensile\nNegetive is Compressive***\n')
# print('\n\nStrain in the elements')
# print(elstrain)
# numpy.set_printoptions(3, suppress=True)

# ###__________________stress in elements______________________###

# elstress = numpy.zeros((te,1))
# for i in range(te):
#     elstress[i,0] = E * elstrain[i,0]


# with open('Result_log.txt', 'a') as result_log:
#     result_log.write('\n\nStress in the elements')
#     result_log.write(str(elstress))
# print('\n\nStress in the elements')
# print(elstress)

# ###_________________Member forces____________________#########

# eforce = numpy.zeros((te,1))
# for i in range(te):
#     eforce[i,0] = A * elstress[i,0]

# with open('Result_log.txt', 'a') as result_log:
#     result_log.write('\n\nForce in the element')
#     result_log.write(str(eforce))


# print('\n\nForce in the element')
# print(eforce)

# ##numpy.delete(mat, row, 0)
# ##numpy.delete(mat, col, 1)
# ##numpy.matmul(mat1, mat2)
# ##numpy.linalg.inv(mat)
# ##numpy.arange(start, end, step)
# ##array.reshape(row, col)
# ##numpy.zeros((row,col))
# ##numpy.ones((row,col))



##*******************************************************************************************************************************##

import SpFunc
SpFunc.SolveEngine00()