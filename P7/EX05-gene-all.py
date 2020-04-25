import http.client
import json
import termcolor
from Seq1 import Seq


GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

BASES = ['A', 'C', 'T', 'G']

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'

for name in GENES:
    REQ = ENDPOINT + GENES[name] + PARAMS
    URL = SERVER + REQ

    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQ)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}")
    data1 = r1.read().decode()
    gene = json.loads(data1)

    termcolor.cprint("Gene", 'green', end="")
    print(f": {name}")
    termcolor.cprint("Description", 'green', end="")
    print(f": {gene['desc']}")

    genestr = gene['seq']
    s = Seq(genestr)

    length = s.len()
    termcolor.cprint("Total length", 'green', end="")
    print(f": {length}")

    for e in BASES:
        count = s.count_base(e)
        percentage = round(s.count_base(e) * (100 / s.len()), 2)
        termcolor.cprint(f"{e}", 'blue', end="")
        print(f": {count} ({percentage}%)")

    dictionary = s.count()
    list_values = list(dictionary.values())
    max_base = max(list_values)

    termcolor.cprint("Most frequent base", 'green', end="")
    print(f": {BASES[list_values.index(max_base)]}")
    print()
    print()
