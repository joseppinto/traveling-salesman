import pandas as pd 
import sys
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Indicar ficheiro de input!!")
    sys.exit(0)

data = pd.read_csv(sys.argv[1])
dict = {'n_nodes': [], 'n_reps': [], 'version': [], 'perimeter': [], 'time': [], 'area':[], 'shape': []}

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
    dict['version'].append('greedyK')
    dict['perimeter'].append(row[2])
    dict['perimeter'].append(row[3])
    dict['perimeter'].append(row[4])
    dict['perimeter'].append(row[5])
    dict['time'].append(row[6])
    dict['time'].append(row[7])
    dict['time'].append(row[8])
    dict['time'].append(row[9])
    dict['area'].append(row[10])
    dict['area'].append(row[10])
    dict['area'].append(row[10])
    dict['area'].append(row[10])
    if row[11][1:] == 'True':
        shape = 'circle' 
    else:
        shape = 'square'
    dict['shape'].append(shape)
    dict['shape'].append(shape)
    dict['shape'].append(shape)
    dict['shape'].append(shape)
    

data = pd.DataFrame(dict)
data.to_csv("tests.csv")
data2 = data


plot = sns.relplot(x="area", y="perimeter", data=data2,hue="version", kind="line", col="shape")
plot.set(xscale="log", yscale="log")
plt.show()

plot = sns.relplot(x="n_nodes", y="time", data=data2, hue="version", kind="line")
plot.set(xscale="log", yscale="log")
plt.show()