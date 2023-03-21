import sys
import tracemalloc


def read_polimorf():
    polydict = dict()
    with open('polimorf/polimorf-20180722.tab',"r") as file:
        counter = 0
        limit = 1000000
        while True:
            line = file.readline()
            if not line:
                break
            counter+=1
            if counter>limit:
                formatted_float = "{:.2f}".format(tracemalloc.get_traced_memory()[0] / 1024 ** 3)
                print(formatted_float, 'GB')
                counter = 0
            parts = line.strip().split('\t')
            el= line
            if not parts[0] in polydict:
                polydict[parts[0]] = list()
            polydict[parts[0]].append(el)
    formatted_float = "{:.2f}".format(tracemalloc.get_traced_memory()[0] / 1024 ** 3)
    print(formatted_float, 'GB')


tracemalloc.start()
read_polimorf()

tracemalloc.stop()

