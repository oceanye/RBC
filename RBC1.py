from numpy import *
import numpy as np
from test.py import *


#   LR11     LR12
#      -------
#

Sec_Info=[[600,800],[1,0],[2,0]] # section_size , [x1,y1],[x2,y2]
Reb_Info=[[50,59],[80,0],[2.5,1.8]]  # longitudinal Rebar UpStart UpEnd; longitudinal Buttom ,0;  Stirrup1 + Stirrup2
Reb_Size=[28,28] # Longitudinal rebar size Upper, Buttom


Beam_Info=np.concatenate((Sec_Info,Reb_Info), axis=0)
#test github3

def uni_RB(Beam_Info):
    if Beam_Info[1,1]<Beam_Info[1,0]:
        Beam_Info[1, [0, 1]] = Beam_Info[1, [1, 0]]
        Beam_Info[2, [0, 1]] = Beam_Info[2, [1, 0]]
        Beam_Info[3, [0, 1]] = Beam_Info[3, [1, 0]]
    return(Beam_Info)

def LReb_cal(cal_lrebar_area,d):
    S_Rebar_Area = 0.25*3.14*d*d/100
    Reb_num = ceil(cal_lrebar_area/S_Rebar_Area)
    return[Reb_num,d]

def SReb_cal(width,cal_srebar,dis,n):
    if (n<4 and width>350): n=4
    d=sqrt(cal_srebar*dis/n/(0.25*3.14))
    d=ceil(d/2)*2
    if d<8:d=8
    return[d,dis,n]

def LReb_area(data):  #  print LReb_area([2,25])
    [n,d]=data
    A=n*0.25*3.14*d*d   # mm^2
    return A

def SReb_area(data):
    [d,dist,n]=data
    A=n*0.25*3.14*d*d/dist   # mm^2/1000mm
    return A

def Simple_Beam(Beam_Info,Reb_Size):
    A=make_nd_list([2,3],2,0)
    print(A)
    LR_up1=LReb_cal(Beam_Info[3,0],Reb_Size[0])
    LR_up2=LReb_cal(Beam_Info[3,1],Reb_Size[0])
    LR_buttom=LReb_cal(Beam_Info[4,0],Reb_Size[1])
    SR1   =SReb_cal(Beam_Info[0,0],Beam_Info[5,0],100,2)
    SR2   =SReb_cal(Beam_Info[0,0],Beam_Info[5,1],100,2)
    rebar_table = [LR_up1,LR_up2,LR_buttom,SR1,SR2]
    print size(A)
#    print np.shape(rebar_table[0,3])
    return rebar_table



def Real_Simple_Beam(Sec_info,cal_rebar_table):
    LB_up1=LReb_area(cal_rebar_table[0])
    LB_up2=LReb_area(cal_rebar_table[1])
    LB_buttom=LReb_area(cal_rebar_table[2])
    SR1 = SReb_area(cal_rebar_table[3])
    SR2 = SReb_area(cal_rebar_table[4])
    Ac=Sec_info[0,0]*Sec_info[0,1]
    As = [LB_up1,LB_up2,LB_buttom,SR1,SR2]     #reinforcement area
    p  = As/[Ac,Ac,Ac,1,1]                                # reinforcement ratio
    real_reb_info=[As,p]
    return real_reb_info


def Arrange_Cont_Beam(SB_list):   #SB_list= SB1,SB2,SB3
    t = shape(SB_list)
    N_span = t[0]
    coord_x1y1=SB_list[:][0][1]
    coord_x2y2=SB_list[:][0][2]
    print ("shape x1y1",shape(coord_x1y1))

    D_list =[N_span,b,h]
    CB_list=[D_List,R_SB_list]    # D_list, SB1,SB2...
    return [CB_list]

def Count_most(A):
    T=set(A)
    M_num=zeros(size(T),2)

    return



def Sort_CB_from_SB(SB_list):
    t = len(SB_list)
    N_span = t[0]
    Coord=np.zeros((N_span-1,2))
    print shape(Coord)
    for p in range(N_span-1):
        Coord[p]=SB_list[0][p][1:2]
    return index


def Sort_Coord(coord):
    [x0,y0]=[-1e10,-1e10]
    di=np.zeros(len(coord))
    for i in range(len(coord)-1):
        di[i]=math.sqrt((coord[i][0]-x0)**2+(coord[i][1]-y0)**2)
        print di[i]
    index=np.argsort(di)
    return index

def make_nd_list(dim,n,initial_value):
    if n == 1:
        return [initial_value for i in range(dim[n - 1])]
    else:
        return [make_nd_list(dim, n - 1, initial_value) for i in range(dim[n - 1])]

TB=Simple_Beam(Beam_Info,Reb_Size)
TB2=Real_Simple_Beam(Sec_Info,TB)
SB=(Sec_Info,TB2)

SB1=(Sec_Info*2,TB2*2)
SB2=(Sec_Info*3,TB2*3)

TB_list=(SB,SB1)


print "ouput_test"

SB_list=[SB,SB1,SB2]
#Arrange_Cont_Beam(SB_list)
print ("shape_SB_list" ,shape(SB_list))
print SB_list

print ("size C")
C1=SB_list[0][0][1]  # SB1 [x1,y1]
C2=SB_list[0][0][2]  # SB1 [x2,y2]
C3=SB_list[1][0][1]  # SB2 [x1,y1]
C4=SB_list[1][0][2]  # SB2 [x2,y2]
C=([C1,C2,C3,C4])

C_l=np.zeros(2)



for i in range(1,2):
    C_l[i]=SB_list[i-1][0][1]

print "C1"
print C1

print "C_l"
print C_l

print "C"
print C
print shape(C)



print("size")


#Real_TB=Real_Simple_Beam(Sec_Info,TB)
print(shape(TB[0]))
print(TB2)
print(TB)

print LReb_area(TB[0])