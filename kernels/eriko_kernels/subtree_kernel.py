#! /usr/local/bin/python3
# -*- coding: utf-8 -*


import sys
import math
import re
import itertools
from convert import Sm_to_Sk

def subtree_kernel(s1,s2,LAMDA):
    #convert matsuoka's S fomula to kanagawa's S fomula
    s1 = Sm_to_Sk(s1)
    s2 = Sm_to_Sk(s2)

    #s式から配列の形にする
    s1_array=to_array(s1)
    s2_array=to_array(s2)

    s1_set = []
    s2_set = []
    s1_set = to_subtree(s1_array,s1_set)#配列からサブツリーの集合をつくる
    s2_set = to_subtree(s2_array,s2_set)

    kernel_value=subtree_calculation(s1_set,s2_set,LAMDA)
    print ("subtree kernel value:  "+str(kernel_value))
    return kernel_value

def to_array(s): #出来たと思う
    #print s
    count=0
    array_count=0
    s_array=[]


    s=s.replace(' ','')
    x=s.split("(")
    #print x
    i=1
    last_array=s_array
    while i<len(x):
        #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        xx=x[i]
        if i==1:                    #第一項とその他の場合分け
            s_array.append(xx)
            last_array=s_array
            array_count+=1
        else:
            new_array=[]
            #print "追加するもの"
            #print xx
            xx1=xx.replace(')','')
            #print xx1
            new_array.append(xx1)   #新しい配列に入れる
            #print "new_array"
            #print new_array[0]
            #print "last_array"
            #print last_array
            last_array.append(new_array)#今までの配列に結合
            #print last_array
            #print "くっつけたよ"
            array_count+=1
            #print "last"
            #print last_array

            flag=")" in xx  #今見ている項に)があるかのflag
            #print "xx"
            #print xx

            if flag==0: #)が無い＝配列をもう一段深くする＝次くっつける配列は今のもの
                last_array=last_array[len(last_array)-1]
                #print ")無いよ"
                #print "くっつけるもの"
                #print last_array
                #array_count+=1
            else:#)がある
                #print "）ある"
                end_count=xx.count(")")
                #print "くっつけるもの"
                #print last_array
                #print ")の数"
                #print end_count
                #print "配列の深さ？"
                #print array_count
                up_array=s_array
                #ループの条件がおかしいと思う
                #print "配列の深さー)の数"
                #print array_count-end_count
                jj=array_count-end_count
                j=1
                if j<jj:
                    array_count=1
                    while j<jj:
                        #print"ループ-----------"
                        #print "j: "+str(j)
                        #print "jj: "+str(jj)
                        #print up_array
                        up_array=up_array[len(up_array)-1]
                        #print up_array
                        array_count+=1
                        #print array_count
                        j+=1
                else:
                    array_count=1
                #これじゃぜったいだめ
                #print "ループ後配列の深さ"

                #print array_count
                last_array=up_array
                #print last_array
                #print"配列かうんと"
                #print array_count
                #print"last"
                #print last_array
            #print s_array
            #last_array=new_array
            #print"---------------------------------------------------"
            # print array_count
            #print"s_array"
            #print s_array

        #print s_array
        i+=1
    return s_array

def to_subtree(array,s):
    #print array
    s.append(array)
    #print array
    #print s_set
    i=1
    while i<len(array):
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            s = to_subtree(x,s)
            #print x


        i+=1

    return s

def subtree_calculation(list_1,list_2,LAMDA):
    hukasa_max = 0
    value=0
    for i in list_1:
        for j in list_2:
            if i==j:
                #print("一致")
                depth_search(i,0,hukasa_max)
                #print deep
                #hukasa_max=0
                #print "-------------------"
                deep=hukasa_max-1
                #print deep
                hukasa_max=0
                #print "-------------------"
                #print sys.setrecursionlimit(st_1)
                #print st_1
                #print st_2
                value+=1*(LAMDA**deep)


    return value

def depth_search(array,hukasa,hukasa_max):
    hukasa+=1
    #print hukasa

    i=1

    while i<len(array):
        #print array[i]
        new_hukasa=depth_search(array[i],hukasa,hukasa_max)
        if hukasa_max<new_hukasa:
            hukasa_max=new_hukasa

        if hukasa_max<hukasa:
            hukasa_max=hukasa
        i+=1
    return hukasa

if __name__ == '__main__':
    s1 = "(A (B C))"
    s2 = "(A (B C))"
    subtree_kernel(s1,s2,1)
