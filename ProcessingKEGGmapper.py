# I need to produce a new KEGG mapper filer that will:
# 1. add compounds not detected from the sample (green if in both or yellow if not)
# 2. remove KOs originating from the food genomes 
# only origins should be microbial (blue), dietary (yellow), or both (green)

# get KEGG_mapper file
km = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/org/kegg_mapper.tsv'

# turn KEGG mapper file into dict 
mapper = {}
f = open(km, 'r')
for line in f: 
    line = line.split('\t')
    mapper[line[0]] = line[1]
f.close()

# for each key 
keys_to_remove = []
for key in mapper.keys():
    # this checks for key as first line is empty 
    if len(key) > 0:
        # make sure that it is a KO
        if key[0] == 'K':
            # if diet KO add to remove list 
            if mapper[key] == 'yellow\n':
                keys_to_remove.append(key)
            # if KO could come from both make microbe
            if mapper[key] == 'green\n':
                mapper[key] = 'blue\n'
        # check if compound 
        elif key[0] == 'C':
            # re-maps detected compounds(metabolome)
            # orange = metabolome = diet 
            # if yellow or undetected = yellow 
            # if blue(microbes) or green(both) = green(both)
            if mapper[key] == 'yellow,orange\n':
                mapper[key] = 'yellow\n'
            elif mapper[key] == 'blue,orange\n':
                mapper[key] = 'green\n'
            elif mapper[key] == ',orange\n':
                mapper[key] = 'yellow\n'
            elif mapper[key] == 'green,orange\n':
                mapper[key] = 'green\n'

# remove keys to remove 
for key in keys_to_remove:
    mapper.pop(key)

# sanity checks 
for key in mapper.keys():
    if len(key) > 0:
        if key[0] == 'K':
            if mapper[key] != 'blue\n':
                print ('KO detected that is not blue')
        elif key[0] == 'C':
            if mapper[key] == 'yellow\n' or mapper[key] == 'green\n' or mapper[key] == 'blue\n':
                pass
            else:
                print('compound is not correctly labeled')

# write to a new kegg mapper file 
nKM = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/org/new_kegg_mapper.tsv'
f = open(nKM, 'w')
for key in mapper.keys():
    line = key + '\t' + mapper[key]
    f.write(line)
f.close()
