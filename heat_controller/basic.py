#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from statistics import mean, median,variance,stdev
import TMgenerator as tmg
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#basic

# class Tree Map Contoroller
class Heat_Controller:
    def __init__(self,atom,hsource,heat_min,heat_max,kernel,EOGkernel):
        self.atom = atom              #atom is set of chunk
        self.hsource = hsource        #hsource is dict: value = heat_source(s fomula), value = its function
        self.min =  heat_min          #heat min
        self.max =  heat_max          #heat max
        self.kernel = kernel          #kernel function
        self.EOGkernel = EOGkernel    #constant which is used for weight beteween EOG and perfect tree
        self.G = nx.Graph()           #Graph
        self.TL = tmg.generator(atom) #TL is dict : value = s fomula, value = number of chunk
        self.time = 0                 #time
        #add nodes, set heat on the node
        for s in self.TL.keys():
            if s not in self.hsource.keys():
                self.G.add_node(s, heat = self.max)
            else:
                for source,func in self.hsource.items():
                    if source == s:
                        self.G.add_node(s, heat = -func(0))


    def calc_weight(self):
        # set weight on edge (except EOG)
        for i in [k for k in self.TL.keys() if k != "EOG"]:
            for j in self.get_neighbors(i):
                self.G.add_edge(i, j, weight=self.kernel(i,j))

        # set weight on edge which is between EOG and the node that every atom is used
        for i in [k for k,v in self.TL.items() if v == len(self.atom)]:
            self.G.add_edge(i, "EOG", weight=self.EOGkernel)

    #neighbor is everyone except EOG
    def get_neighbors(self,base):
        return [k for k in self.TL.keys() if k != base and k != "EOG"]

    def info(self):
        print(self.G.nodes(data=True))
        print(self.G.edges(data=True))

    def show(self):
        #output infomation on console
        print(self.G.nodes(data=True))

        #calc stat info
        self.calc_stat()

        #visualize heat of node
        plt.clf()
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True ,edgelist = [], pos = self.npos)
        plt.pause(.02)

    # calc varicance of heat on the node that every atom is used
    def calc_stat(self):
        pnode = dict()
        for i in [k for k,v in self.TL.items() if v == len(self.atom)]:
            pnode[i] = nx.get_node_attributes(self.G, "heat")[i]
        print(pnode)
        m = mean(pnode.values())
        v = variance(pnode.values())
        l = min(pnode, key=(lambda x: pnode[x]))
        print('平均: {0:.2f}'.format(m))
        print('分散: {0:.2f}'.format(v))
        print("最低温木: " + l)


    def set_color(self):
        values = nx.get_node_attributes(self.G, "heat").values()
        return list(map(lambda x: (x+(self.max-self.min)/2)/(self.max-self.min), values))


    def update(self):
        self.time += 1
        tmpdict = dict()
        for i in [k for k in self.TL.keys() if k != "EOG"]:
            # dT/dt = ∇^2T + S
            # evaluate S
            if i not in self.hsource.keys():
                S=0
            else:
                for source,func in self.hsource.items():
                    if source == i:
                        S = -func(self.time)
            T = self.laplace_operator(i) + S
            tmpdict[i] = T + nx.get_node_attributes(self.G, "heat")[i]
        # set new heat map on node
        nx.set_node_attributes(self.G,tmpdict,"heat")


    def laplace_operator(self,base):
        # I-P
        # x_u - (1/m(u)) * sum(v)(k(u,v)x_v)
        x_u = nx.get_node_attributes(self.G, "heat")[base] # heat of base node
        ktotal = 0 #total of neighbor kernel value
        nheat = 0 #weighted (by kernel value) sum of neighbor heat

        for s,heat in self.G[base].items():
            ktotal += heat["weight"]
            nheat += heat["weight"] * nx.get_node_attributes(self.G, "heat")[s]

        #辻褄合わせのためにマイナスを最後につけている
        return -(x_u - (1/ktotal)*nheat)
