# -*- coding: utf-8 -*-
"""
@author: Amal Joseph Varghese
@email: amaljova@gmail.com

"""


def readBlock(block_data):
    Mi=[]
    for i in block_data[1].replace('\n', '').replace('  ', ' ').split(' '):
        try:
            Mi.append(float(i))
        except:
             pass

    Ai=[]
    for i in block_data[2].replace('\n', '').replace('  ', ' ').split(' '):
        try:
            Ai.append(float(i))
        except:
             pass
    
    #Mi = [round(float(i), 6) for i in block_data[1].replace('\n', '').split(' ')]
    #Ai = [round(float(i), 6) for i in block_data[2].replace('\n', '').split(' ')]
    
    #Si = Mj + Ak + delt given that Mj + Ak > 0
    tem_dict = dict()
    for i in Mi:
        for j in Ai:
            a = round(i+j, 6)
            if a > 0:      # satisfy Mj + Ak > 0 condition
                tem_dict[(Mi.index(i)+1, Ai.index(j)+1)] = a
    print('done: summed')
    return (tem_dict)
    #return (M_number, K_number, N_number, Mi, Ai, Si)


def getSi(block_data):
    Si=[]
    for i in block_data[3].replace('\n', '').replace('  ', ' ').split(' '):
        try:
            Si.append(float(i))
        except:
             pass
    #Si = [round(float(i), 6) for i in block_data[3].replace('\n', '').split(' ')]
    return Si


def findDelta(tem_dict, Si):
    del_list = []
    dict_delta = dict()
    for signal in Si:
        for item in tem_dict:
            dict_delta[item] = abs(round(signal - tem_dict[item], 6))
        del_list.append(min(dict_delta, key= dict_delta.get))
    print('done! delta found')
    return del_list


def run(in_file):
    #open file to read data
    with open(in_file, "r") as f:
        data = f.readlines()

    T_cases = int(data[0]) # 0 line 
    readline = 1
    #blockwise operation
    out_data = []
    while(T_cases > 0):
        T_cases-=1
        tem_dict = readBlock(data[readline:readline+4])
        Si = getSi(data[readline:readline+4])
        out_data = out_data + findDelta(tem_dict, Si)
        readline = readline+4
        print(f'done! test case remining: {T_cases}')
    return out_data


def printer(out_data, out_file):
    giantSting = '' 
    for i in out_data:
        giantSting = giantSting + str(i[0]) + ' ' + str(i[1]) + '\n'
    with open(out_file,'w') as f:
        f.write(giantSting)
    print(f'data writtern to {out_file}')




#main
in_file = '1.txt'
out_file = '1_out.txt'
printer(run(in_file), out_file)
print('all done!')
