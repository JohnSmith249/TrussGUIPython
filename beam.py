#beam analysis and design
import numpy as np
from numpy.linalg import inv
import csv
import matplotlib.pyplot as plt
from pylab import figure, axes,pie, title, show
import seaborn as sns

#beam analysis using stiffness member approach
#node x nodey
node=[
    [0,0],
    [4,0],
    [10,0],
    [14,0]]
nnode=len(node)
#member
#node1 node2 E B D
#E= modulous of elastisity
#B,D= bredth and depth of section
member=[
    [1,2,1,12,1],
    [2,3,1,24,1],
    [3,4,1,12,1]]
nmember= len(member)    
#loading condition
memld=[
    [1,2,-16,4],
    [2,2,-16,6],
    [3,2,-16,4]]
#joint loading condition
nmemld=len(memld)
jdld=[
    [1,1,0]]
njdld=len(jdld)
#support condtion
#1-fixed/restrain 0-free
support=[
    [1,0],
    [1,0],
    [1,0],
    [1,0]]


sm = np.zeros((4,4,nmember))
sj = np.zeros((nnode*2,nnode*2))
aml = np.zeros((4,1,nmember))
am = np.zeros((4,1,nmember))
aj = np.zeros((nnode*2,1))
ae = np.zeros((nnode*2,1))
l=np.zeros(nmember)
length=np.zeros(nmember)
assem=np.zeros(4)
freemat=0
lenco=np.zeros(nnode)
tempmom=node[nnode-1][0]
nx=np.zeros((1,100,nmember))
momy=np.zeros((1,100,nmember))
sheary=np.zeros((1,100,nmember))
#------------------------------------------------
#for the aj matrix(joint action)
for i in range(0,njdld):
    if jdld[i][0]==1:
        if jdld[i][1]==1:
            aj[0]=jdld[i][2]
        elif jdld[i][0]==2:
                aj[1]=jdld[i][2]
        
    if jdld[i][1]==1:
        temp=2*jdld[i][0]
        aj[temp-2]=jdld[i][2]
    else:
        temp=jdld[i][0]
        temp=2*jdld[i][0]
        aj[temp-1]=jdld[i][2]

#-------------------------------------------------
#stiffness matrix for the each memeber
for i in range(0,nmember):
    #I for the retangular element is (bd**3)/12
    ei= member[i][2]*member[i][3]*(member[i][4]**3)/12
    i2= node[member[i][1]-1][0]-node[member[i][0]-1][0]
    i1= node[member[i][1]-1][1]-node[member[i][0]-1][1]
    #finding the length for the member
    l[i]=((i2**2)+(i1**2))**(1/2)
    length[i]=l[i]
    sm[0][0][i]=12*ei/(l[i]*l[i]*l[i])    
    sm[1][0][i]=6*ei/(l[i]*l[i])    
    sm[2][0][i]=-12*ei/(l[i]*l[i]*l[i])
    sm[3][0][i]=6*ei/(l[i]*l[i])
    
    sm[0][1][i]=6*ei/(l[i]*l[i])
    sm[1][1][i]=4*ei/(l[i])
    sm[2][1][i]=-6*ei/(l[i]*l[i])
    sm[3][1][i]=2*ei/(l[i])
    
    sm[0][2][i]=-12*ei/(l[i]*l[i]*l[i])
    sm[1][2][i]=-6*ei/(l[i]*l[i])
    sm[2][2][i]=12*ei/(l[i]*l[i]*l[i])
    sm[3][2][i]= -6*ei/(l[i]*l[i])

    sm[0][3][i]=6*ei/(l[i]*l[i])
    sm[1][3][i]=2*ei/(l[i])
    sm[2][3][i]=-6*ei/(l[i]*l[i])
    sm[3][3][i]=4*ei/(l[i])

    #aa=member[i][0]
    #bb=member[i][1]
    #cc=node[aa-1][0]
    #dd=node[bb-1][0]
    #nx[:,:,i]=np.linspace(cc,dd,50)
    #nx[:,:,i]=np.linspace(0,l[i],50)
    for j in range(1,100):
        part = l[i]/99
        nx[:,j,i]=nx[:,j-1,i]+ part
    #node number for the stiffness matrix sj
    assem[0] = 2*member[i][0]-2
    assem[1] = 2*member[i][0]-1
    assem[2] = 2*member[i][1]-2
    assem[3] = 2*member[i][1]-1
    #finding the coordinates
    #-------------------------------------------------
    #asembly of the stiffness matrix    
    for j in range(0,4):
        for k in range(0,4):
            jj=int(assem[j])
            kk=int(assem[k])
            sj[jj][kk]= sj[jj][kk]+sm[j][k][i]
#finding the coordinates
#-------------------------------------------------
nxtemp=nx
#for the member loading am matrix
for i in range(0,nmemld):
    if memld[i][1]==1:
        #POINT LOAD condition
        temp=(memld[i][0])-1
        l1=l[(temp)]
        a1 = memld[i][3]
        b1=l1-a1
        w1 = memld[i][2]
        #aml[0][0][temp]+= -(w1*b1*b1)*(((3*a1)+b1)/(l1**3))
        aml[0][0][temp]+= -(w1*a1)/(l1)
        aml[1][0][temp]+= -(w1*a1*b1*b1)/(l1**2)
        #aml[2][0][temp]+= -(w1*a1*a1)*(((3*b1)+a1)/(l1**3))
        aml[2][0][temp]+= -(w1*b1)/(l1)
        aml[3][0][temp]+= (w1*b1*a1*a1)/(l1**2)
        for j in range(0,100):
            if nx[0][j][temp]< a1:
                sheary[0][j][temp]+= -(w1*a1)/(l1)
            else:
                sheary[0][j][temp]+= +(w1*b1)/(l1) 

        for j in range(0,100):
            if nx[0][j][temp]< a1:
                p=nx[0][j][temp]
                momy[0][j][temp]+=(-w1*b1*p)/(l1)
            else:
                p=nx[0][j][temp]
                momy[0][j][temp]+=(-w1*a1*(l1-p))/(l1)
    
    elif memld[i][1]==2:
        #UDL conditon
        #UDL is for the given full length only
        temp0=(memld[i][0])-1
        temp = int((memld[i][0])-1)
        ll = memld[i][3]
        ww = memld[i][2]
        temp2= ww*ll/2
        temp3= ww*ll*ll/12
        temp4= ww*ll/2
        temp5= ww*ll*ll/12
        aml[0][0][temp0]+= -temp2 
        aml[1][0][temp0]+= -temp3
        aml[2][0][temp0]+= -temp4
        aml[3][0][temp0]+= temp5
        for j in range(0,100):
            p=nx[0][j][temp]
            sheary[0][j][temp]+= -ww*((ll/2)-p)
            momy[0][j][temp]+= -((ll-p)*ww*p)/2

    elif memld[i][1]==3:
        #MOMENT condition
        temp = int((memld[i][0])-1)
        l3=l[(temp)]
        a3 = memld[i][3]
        b3=l3-a3
        m3 = memld[i][2]
        l3temp= l3**3
        aml[0][0][temp]+= 6*m3*a3*b3/l3temp
        aml[1][0][temp]+= m3*b3*((2*a3)-b3)/(l3**2)
        aml[2][0][temp]+= -6*m3*a3*b3/l3temp
        aml[3][0][temp]+= m3*a3*((2*b3)-a3)/(l3**2)
        for j in range(0,100):
            sheary[0][j][temp]+= (-m3)/(l3)
            if nx[0][j][temp]<a3:
                p=nx[0][j][temp]
                momy[0][j][temp]+= (m3)*(p)/(l3)
            else:
                p=nx[0][j][temp]
                momy[0][j][temp]+= (m3)*((l3)-p)/(l3)
        
    elif memld[i][1]==4:
        #UVL condition
        #UVL is for the given full length only
        temp = int((memld[i][0])-1)
        l4=l[(temp)]
        w41 = memld[i][2]
        w410 = memld[i][3]
        w42= w410-w41
        temp = int((memld[i][0])-1)
        tri1 = -3*w42*l4/20
        tri2 = (-w42*l4**2)/30
        tri3 = -7*w42*l4/20
        tri4 = (w42*l4**2)/20
        aml[0][0][temp]+=(-w41*l4/2)+tri1
        aml[1][0][temp]+=(-(w41*l4**2)/12)+tri2
        aml[2][0][temp]+=(-w41*l4/2)+tri3
        aml[3][0][temp]+=((w41*l4**2)/12)+tri4
        for j in range(0,100):
            p=nx[0][j][temp]
            sheary[0][j][temp]+= -(w41)*((l4/2)-p) - ((w42/3)-((w42*p*p)/(l4**2)))
            momy[0][j][temp]+= -(((l4-p)*w41*p)/2)-(w42*p*((l4**2)-(p**2))/(3*l4**2))
        

#-------------------------------------------------
#write ae matrix        
for i in range(0,nmember):
    assem[0] = 2*member[i][0]-2
    assem[1] = 2*member[i][0]-1
    assem[2] = 2*member[i][1]-2
    assem[3] = 2*member[i][1]-1
    for j in range(0,4):
        jj=int(assem[j])
        ae[jj][0]=ae[jj][0]+aml[j][0][i]

#-------------------------------------------------
#finding the sff and sfc matrix
for i in range(0,nnode):  
    for j in range(0,2):
        if support[i][j] == 0:
            freemat+=1
        else:
            freemat=freemat

resmat = (nnode*2)- freemat
sff = np.zeros((freemat,freemat))
aff = np.zeros((freemat,1))
supportone =np.zeros(2*nnode)

#arrange the support in the horizontal diraction
for i in range(0,nnode):
    if i==0:
        supportone[0]=support[i][0]
        supportone[1]=support[i][1]
    else:
        supportone[(2*i)+1]=support[i][1]
        supportone[(2*i)]=support[i][0]

#fetch the number of free degree of freedom        
nfreedof =np.zeros(freemat)
tnode=2*nnode
resmat= tnode-freemat
nrisdof = np.zeros(resmat) 
temp=0
temp1=0

for i in range(0,(2*nnode)):
    if supportone[i]==0:
        nfreedof[temp] = i
        temp+=1
    else:
        nrisdof[temp1]=i
        temp1+=1

#write the sff matrix 
for i in range(0,freemat):
    for j in range(0,freemat):
        temp1=int(nfreedof[i])
        temp2=int(nfreedof[j])
        sff[i][j]=sj[temp1][temp2]

#for the srf matrix
sfr = np.zeros((resmat,freemat))
afr = np.zeros((resmat,1))
for i in range(0,resmat):
    for k in range(0,freemat):
        temp1=int(nrisdof[i])
        temp2=int(nfreedof[k])
        sfr[i][k]=sj[temp1][temp2]
        
#-------------------------------------------------
#for the ac matrix
ac=aj-ae
#for aff matrix
#write the sff matrix 
for i in range(0,freemat):
        temp1=int(nfreedof[i])
        aff[i][0]=ac[temp1][0]
#write the afr matrix
for i in range(0,resmat):
        temp1=int(nrisdof[i])
        afr[i][0]=ac[temp1][0]
#-------------------------------------------------
#find the displacement in the beam
disptemp=inv(sff)
disp = np.dot(disptemp,aff)
#-------------------------------------------------
#find the displacement for meember
dispglob = np.zeros((4,1,nmember))
dispfull= np.zeros((2*nnode,1))
for i in range(0,freemat):
    temp=int(nfreedof[i])
    dispfull[temp][0]= disp[i]
for i in range(0,nmember):
    assem[0] = (2*member[i][0]-2)
    assem[1] = 2*member[i][0]-1
    assem[2] = 2*member[i][1]-2
    assem[3] = 2*member[i][1]-1
    temp1=int(assem[0])
    temp2=int(assem[1])
    temp3=int(assem[2])
    temp4=int(assem[3])
    dispglob[0][0][i]=dispfull[temp1]
    dispglob[1][0][i]=dispfull[temp2]
    dispglob[2][0][i]=dispfull[temp3]
    dispglob[3][0][i]=dispfull[temp4]

#-------------------------------------------------
#find the displacement for meember
# AM = AML + SM*JD
for i in range(0,nmember):
    am[:,:,i]= aml[:,:,i]+ (np.dot(sm[:,:,i],dispglob[:,:,i]))

printam= np.zeros((4,nmember))
printaml= np.zeros((4,nmember))
for i in range(0,nmember):
    for j in range(0,4):
        for l in range(0,nmember):
            printam[j][i]=am[j][0][i]
            printaml[j][i]=aml[j][0][i]
#---------------------------------------------------
#end of calculation
#for diagram of calculation
dispmom= np.zeros((nmember,100))
dispshear= np.zeros((nmember,100))
for i in range(0,nmember):
    temp1= -am[1][0][i]
    temp2= am[3][0][i]
    dispmom[i][:]=np.linspace(temp1,temp2,100)
for i in range(0,nmember):
    temp3= am[0][0][i]
    temp4= -am[2][0][i]
    dispshear[i][:]=np.linspace(temp3,temp4,100)
#-------------------------------------------------
momyd=np.zeros((1,100,nmember))
sheard=np.zeros((1,100,nmember))
for i in range(0,nmember):
    for k in range(0,100):
        momyd[0][k][i]= momy[0][k][i]+dispmom[i][k]
        sheard[0][k][i]= sheary[0][k][i]+ dispshear[i][k] 
#sheary=np.zeros((1,11,nmember))

#printing of report
with open("output.html",'w',encoding = 'utf-8') as f:
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<head>\n")
    f.write("<link rel='stylesheet' href='styles.css'>")
    f.write("</head>")
    f.write("<h2><center><b><u>Beam Analysis Report<center></u></b></center></h2>")
    f.write("<hr>")
    f.write("<img src='BMD.svg'>")
    f.write("<h3><b><u><strong>Input Details</srong></u></b></h3>")
    f.write("<h4><b><u>Node Details</u></b></h4>\n")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>Node No.<b></th>\n")
    f.write("<th><b>X(m)<b></th>\n")
    f.write("<th><b>Y(m)<b></th>\n")
    for i in range(0,nnode):
        f.write("<tr>\n")
        f.write("<td>%d</td>\n"%(i+1))
        f.write("<td>%0.2f</td>\n"%node[i][0])
        f.write("<td>%0.2f</td>\n"% node[i][1])
        f.write("</tr>")
    f.write("</table>")
    f.write("<h4><b><u>Member Details:</u></b></h4>\n")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>Member No.<b></th>\n")
    f.write("<th><b>Node 1<b></th>\n")
    f.write("<th><b>Node 2<b></th>\n")
    f.write("<th><b>Length(m)<b></th>\n")
    f.write("<th><b>MoE(N/m<sup>2</sup>)<b></th>\n")
    f.write("<th><b>B(m)<b></th>\n")
    f.write("<th><b>D(m)<b></th>\n")
    for i in range(0,nmember):
        f.write("<tr>\n")
        f.write("<td>%d</td>\n"%(i+1))
        f.write("<td>%d</td>\n"%member[i][0])
        f.write("<td>%d</td>\n"%member[i][1])
        f.write("<td>%0.2f</td>\n"%length[i])
        f.write("<td>%0.2f</td>\n"%member[i][2])
        f.write("<td>%0.2f</td>\n"%member[i][3])
        f.write("<td>%0.2f</td>\n"%member[i][4])
        f.write("</tr>\n")
    f.write("</table>")
    f.write("<h4><b><u>Member Load:</u></b></h4>\n")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>Load No.<b></th>\n")
    f.write("<th><b>Member No.<b></th>\n")
    f.write("<th><b>Load Type<b></th>\n")
    f.write("<th><b>Intensity<b></th>\n")
    f.write("<th><b>Distance/Intensity<b></th>\n")
    for i in range(0,nmemld):
        f.write("<tr>\n")
        f.write("<td>%d</td>\n"%(i+1))
        f.write("<td>%d</td>\n"%memld[i][0])
        if memld[i][1]==1:
            f.write("<td>%d-(Point Load)</td>\n"%memld[i][1])
            f.write("<td>%0.2f kN</td>\n"%memld[i][2])
        elif memld[i][1]==2:
            f.write("<td>%d-(UDL)</td>\n"%memld[i][1])
            f.write("<td>%0.2f kN/m</td>\n"%memld[i][2])
        elif memld[i][1]==3:
            f.write("<td>%d-(Moment)</td>\n"%memld[i][1])
            f.write("<td>%0.2f kN.m</td>\n"%memld[i][2])
        else:
            f.write("<td>%d-(UVL)</td>\n"%memld[i][1])
            f.write("<td>%0.2f kN/m</td>\n"%memld[i][2])

        if memld[i][1]==4:
            f.write("<td>%0.2f kN/m</td>\n"%memld[i][3])
        else:
            f.write("<td>%0.2f m</td>\n"%memld[i][3])
        f.write("</tr>\n")
    f.write("</table>")
    #f.write("<b><sup>*</sup>1-pointload, 2-UDL, 3-Moment, 4-UVL</b><br>")
    #f.write("<b><sup>@</sup> for member type-4 distance=Intensity at right end</b>")
    f.write("<h4><b><u>Nodal Load:</u></b></h4>\n")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>Nodal Load No.</b></th>\n")
    f.write("<th><b>Member No.</b></th>\n")
    f.write("<th><b>Load Type</b></th>\n")
    f.write("<th><b>Intensity</b></th>\n")
    for i in range(0,njdld):
        f.write("<tr>\n")
        f.write("<td>%d</td>\n"%(i+1))
        f.write("<td>%d</td>\n"%jdld[i][0])
        if jdld[i][1]==1:
            f.write("<td>%d-(Point Load)</td>\n"%jdld[i][1])
            f.write("<td>%0.2f kN</td>\n"%jdld[i][2])
        else:
            f.write("<td>%d-(Moment)</td>\n"%jdld[i][1])
            f.write("<td>%0.2f kN.m</td>\n"%jdld[i][2])    
        f.write("</tr>\n")
    f.write("</table>")
    f.write("<h4><b><u>Support Condition:</u></b></h4>\n")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>Member No.<b></th>\n")
    f.write("<th><b>X<sup>*</sup><b></th>\n")
    f.write("<th><b>Y<sup>*</sup><b></th>\n")
    for i in range(0,nnode):
        f.write("<tr>\n")
        f.write("<td>%d</td>\n"%(i+1))
        f.write("<td>%d</td>\n"%support[i][0])
        f.write("<td>%d</td>\n"%support[i][1])
        f.write("</tr>\n")
    f.write("</table>")
    f.write("<sup>*</sup>1-Fixed, 0-Restrain")
    f.write("<br>")
    f.write("<br>")
    f.write("<hr>")
    f.write("<br>")
    f.write("<h3><b><u><strong>Output Details</srong></u></b></h3>")
    f.write("<table border='1' cellpadding='5'>\n")
    for i in range(0,nmember):
        f.write("<h4><b><u>Stiffness Matrix for member %d</u></b></h4>\n"%(i+1))
        f.write("<table border='0' cellpadding='5'>\n")
        for j in range(0,4):
            f.write("<tr>\n")
            for k in range(0,4):
                f.write("<td>%f</td>\n"%sm[j][k][i])
            f.write("</tr>\n")
        f.write("</table>")

    f.write("<h4><b><u>SJ matrix</u></b></h4>")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>DOF<b>\n</th>")
    for m in range (0,2*nnode):
        f.write("<th><b>%d<b>\n</th>"%(m+1))
    for i in range(0,2*nnode):
        f.write("<tr>\n")
        f.write("<td><b>%d<b>\n</td>"%(i+1))
        for j in range(0,2*nnode):
            if sj[i][j]==0:
                f.write("<td>0</td>\n")
            else:
                f.write("<td>%0.4f</td>\n"%sj[i][j])
        f.write("</tr>\n")
    f.write("</table>")
    f.write("<h4><b><u>SFF matrix</u></b></h4>")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th><b>DOF</b></th>\n")
    for i in range(0,freemat):
        f.write("<th><b>%d</b></th>\n"%nfreedof[i])
    for i in range(0,freemat):
        f.write("<tr>\n")
        f.write("<td><b>%d</b></td>\n"%nfreedof[i])
        for j in range(0,freemat):      
            f.write("<td>%0.4f</td>\n"%sff[i][j])
        f.write("</tr>\n")
    f.write("</table>")

    f.write("<br>")
    f.write("<h4><b><u>ADL Matrix</u></b></h4>")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th>Unit</th>")
    for i in range(0,nmember):
        f.write("<th>Member-%d</th>"%(i+1))
    for j in range(0,4):
        f.write("<tr>\n")
        if  j==0:
            f.write("<td>kN</td>\n")
        elif j==2:
            f.write("<td>kN</td>\n")
        else:
            f.write("<td>kN.m</td>\n")
        for k in range(0,nmember):   
            f.write("<td>%f</td>\n"%printaml[j][k])
        f.write("</tr>\n")
    f.write("</table>")
    f.write("<h4><b><u>AJ matrix</u></b></h4>")
    f.write("<table border='0' cellpadding='5'>\n")
    for i in range(0,2*nnode):
        f.write("<tr>\n")     
        f.write("<td>%0.4f</td>\n"%aj[i][0])
        f.write("</tr>\n")
    f.write("</table>")
    
    f.write("<h4><b><u>Final AM Matrix</u></b></h4>")
    f.write("<table border='0' cellpadding='5'>\n")
    f.write("<th>Unit</th>")
    for i in range(0,nmember):
        f.write("<th>Member-%d</th>"%(i+1))
    for j in range(0,4):
        f.write("<tr>\n")
        if  j==0:
            f.write("<td>kN</td>\n")
        elif j==2:
            f.write("<td>kN</td>\n")
        else:
            f.write("<td>kN.m</td>\n")
        for k in range(0,nmember):   
            f.write("<td>%f</td>\n"%printam[j][k])
        f.write("</tr>\n")
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")
    #for i in range(10):
     #f.write("<h1>welcome to world<h1> %d\r\n" % (i+1))

#ploting of graph sfd
#
for i in range(0,nmember):
   nxtemp[0,:,i]+= node[i][0]

sns.set_style("whitegrid")
# Color palette
blue, = sns.color_palette("muted", 1)
# Create data
x=[]
xs=[]
mz=[]
sy=[]
with open("bmd.csv",'w',encoding = 'utf-8') as f:
    for i in range(0,nmember):
        for k in range(0,100):
            f.write("%f,"%nx[0][k][i])
            f.write("%f\n"%momyd[0][k][i])
with open('BMD.csv','r')as csvfile:
    plots= csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        mz.append(float(row[1]))
for i in range(0,nnode):
    plt.scatter(node[i][0],node[i][1])
fig, ax = plt.subplots()
bmd=ax.plot(x, mz, color=blue, lw=2)
ax.fill_between(x, 0, mz, alpha=.3)

fig.set_size_inches(12.5,5.5)
plt.savefig('BMD.svg')
f.close()
plt.close()
with open("sfd.csv",'w',encoding = 'utf-8') as f:
    for i in range(0,nmember):
        for k in range(0,100):
            f.write("%f"%nx[0][k][i])
            f.write(",%f\n"%sheard[0][k][i])
with open('sfd.csv','r')as csvfile:
    plots= csv.reader(csvfile,delimiter=',')
    for row in plots:
        xs.append(float(row[0]))
        sy.append(float(row[1]))
for i in range(0,nnode):
    plt.scatter(node[i][0],node[i][1])
plt.plot(x,sy)
plt.savefig('sfd.svg')


            
