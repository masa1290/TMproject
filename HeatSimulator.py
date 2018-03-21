#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from statistics import mean, median,variance,stdev
import TMgenerator as tmg
import networkx as nx
import numpy as np
import kernel_calc as kernel
import matplotlib.pyplot as plt
import random
#consider complete graph

# class Tree Map Contoroller
class TMC:
    #atom is set of chunk / hsource is pair(dict) of heat_source and function
    def __init__(self,atom,hsource):
        self.hsource = hsource
        self.atom = atom
        self.G = nx.Graph()
        self.TL = tmg.generator(atom) #all tree list
        self.time = 0
        #add nodes, set heat on the node
        for s in self.TL:
            if s not in self.hsource.keys():
                self.G.add_node(s, heat = 1000)
            else:
                for source,func in self.hsource.items():
                    if source == s:
                        self.G.add_node(s, heat = -func(0))
        #calc edge weight
        self.calc_weight()

        #visualize heat of node
        self.pos = nx.circular_layout(self.G)
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True ,edgelist = [], pos = self.pos)
        plt.show()


    def calc_weight(self):
        # set weight on edge (except EOG)
        for i in [k for k in self.TL if k != "EOG"]:
            for j in [k for k in self.TL if k != i and k != "EOG"]:
                self.G.add_edge(i, j, weight=1)
                #change kernel when time comes /weight = kernel.main(i,j,1)
        # set weight on edge which is between EOG and the node that every atom is used
        for i in [k for k in self.TL if k != "EOG"]:
            count = 0
            for j in self.atom:
                if not i.count(j):break
                count += 1
            if count == len(self.atom):
                self.G.add_edge(i, "EOG", weight=1)

    def show_neighbors(self,base):
        print(self.G[base])
        #print(nx.get_node_attributes(self.G,"heat")["(B)"])

    def show(self):
        #output infomation on console
        print(self.G.nodes(data=True))

        #calc stat info
        self.calc_stat()

        #visualize heat of node
        plt.clf()
        nx.draw(self.G, cmap=plt.get_cmap('rainbow'), node_color=self.set_color(), with_labels=True ,edgelist = [], pos = self.pos)
        plt.pause(.02)

    # calc varicance of heat on the node that every atom is used
    def calc_stat(self):
        pnode = dict()
        for i in [k for k in self.TL if k != "EOG"]:
            count = 0
            for j in self.atom:
                if not i.count(j):break
                count += 1
            if count == len(self.atom):
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
        return list(map(lambda x: (x+1000)/2000, values))


    def update(self):
        self.time += 1
        tmpdict = dict()
        for i in [k for k in self.TL if k != "EOG"]:
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



# exponential fucntion generator
def egene(a,b,c):
    return lambda x: a*np.exp(-b*x)+c

if __name__ == '__main__':
    # dictionary of function
    fdict = {"(A)":egene(100,1,100),"(B)":egene(200,5,300),"(C)":egene(500,20,50)}
    HeatSystem = TMC(["A","B","C"],fdict)
    HeatSystem.show()

    while HeatSystem.time < 100:
        HeatSystem.update()
        HeatSystem.show()
    plt.show()
