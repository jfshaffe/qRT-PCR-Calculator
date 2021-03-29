#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#written by Joshua Shaffer (jfshaffe@ucsc.edu)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
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




