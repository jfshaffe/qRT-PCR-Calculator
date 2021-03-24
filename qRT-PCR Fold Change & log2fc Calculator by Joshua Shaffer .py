#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#written by Joshua Shaffer (jfshaffe@ucsc.edu)
#DIRECTIONS ON HOW TO USE:
#in pycharm press Run then press Run 'main', enter Cq/Ct values (press enter after each entry),
#then press enter to get output
#below are tested values with a known output
#Example is RNase9 expression in knockout caput relative to RNase9 expression in wildtype caput
#Experimental group would be knockout caput, control group would be wildtype caput
#Experimental gene would be RNase9, housekeeping gene would be B-actin
#experimental group technical replicate 1 experimental gene Cq/Ct value: 32.59
#experimental group technical replicate 3 experimental gene Cq/Ct value: 32.5
#experimental group technical replicate 2 experimental gene Cq/Ct value: 32
#experimental group technical replicate 1 housekeeping gene Cq/Ct value: 20.37
#experimental group technical replicate 2 housekeeping gene Cq/Ct value: 20.39
#experimental group technical replicate 3 housekeeping gene Cq/Ct value: 19.73
#control group technical replicate 1 experimental gene Cq/Ct value: 15.34
#control group technical replicate 2 experimental gene Cq/Ct value: 15.33
#control group technical replicate 3 experimental gene Cq/Ct value: 16.18
#control group technical replicate 1 housekeeping gene Cq/Ct value: 19.81
#control group technical replicate 2 housekeeping gene Cq/Ct value: 20.04
#control group technical replicate 3 housekeeping gene Cq/Ct value: 20.43
#Expected output printed below inputs
#fold change =  9.546036830854443e-06
#log2 fold change =  -16.676666666666662

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
class QRTPCR (float):
    def __init__(self, d):
        self.d=d
    #def foldchange(self):
        #return 2**(-self.d)
def main():
    data0 = input("experimental group technical replicate 1 experimental gene Cq/Ct value: ")
    data1 = input("experimental group technical replicate 2 experimental gene Cq/Ct value: ")
    data2 = input("experimental group technical replicate 3 experimental gene Cq/Ct value: ")
    data3 = input("experimental group technical replicate 1 housekeeping gene Cq/Ct value: ")
    data4 = input("experimental group technical replicate 2 housekeeping gene Cq/Ct value: ")
    data5 = input("experimental group technical replicate 3 housekeeping gene Cq/Ct value: ")
    data6 = input("control group technical replicate 1 experimental gene Cq/Ct value: ")
    data7 = input("control group technical replicate 2 experimental gene Cq/Ct value: ")
    data8 = input("control group technical replicate 3 experimental gene Cq/Ct value: ")
    data9 = input("control group technical replicate 1 housekeeping gene Cq/Ct value: ")
    data10 = input("control group technical replicate 2 housekeeping gene Cq/Ct value: ")
    data11 = input("control group technical replicate 3 housekeeping gene Cq/Ct value: ")
    dataA = float(data0)
    dataB = float(data1)
    dataC = float(data2)
    dataD = float(data3)
    dataE = float(data4)
    dataF = float(data5)
    dataG = float(data6)
    dataH = float(data7)
    dataI = float(data8)
    dataJ = float(data9)
    dataK = float(data10)
    dataL = float(data11)
    te = ((dataA+dataB+dataC))/3
    he = ((dataD+dataE+dataF))/3
    tc = ((dataG+dataH+dataI))/3
    hc = ((dataJ+dataK+dataL))/3
    deltaCtE = te - he
    deltaCtC = tc - hc
    deltadeltaCt = deltaCtE - deltaCtC
    fc = 2**(-deltadeltaCt)
    log2fc = math.log(fc,2)
    print("fold change = ", fc)
    print("log2 fold change = ", log2fc)
main()






# In[ ]:




