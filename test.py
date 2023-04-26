import numpy as np
from anastruct import SystemElements
from SolveEngine01 import SolveEngine01, Read_data
import os

# ss = SystemElements(EA=2e9, EI=2e5)

# # ss.add_element(location=[[0,0],[3,4]])
# # ss.add_element(location=[[3,4],[8,4]])
# # ss.add_support_hinged(node_id=1)
# # ss.add_support_fixed(node_id=3)
# # ss.q_load(element_id=2, q=-10)
# # ss.solve()

# ss.add_element(location=[[0,0],[0,1]])
# ss.add_element(location=[[0,1],[0.5,1]])
# ss.add_element(location=[[0.5,1],[1,1]])
# ss.add_element(location=[[1,1],[2,0]])
# # ss.add_truss_element(location=[[1,1],[2,2]])
# # ss.add_truss_element(location=[[1,1],[2,0]])

# ss.add_support_fixed(node_id=1)
# ss.add_support_fixed(node_id=4)
# # ss.add_support_roll(node_id=1, direction=2)
# # ss.add_support_hinged(node_id=2)
# # ss.add_support_hinged(node_id=3)

# ss.q_load(q=-10000, element_id=1, direction='element')
# ss.moment_load(node_id=2, Ty=-10000)
# ss.point_load(node_id=3, Fy=10000)

# ss.solve()

# for i in range(5):
#     print(ss.get_node_displacements(node_id=i+1)['ux'])
#     print(ss.get_node_displacements(node_id=i+1)['uy'])
#     print("*"*40)
# ss.show_structure()
# # ss.show_reaction_force()
# # ss.show_axial_force()
# # ss.show_shear_force()
# ss.show_bending_moment()
# ss.show_displacement()

Node_data = Read_data("nodes")
Properties_data = Read_data("properties")
Element_data = Read_data("elements")
Support_data = Read_data("supports")
Load_data = Read_data("loads")

ss = SystemElements(EA=2e9, figsize=(7,5))
for i in range(len(Element_data)):
    begin = Element_data[i][0]
    end = Element_data[i][1]
    begin_coor = list(Node_data[begin])
    end_coor = list(Node_data[end])
    ss.add_truss_element(location=[begin_coor, end_coor])
ss.show_structure()