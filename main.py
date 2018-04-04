import sys
import matplotlib.pyplot as plt
sys.path.append("heat_controller")
sys.path.append("heat_functions")
sys.path.append("kernels/eriko_kernels")
from hierarchy_st import Heat_Controller_Hierarchy_St
from heat_functions import egene
from subset_tree_kernel import subset_tree_kernel


if __name__ == '__main__':
    #use :(atom,hsource,heat_min,heat_max,kernel,decay,EOGkernel):
    fdict = {"(A)":egene(100,1,100),"(B)":egene(200,5,300),"(C)":egene(500,20,50)}
    system = Heat_Controller_Hierarchy_St(["A","B","C"],fdict,-1000,1000,subset_tree_kernel,1,1)
    system.info()
    #sys.exit()

    while system.time < 100:
        system.update()
        system.show()
    plt.show()
