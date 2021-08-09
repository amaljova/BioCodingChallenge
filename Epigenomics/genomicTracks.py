# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@email: amaljova@gmail.com

"""



import pandas as pd

def myFunction(l_data):
    #make data frame
    l_data = pd.DataFrame(l_data)

    #making a list of srings whre each string is an entire column
    lines_trans = []
    for col in l_data.columns:
        list1 = ''.join(l_data[col])
        lines_trans.append(list1)

    #make dictionary
    dict1 = dict()
    num = 1
    for item in lines_trans:
        if item not in dict1.keys():
            dict1[item] = str(num)
            num = num+1
    #maping to dictionary and substitutions
    for key in dict1.keys():
        for e in lines_trans:
            if key == e:
                lines_trans[lines_trans.index(e)] = dict1[key]
    
    return (lines_trans, str(len(dict1)))

def extLineData(data, readline, num_lines):
    #extract needed data
    l_data = []
    for i in range(num_lines):
        for x in data[readline:readline+num_lines]:
            x = x.replace('\n', '')
            a = [i for i in x]
        #a = [i for i in data[readline:readline+num_lines].replace('\n', '')]
            l_data.append(a)
    return (l_data)

def readBlock(data, readline):
    #important numbers
    nub_lines_elements = data[readline].split(' ')
    num_lines, num_elements = int(nub_lines_elements[0]),int(nub_lines_elements[1])
    #extratiing data
    readline += 1 # 2 line
    b_data = extLineData(data, readline, num_lines)
    readline = readline+num_lines
    return (b_data, num_lines, num_elements, readline)


def doSomething(b_data):
    s = str(len(set(b_data[0])))
    a = b_data[0][0]
    result = []
    for item in b_data[0]:
        if item == a:
            result.append(str(1))
        else:
            result.append(str(2))
    return (result, s)

def run(in_file):
    #open file to read data
    with open(in_file, "r") as f:
        data = f.readlines()

    num_tests = int(data[0]) # 0 line 
    readline = 1
    #blockwise operation
    out_data = []
    while(num_tests > 0):
        num_tests-=1
        b_data, num_lines, num_elements, readline = readBlock(data, readline)
        if num_lines == 1:
            results, s = doSomething(b_data)
        else:
            results, s = myFunction(b_data)
        #results, s = myFunction(b_data)  
        out_data.append(s)
        results = ' '.join(results)
        out_data.append(results)
        
        
    out_data = '\n'.join(out_data)
    with open(out_file,'w') as f:
        f.write(out_data)
    return out_data


#main
in_file = '1.txt'
out_file = '1_out.txt'
run(in_file)
print('done!')

        