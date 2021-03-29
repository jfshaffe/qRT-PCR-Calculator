# qRT-PCR-Calculator
Calculates Fold Change and Log2 Fold Change using raw Ct/Cq values (three technical replicates each condition) using delta delta Ct method
DIRECTIONS ON HOW TO USE:
1. Open this website: https://www.onlinegdb.com/online_python_compiler   (it's a free secure online Python IDE/Internal Development Environment like PyCharm except it's online)
2.  Copy the qRT-PCR Calculator Python code (qRT-PCR Fold Change & log2fc Calculator by Joshua Shaffer .py) that I wrote and paste it into the top panel of the website 
3.  Click the green play (triangle) button that says 'Run'
4.  In the bottom panel it will prompt you to enter a Cq/Ct value where there is a cursor flashing next to the description of which value to enter
5.  Enter the value then press enter on your keyboard
6.  Enter the next Cq/Ct value it prompts you to enter and then press enter
7.  Keep doing this until all 9 values are entered and after pressing enter for the 9th value it will show the fold change and log2fc at the bottom
8.  Copy and paste everything in the bottom panel of the website (especially the fold change and log2fc values) into Excel 
#EXPLANATION BELOW ABOUT WHERE TO PUT WHICH CQ/CT VALUES 
#Say for example we are querying the expression of _MAL12_ mRNA (encodes a maltase enzyme for breaking down maltose) in yeast (_Saccharomyces cerevisiae_) grown in maltose rich media (YPM aka yeast extract peptone maltose) versus yeast grown in glucose rich media (YPD aka yeast extract peptone dextrose). The experimental group would be the yeast grown in maltose rich media whereas the control group would be the yeast grown in glucose rich media. The experimental gene would be _MAL12_ whereas the housekeeping gene would be a gene that would not be expected to change in expression between the two groups and that is known to be expressed at steady levels such as _GAPDH_ or _B-actin_
