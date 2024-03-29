from __future__ import print_function
import sys 
import re

# Se nao tiver os argumentos dos ficheiros termina
if len(sys.argv) < 3:
    print("Erro, poucos argumentos")
    sys.exit(0)

# Nomes das colunas onde vamos organizar o output
cols = ['n_nodes', 'n_reps', 'sim_an', 'monte_carlo', 'greedy', 'greedyK', 'sim_an_t', 'monte_carlo_t', 'greedy_t', 'greedyK_t', 'area', 'circle']

# Abrir o ficehiro csv para escrever
out = open(sys.argv[2], 'w')
# Imprimir o cabecalho do csv
for c in cols:
    if not c is 'circle':
        print(c + ", ", end="", file =out)
    else:
        print( c + "\n", end="", file=out)

# Ler as linhas do ficheiro produzido pelo matlab
f = open(sys.argv[1], 'r')
# Booleano para ver se estamos a fazer parse das medicoes do tempo
time_flag = False
count = 0
multiplier = 1
dict = {}
for c in cols:
    if c in ['greedyK', 'greedy', 'sim_an', 'monte_carlo', 'sim_an_t', 'monte_carlo_t', 'greedy_t', 'greedyK_t']:
        dict[c] = sys.float_info.max
    else:
        dict[c] = 0
for line in f:
    if re.match('tempos' , line):
        time_flag = True 
    elif re.match( '[0-9]+, [0-9]+, [0-9]+, (true|false)\n', line):
        # Inicio de uma nova execucao da main do matlab
        dict['n_nodes'] = int(line.split(', ')[0])
        dict['n_reps'] = int(line.split(', ')[1])
        dict['area'] = int(line.split(', ')[2])
        dict['circle'] = ('true' in line.split(', ')[3])
        count = 0
        multiplier = 1.0
    elif re.match( '\s+1\.0e\+\d+\s+\*', line):
        # Linha com multiplicador 
        multiplier = float(line.split('*')[0])
    elif re.match('\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+', line):
        if time_flag:
            # Extrair os tempos da linha e multiplicar pelo multiplicador
            l = [multiplier * float(a) for a in line.split()]
            dict[cols[6]] = l[0]/dict['n_reps']
            dict[cols[7]] = l[1]/dict['n_reps']
            dict[cols[8]] = l[2]/dict['n_reps']
            dict[cols[9]] = l[3]/dict['n_reps']
            count += 1
            if count is dict['n_reps']:
                for c in cols:
                    if not c is 'circle':
                        string = str(dict[c]) + ', '
                    else: 
                        string = str(dict[c]) + "\n"
                    print(string, end="", file=out)
                    if c in ['greedyK', 'greedy', 'sim_an', 'monte_carlo', 'sim_an_t', 'monte_carlo_t', 'greedy_t', 'greedyK_t']:
                        dict[c] = sys.float_info.max
                    else:
                        dict[c] = 0
                count = 0
                time_flag = False
                multiplier = 1
        else:
            # Extrair os resultados da linha e multiplicar pelo multiplicador
            l = [multiplier * float(a) for a in line.split()]
            dict[cols[2]] = l[0]/dict['n_reps']
            dict[cols[3]] = l[1]/dict['n_reps']
            dict[cols[4]] = l[2]/dict['n_reps']
            dict[cols[5]] = l[3]/dict['n_reps']
            count += 1
            if count is dict['n_reps']:
                count = 0
                multiplier = 1

f.close()
out.close()

