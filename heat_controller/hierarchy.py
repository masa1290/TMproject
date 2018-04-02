#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
from basic import Heat_Controller
#consider treelike graph
#laplace operator = upnode or downnode

# class Tree Map Contoroller
class Heat_Controller_Hierarchy(Heat_Controller):
    def __init__(self,atom,hsource,heat_min,heat_max,kernel,decay,EOGkernel):
        #super class init
        super().__init__(atom,hsource,heat_min,heat_max,kernel,decay,EOGkernel)
        #set edge between nodes and calc edge weight
        self.calc_weight()
        #show graph info and statistics
        self.info()
        self.calc_stat()
        #visualize heat of node
        self.npos = nx.kamada_kawai_layout(self.G) #node position for matplotlib
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True, pos = self.npos)
        plt.show()


    #neighbor is upnode or downnode: ex. a->b's neighbor is a and a->b->c
    def get_neighbors(self,base):
        a = self.get_upnodes(base)
        b = self.get_downnodes(base)
        return a.extend(b)

    #neighbor is upnode or downnode: ex. a->b's neighbor is a and a->b->c
    def get_upnodes(self,base):
        return [k for k,v in self.TL.items() if k != base and v == self.TL[base]-1]

    def get_downnodes(self,base):
        return [k for k,v in self.TL.items() if k != base and v == self.TL[base]+1]

    def show(self):
        #output infomation on console
        print(self.G.nodes(data=True))

        #calc stat info
        self.calc_stat()

        #visualize heat of node
        plt.clf()
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True ,pos = self.npos)
        plt.pause(.02)
