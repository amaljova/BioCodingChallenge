
def locFind(target_seq,query_seq):
    start, end = 0, len(query_seq)
    result = []
    for i in range(len(target_seq)):
        if target_seq[start:end] == query_seq:
            result.append(str(start+1))
        start, end = start+1, end+1
    return result

def patternFinder(infile):
    with open(infile, 'r') as f:
        lines = f.readlines()
    collection = []
    num = len(lines)
    for i in range(1,num,2):
        s = lines[i].replace('\n','')
        t = lines[i+1].replace('\n','')
        collection.append(locFind(s,t))
    return collection

def writer(infile, outfile):
    a = patternFinder(infile)
    a = '\n'.join([" ".join(item) for item in a])
    print(a)

    with open(outfile,'w',encoding = 'utf-8') as f:
            f.write(a)
    
writer("input.txt", "output.txt")