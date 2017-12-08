import matplotlib
print("test anastasia")
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks(([1, 2, 3], ["Juku", "Kati", "Mati"])
plt.savefig("anastasia1.png")
plt.clf()
