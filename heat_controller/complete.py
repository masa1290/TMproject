#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
from basic import Heat_Controller
#consider complete graph
#laplace operator = everyone

# class Tree Map Contoroller
class Heat_Controller_Complete(Heat_Controller):
    def __init__(self,atom,hsource,heat_min,heat_max,kernel,EOGkernel):
        #super class init
        super().__init__(atom,hsource,heat_min,heat_max,kernel,EOGkernel)
        #set edge between nodes and calc edge weight
        self.calc_weight()
        #show graph info and statistics
        self.info()
        self.calc_stat()
        #visualize heat of node
        self.npos = nx.circular_layout(self.G) #node position for matplotlib
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True, edgelist = [], pos = self.npos)
        plt.show()


    #neighbor is everyone except EOG
    def get_neighbors(self,base):
        return [k for k in self.TL.keys() if k != base and k != "EOG"]

    def show(self):
        #output infomation on console
        print(self.G.nodes(data=True))

        #calc stat info
        self.calc_stat()

        #visualize heat of node
        plt.clf()
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True ,edgelist = [],pos = self.npos)
        plt.pause(.02)
