def split_to_pos():
    sub_pos = ['adj', 'adja', 'adjc', 'adjp', 'adv', 'aglt', 'bedzie', 'brev', 'comp',
               'cond', 'conj', 'depr', 'fin', 'frag', 'ger', 'imps', 'impt', 'inf', 'interj',
               'num', 'numcomp', 'pact', 'pacta', 'pant', 'part', 'pcon', 'ppas',
               'ppron12', 'ppron3', 'praet', 'pred', 'prep', 'subst', 'winien']

    fdict = dict()
    for i in range(0, len(sub_pos)):
        f = open('gen/'+sub_pos[i]+'.tab', 'w')
        fdict[sub_pos[i]] = f
    file = open('input/polimorf-20180722.tab', 'r')
    while True:
        line = file.readline()
        if line.startswith('#</'):
            break

    counter = 0
    while True:
        line = file.readline()
        if not line:
            break
        counter+=1
        if counter % 1000000 == 0:
            print(".",end='')
        parts = line.split('\t')
        sub_pos = parts[2].split(':')[0]
        fdict[sub_pos].write(line)
    file.close()
    for el in fdict:
        fdict[el].close()


# other forms infnitive verb
def form_inf():
    dic = dict()
    with open('gen/inf.tab', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            parts = line.strip().split('\t')
            if parts[0]!=parts[1]:
                dic[parts[0]] = parts[1]
    li = list()
    for el in dic.keys():
        print(el, dic[el], sep=';')

# split_to_pos()
form_inf()
