#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#written by Joshua Shaffer (jfshaffe@ucsc.edu)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
def main():
    gene_types = ('experimental', 'housekeeping')
    inputs = {
        'experimental': {},
        'control': {}
    }
    for group in inputs.keys():
        for gene_type in gene_types:
            inputs[group][gene_type] = []
            for i in range(1,4):
                x = input("{} group technical replicate {} {} gene Cq/Ct value: ".format(group, i, gene_type))
                inputs[group][gene_type].append(float(x))
    te = sum(inputs['experimental']['experimental'])/3
    he = sum(inputs['experimental']['housekeeping'])/3
    tc = sum(inputs['control']['experimental'])/3
    hc = sum(inputs['control']['housekeeping'])/3
    deltaCtE = te - he
    deltaCtC = tc - hc
    deltadeltaCt = deltaCtE - deltaCtC
    fc = 2**(-deltadeltaCt)
    log2fc = math.log(fc,2)
    print("fold change = ", fc)
    print("log2 fold change = ", log2fc)
main()






# In[ ]:




