from SolveEngine01 import Read_data
from anastruct import SystemElements
from SolveEngine01 import SolveEngine01

def Solve_Engine_02(key):

    Node_data = Read_data("nodes")
    Properties_data = Read_data("properties")
    Element_data = Read_data("elements")
    Support_data = Read_data("supports")
    Load_data = Read_data("loads")
    
    A = Properties_data[0]
    E = Properties_data[1]

    ss = SystemElements(EA=E*A, figsize=(6,4))

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

    # for i in range(4):
    #     print(ss.get_node_displacements(node_id=i+1)['ux'])
    #     print(ss.get_node_displacements(node_id=i+1)['uy'])
    #     print("*"*40)
    Fig = [ss.show_structure(show=False),
    ss.show_axial_force(show=False),
    ss.show_displacement(show=False)]

    Node_displacements = []
    Node_result_system = []
    Element_result = []

    for i in range(len(Node_data)):
        Node_displacements.append(ss.get_node_displacements(node_id=i+1))
        Node_result_system.append(ss.get_node_results_system(node_id=i+1))
        Element_result.append(ss.get_element_results(element_id=i+1))


        print("node id :" + str(ss.get_node_displacements(node_id=i+1)['id']))
        print("ux :" + str(ss.get_node_displacements(node_id=i+1)['ux']))
        print("uy :" + str(ss.get_node_displacements(node_id=i+1)['uy']))
        print("phi y :" + str(ss.get_node_displacements(node_id=i+1)['phi_y']))
        print('*'*40)
    
    with open('Full_result.txt', 'w') as f:
        f.write('='*100 + '\n')
        text = "Node Dispalcements"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('='*100 + '\n'*3)
        for i in Node_displacements:
            f.write('+'*100 + '\n')
            f.write("node id : " + str(i['id']) + '\n')
            f.write("ux : " + str(i['ux']) + '\n')
            f.write("uy : " + str(i['uy']) + '\n')
            f.write("phi y : " + str(i['phi_y']))
            f.write('\n' + '+'*100 + '\n'*1)
        
        f.write('\n'*5)
        f.write('='*100 + '\n')
        text = "Node Result System"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('='*100 + '\n'*3)
        for i in Node_result_system:
            f.write('+'*100 + '\n')
            f.write("node id : " + str(i['id']) + '\n')
            f.write("Fx : " + str(i['Fx']) + '\n')
            f.write("Fy : " + str(i['Fy']) + '\n')
            f.write("Ty : " + str(i['Ty']) + '\n')
            f.write("ux : " + str(i['ux']) + '\n')
            f.write("uy : " + str(i['uy']) + '\n')
            f.write("phi y : " + str(i['phi_y']))
            f.write('\n' + '+'*100 + '\n'*1)
        
        f.write('\n'*5)
        f.write('='*100 + '\n')
        text = "Element Result System"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('='*100 + '\n'*3)
        for i in Element_result:
            f.write('+'*100 + '\n')
            f.write("node id : " + str(i['id']) + '\n')
            f.write("alpha : " + str(i['alpha']) + '\n')
            f.write("u : " + str(i['u']) + '\n')
            f.write("maximum axial compression force : " + str(i['N']))
            f.write('\n' + '+'*100 + '\n'*1)
        
        Solve_data = SolveEngine01()

        f.write('\n'*5)
        f.write('='*100 + '\n')
        text = "Total Stiffness Matrix"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('='*100 + '\n'*3)
        f.write('+'*100 + '\n')
        f.write(str(Solve_data[-1]))
        f.write('\n' + '+'*100 + '\n'*1)

        f.write('\n'*5)
        f.write('='*100 + '\n')
        text = "Stress matrix"
        f.write(f'{text:-^100}')
        f.write('\n')
        f.write('='*100 + '\n'*3)
        f.write('+'*100 + '\n')
        f.write(str(Solve_data[2]))
        f.write('\n' + '+'*100 + '\n'*1)


    if key == "graph":
        return Fig
    

Solve_Engine_02('graph')
# ss.show_bending_moment(show=False),
# ss.show_shear_force(show=False),