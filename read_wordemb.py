import numpy as np

lines_num, dim = 0, 0
vectors = {}
iw = []
wi = {}
with open('../emb_word', errors='ignore') as f:
    first_line = True
    for line in f:
        if first_line:
            first_line = False
            dim = int(line.rstrip().split()[1])
            continue

        lines_num += 1
        tokens = line.rstrip().split(' ')
        vectors[tokens[0]] = np.asarray([float(x) for x in tokens[1:]])
        iw.append(tokens[0])
        if lines_num >= topn:
            break

    for i, w in enumerate(iw):
        wi[w] = i
