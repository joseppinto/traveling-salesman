import re
import sys

input = "sample.txt"
output = "output.csv"

if len(sys.argv) == 3:
    input = sys.argv[1]
    output = sys.argv[2]
elif len(sys.argv) == 2:
    input = sys.argv[1]

with open(input, "r",encoding="utf-8") as ficheiro:
    linhas = ficheiro.read()
    regex = r'(\d+), (\d+)[\n\ ]*ans =[\n\ ]*(?:([0-9\.]*e\+\d+)\ \*[\n\ ]*)?((?:(?:\d+\.\d+)[\ \n]+)+)'
    dados = dict()
    for x in re.finditer( regex, linhas):
        (n_nodes, n_pross, not_cientifica, pre_valores ) = x.groups()
        if not_cientifica == None:
            not_cientifica = 1.0
        else:
            not_cientifica = float(not_cientifica)
        valores = dict()
        for pre_linha in pre_valores.split('\n'):
            index = 0
            for pre_valor in re.split('\ *', pre_linha,3):
                if pre_valor != '':
                    valor_aux = float(pre_valor) * not_cientifica
                    valor_dict = valores.get(index, None)
                    if valor_dict == None or valor_dict > valor_aux:
                        valores[index] = valor_aux 
                    index+=1
        dados.setdefault(n_nodes,[]).append((n_pross, valores))
with open(output,"w+") as output:
    for (n_nodes, valores) in dados.items():
        output.write(str(n_nodes) + '\n')
        for (n_processos, minimos) in valores:
            output.write(str(n_processos) + ';')
            for minimo in minimos.values():
                output.write(str(minimo) + ';')
            output.write('\n')
        output.write('\n')
