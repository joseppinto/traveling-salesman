import pandas as pd 
import sys
import seaborn as sns
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Indicar ficheiro de input!!")
    sys.exit(0)

data = pd.read_csv(sys.argv[1])

data2 = data

plot = sns.relplot(x="area", y="perimeter", data=data2,hue="version", kind="line", col="shape")
plot.set(xscale="log", yscale="log")
plt.show()

plot = sns.relplot(x="n_nodes", y="time", data=data2, hue="version", kind="line")
plot.set(xscale="log", yscale="log")
plt.show()