import sys 
import re

# Se nao tiver os argumentos dos ficheiros termina
if len(sys.argv) < 3:
    print("Erro, poucos argumentos")
    sys.exit(0)

# Nomes das colunas onde vamos organizar o output
cols = ['n_nodes', 'n_reps', 'sim_an', 'monte_carlo', 'greedy', 'sim_an_t', 'monte_carlo_t', 'greedy_t']

# Abrir o ficehiro csv para escrever
out = open(sys.argv[2], 'w')
# Imprimir o cabeçalho do csv
for c in cols:
    if not c is 'greedy_t':
        print(c + ", ", end="", file = out)
    else:
        print( c + "\n", end="", file= out )

# Ler as linhas do ficheiro produzido pelo matlab
f = open(sys.argv[1], 'r')
# Booleano para ver se estamos a fazer parse das medições do tempo
time_flag = False
count = 0
multiplier = 0
dict = {}
for c in cols:
    dict[c] = 0
for line in f:
    if re.match('tempos' , line):
        time_flag = True 
    elif re.match( '[0-9]+, [0-9]+\n', line):
        # Início de uma nova execução da main do matlab
        dict['n_nodes'] = int(line.split(', ')[0])
        dict['n_reps'] = int(line.split(', ')[1])
        count = 0
        multiplier = 1.0
    elif re.match( '\s+1\.0e\+\d+\s+\*', line):
        # Linha com multiplicador 
        multiplier = float(line.split('*')[0])
    elif re.match('\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+', line):
        if time_flag:
             # Extrair os tempos da linha e multiplicar pelo multiplicador
             l = [multiplier * float(a) for a in line.split()]
            dict[cols[5]] += l[0]
            dict[cols[6]] += l[1]
            dict[cols[7]] += l[2]
            count += 1
            if count is dict['n_reps']:
                for i in range(2, 8):
                    dict[cols[i]] /= count
                for c in cols:
                    if not c is 'greedy_t':
                        string = str(dict[c]) + ', '
                    else: 
                        string = str(dict[c]) + "\n"
                    print(string, end="", file=out)
                    dict[c] = 0
                count = 0
                time_flag = False
        else:
            # Extrair os resultados da linha e multiplicar pelo multiplicador
            l = [multiplier * float(a) for a in line.split()]
            dict[cols[2]] += l[0]
            dict[cols[3]] += l[1]
            dict[cols[4]] += l[2]
            count += 1
            if count is dict['n_reps']:
                count = 0
                multiplier = 1

f.close()
out.close()

