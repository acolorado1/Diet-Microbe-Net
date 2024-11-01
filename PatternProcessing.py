import json
import pandas as pd

ag_OrgFoo = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/org_foo/Neo4j/patterns.json'
ag_Org = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/org/Neo4j/patterns.json' 
ag_foo = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/foo/Neo4j/patterns.json' 

def GetPatterns (f:str):
    # open pattern file 
    with open(f, 'r') as file:
        data = json.load(file)
    file.close()

    # remove water from reactions 
    data = [item for item in data if item['p']['start']['properties']['id'] != 'C00001']

    # get a list of all KOs and reactions 
    KOs = []
    rxns = []
    for item in range(len(data)):
        ko = data[item]['p']['segments'][0]['relationship']['properties']['KOs'].split(',')
        rxn = data[item]['p']['segments'][0]['relationship']['properties']['Reaction'].split(',')
        KOs += ko
        rxns += rxn

    return (KOs, rxns)

OF_ko, OF_r = GetPatterns(ag_OrgFoo)
print("Done with Org Foo")
O_ko, O_r = GetPatterns(ag_Org)
print("Done with Org")
F_ko, F_r = GetPatterns(ag_foo)
print("Done with Foo")

shared_KOs = list(set(OF_ko) & set(O_ko) & set(F_ko))
print('shared KOs: ', shared_KOs)
print('shared KOs count: '+str(len(shared_KOs)))

# export gene list 
genelist = '/Users/burkhang/Code_Projs/Diet-Microbe-Net/AMON_Western/genelist.txt'
f = open(genelist, 'w')
for item in range(len(shared_KOs)):
    f.write('gene' + str(item) + ' ' + shared_KOs[item]+'\n')
f.close()

ag = ['K07009', 'K13818', 'K01775', 'K02231', 'K15792', 'K02778', 'K01798', 'K02233', 'K21344', 'K06920', 'K02804', 'K09882', 'K25814', 'K02588', 'K19405', 'K15372', 'K02779', 'K05780', 'K00880', 'K00806', 'K06166', 'K19697', 'K09001', 'K19712', 'K02586', 'K00874', 'K06864', 'K01921', 'K00531', 'K09758', 'K00881', 'K03367', 'K00566', 'K13930', 'K19726', 'K00929', 'K03272', 'K00005', 'K08693', 'K03752', 'K01924', 'K01843', 'K02591', 'K23144', 'K19709', 'K01034', 'K01779', 'K02795', 'K02227', 'K04075', 'K01902', 'K00932', 'K00973', 'K13059', 'K01925', 'K03800', 'K23756', 'K13927', 'K01912', 'K02230', 'K06165', 'K05966', 'K04343', 'K02810', 'K08722', 'K02232', 'K02794', 'K00925', 'K01928', 'K10710', 'K06164', 'K23393', 'K24707', 'K02224', 'K01739', 'K21345', 'K01910', 'K18126', 'K12570', 'K20118', 'K02777', 'K00883', 'K00848', 'K13571', 'K01903', 'K02791', 'K07031', 'K14188', 'K02796', 'K00853', 'K01026', 'K01589', 'K02225', 'K01929', 'K02793', 'K01035', 'K09883']

we = ['K14268', 'K03752', 'K04075', 'K02779', 'K08693', 'K00929', 'K01460', 'K03707', 'K03365', 'K17104', 'K02810', 'K15888', 'K08722', 'K02362', 'K07806', 'K02791', 'K09024', 'K00973', 'K00925', 'K01833', 'K01739', 'K02777', 'K19665', 'K18931', 'K01798', 'K00836', 'K00806', 'K15922', 'K03800', 'K02363', 'K00932', 'K01924', 'K08968', 'K00117', 'K19697', 'K16181', 'K01582', 'K07250', 'K00832', 'K00005', 'K09470', 'K02778', 'K02364', 'K02231', 'K20118', 'K01775', 'K01252', 'K00673', 'K17488', 'K19712', 'K00877', 'K19726', 'K13818', 'K13069', 'K17105', 'K01026', 'K15785', 'K02488', 'K01917', 'K09018', 'K23144', 'K01843', 'K01485']

print(list(set(ag) & set(we)))

print(len(list(set(ag) & set(we))))

['K01775', 'K01843', 'K02779', 'K00005', 'K03800', 'K19726', 'K19712', 'K00973', 'K02810', 'K00929', 'K02777', 'K08693', 'K20118', 'K04075', 'K02791', 'K01924', 'K01026', 'K23144', 'K01798', 'K02231', 'K01739', 'K00932', 'K19697', 'K00806', 'K00925', 'K02778', 'K13818', 'K03752', 'K08722']