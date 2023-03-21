import sys
import tracemalloc

polydict = dict()

def read_polimorf():
    polydict = dict()
    with open('polimorf/polimorf-20180722.tab',"r") as file:
        while True:
            line = file.readline()
            if not line or line.startswith('#</'):
                break
        counter = 0
        chnunk_size = 1000000
        while True:
            line = file.readline()
            if not line:
                break
            counter+=1
            if counter > chnunk_size:
                formatted_float = "{:.2f}".format(tracemalloc.get_traced_memory()[0] / 1024 ** 3)
                print(formatted_float, 'GB')
                counter = 0
            parts = line.strip().split('\t')
            el = parts[1]+';'+parts[2]
            if not parts[0] in polydict:
                polydict[parts[0]] = list()
            polydict[parts[0]].append(el)
    formatted_float = "{:.2f}".format(tracemalloc.get_traced_memory()[0] / 1024 ** 3)
    print(formatted_float, 'GB')
    return polydict


def out_word(word):
    print(word)
    if word in polydict:
        list = polydict[word]
        for l in list:
            print(l)

def analyze_line(line):
    print(line)
    word=''
    for ch in line:
        if ch.isalpha():
            word += ch
        else:
            if len(word) > 0:
                out_word(word)
                word = ''
    if len(word) > 0:
        out_word(word)
    print()

def analyze_sample(sample):
    with open(sample, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            analyze_line(line.strip())


tracemalloc.start()
polydict = read_polimorf()
tracemalloc.stop()

analyze_sample("input/sample1.txt")

