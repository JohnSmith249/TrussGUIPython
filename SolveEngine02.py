from SolveEngine01 import Read_data
from anastruct import SystemElements

def Solve_Engine_02():
    

    Node_data = Read_data("nodes")
    Properties_data = Read_data("properties")
    Element_data = Read_data("elements")
    Support_data = Read_data("supports")
    Load_data = Read_data("loads")
    
    A = Properties_data[0]
    E = Properties_data[1]

    ss = SystemElements(EA=E*A)

    for i in range(len(Element_data)):
        begin = Element_data[i][0]
        end = Element_data[i][1]
        begin_coor = list(Node_data[begin])
        end_coor = list(Node_data[end])
        ss.add_truss_element(location=[begin_coor, end_coor])

    for i in range(len(Support_data)):
        node_index = Support_data[i][0] + 1
        support_type = Support_data[i][1]
        if support_type == 'P':
            ss.add_support_hinged(node_id=node_index)
        if support_type == 'V':
            ss.add_support_roll(node_id=node_index, direction=2)
        if support_type == 'H':
            ss.add_support_roll(node_id=node_index, direction=1)

    for i in range(len(Load_data)):
        node_index = Load_data[i][0] + 1
        Force_x = Load_data[i][1]
        Force_y = Load_data[i][2]
        ss.point_load(node_id=node_index, Fx=Force_x, Fy=Force_y)

    ss.solve()

    for i in range(4):
        print(ss.get_node_displacements(node_id=i+1)['ux'])
        print(ss.get_node_displacements(node_id=i+1)['uy'])
        print("*"*40)

    ss.show_structure()
    ss.show_axial_force()

# Solve_Engine_02()