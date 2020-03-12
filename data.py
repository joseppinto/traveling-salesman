import pandas as pd 
import sys
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Indicar ficheiro de input!!")
    sys.exit(0)

data = pd.read_csv(sys.argv[1])
dict = {'n_nodes': [], 'n_reps': [], 'version': [], 'perimeter': [], 'time': []}

for i, row in data.iterrows():
    dict['n_nodes'].append(row[0])
    dict['n_nodes'].append(row[0])
    dict['n_nodes'].append(row[0])
    dict['n_nodes'].append(row[0])
    dict['n_reps'].append(row[1])
    dict['n_reps'].append(row[1])
    dict['n_reps'].append(row[1])
    dict['n_reps'].append(row[1])
    dict['version'].append('sim_an')
    dict['version'].append('monte_carlo')
    dict['version'].append('greedy')
    dict['version'].append('greedy2')
    dict['perimeter'].append(row[2])
    dict['perimeter'].append(row[3])
    dict['perimeter'].append(row[4])
    dict['perimeter'].append(row[5])
    dict['time'].append(row[6])
    dict['time'].append(row[7])
    dict['time'].append(row[8])
    dict['time'].append(row[9])

data = pd.DataFrame(dict)

plot = sns.relplot(x="n_nodes", y="perimeter", data=data, hue="version", col="n_reps", kind="line")
plt.show()

plot = sns.relplot(x="n_nodes", y="time", data=data, hue="version", col="n_reps", kind="line")
plt.show()