def read_dat(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    s = set()
    for line in lines:
        s.add(line.strip())
    return s


def print_prefixes():
    std_prefixes = read_dat("data/std_prefixes.dat")
    prefd = dict()
    with open("data/no_prefix.csv") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            parts = line.split(';')
            prefix = parts[0][:len(parts[0])-len(parts[1])]
            if len(prefix) > 0 and prefix not in std_prefixes:
                if prefix in prefd:
                    prefd[prefix].append(line)
                else:
                    items = list()
                    items.append(line)
                    prefd[prefix] = items
    preflist = list(prefd)
    preflist.sort()
    for prefix in preflist:
        print(prefix)


def check_lack_ambig():
    pass

print_prefixes()
