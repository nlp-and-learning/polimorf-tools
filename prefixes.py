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


def read_dict():
    prefd = dict()
    with open("data/no_prefix.csv") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line[0] == '#':
                continue
            line = line.strip()
            parts = line.split(';')
            left = parts[0]
            alt = list()
            for n in range(1, len(parts)):
                alt.append(parts[n])
            if left not in prefd:
                el = list()
                el.append(alt)
                prefd[left] = el
            else:
                prefd[left].append(alt)
    return prefd


def one_base_form(word, prefd):
    alts = prefd[word]
    if len(alts) != 1:
        return None
    alt = alts[0]
    return alt[0]


def is_in_any_alt(el, r, prefd):
    alts = prefd[el]
    for alt in alts:
        if alt[0] == r:
            return True
    return False


def correct_third_column():
    prefd = read_dict()
    for el in prefd.keys():
        alts = prefd[el]
        for alt in alts:
            need3 = False
            r0 = alt[0]
            if len(alt) > 1:
                r1 = alt[1]
            else:
                r1 = None

            if not r1 and r0 in prefd:
                r1 = one_base_form(r0, prefd)
                if r1 and r1 != r0:
                    print(el, r0, r1, sep=';')
                    need3 = True
            if not need3:
                if len(alt) > 1:
                    print(el, alt[0], alt[1], sep=';')
                else:
                    print(el, alt[0], sep=';')


correct_third_column()
