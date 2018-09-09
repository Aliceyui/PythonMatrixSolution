import pandas as pd
import numpy as np

path="C:/Users/jenny/OneDrive/Desktop/testcode/basket/cat_data.csv"
data=pd.read_csv(path,encoding='utf-8')

pv=pd.pivot_table(data,index=['posno'], values=['Category'], aggfunc=pd.Series.nunique)
pv.to_csv('C:/Users/jenny/OneDrive/Desktop/testcode/basket/piv_result.csv')

path2="C:/Users/jenny/OneDrive/Desktop/testcode/basket/piv_result.csv"
data2=pd.read_csv(path2,encoding='utf-8')


data.insert(2, 'Category_Count', data['posno'].map(data2.set_index('posno')['Category']))
data.insert(4,'posno2',data['posno'])
# df1.insert(2, 'MAKE', df1['MODEL'].map(df2.set_index('MODEL')['MAKE']))

piv2=pd.pivot_table(data[data.Category_Count>1], index=['posno'], columns=['Cat Order'], values=['posno2'], aggfunc=pd.Series.nunique)

piv2.columns = piv2.columns.droplevel(0)

piv3=piv2.reindex(piv2.sum().sort_values(ascending=False).index, axis=1)


# piv3.to_csv('C:/Users/jenny/OneDrive/Desktop/testcode/basket/cat_result.csv')

# path3="C:/Users/jenny/OneDrive/Desktop/testcode/basket/cat_result.csv"
# aqicsv=pd.read_csv(path3,encoding='utf-8')
#
aqicsv=piv3

list1=aqicsv.columns[0:37]
list2=aqicsv.columns[0:26260]

with open('C:/Users/jenny/OneDrive/Desktop/testcode/basket/finalresult.csv', 'w', newline='') as f:
    f.write(""+",")

    for row1 in list1:
        f.write(row1+",")  #write header

    f.write("\n")  #next line

    for row1 in list2:
        f.write(row1+",")   #first column for every row
        for row2 in list1:
            x=str(len(aqicsv[(aqicsv[row1] == 1) & (aqicsv[row2] == 1)]))+","   ##count the rows with both row1 and row2
            f.write(x)
        f.write("\n")  #next row
