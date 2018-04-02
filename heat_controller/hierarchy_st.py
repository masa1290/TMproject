#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
from hierarchy import Heat_Controller_Hierarchy
from time import sleep
#consider treelike graph
#laplace operator = upnode or downnode
#heat controller for st/sst kernel
#kernel value between one node tree and two node tree is set 1 by defalut
#because st/sst kernel value is 0 when evaluate it

# class Tree Map Contoroller
class Heat_Controller_Hierarchy_St(Heat_Controller_Hierarchy):

    def __init__(self,atom,hsource,heat_min,heat_max,kernel,decay,EOGkernel):
        #super class init
        super().__init__(atom,hsource,heat_min,heat_max,kernel,decay,EOGkernel)

    #kernel value between one node tree and two node tree is set 1 by defalut
    def calc_weight(self):
        # set weight on edge (except EOG)
        for i in [k for k,v in self.TL.items() if k != "EOG" and v != 1 and v != len(self.atom)]:
            for j in self.get_downnodes(i):
                self.G.add_edge(i, j, weight=self.kernel(i,j,self.decay))
        for i in [k for k,v in self.TL.items() if v == 1]:
            for j in self.get_downnodes(i):
                self.G.add_edge(i, j, weight=1)
        # set weight on edge which is between EOG and the node that every atom is used
        for i in [k for k,v in self.TL.items() if v == len(self.atom)]:
            self.G.add_edge(i, "EOG", weight=self.EOGkernel)
