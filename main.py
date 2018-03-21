import sys
import matplotlib.pyplot as plt
sys.path.append("heat_controller")
sys.path.append("heat_functions")
sys.path.append("kernels")
from hierarchy import Heat_Controller_Hierarchy
from heat_functions import egene
from flat_kernel import flat_kernel

if __name__ == '__main__':
    #use :(atom,hsource,heat_min,heat_max,kernel,EOGkernel(constant))
    fdict = {"(A)":egene(100,1,100),"(B)":egene(200,5,300),"(C)":egene(500,20,50)}
    system = Heat_Controller_Hierarchy(["A","B","C"],fdict,-1000,1000,flat_kernel,1)
    while system.time < 100:
        system.update()
        system.show()
    plt.show()
