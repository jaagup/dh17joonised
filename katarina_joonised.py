import matplotlib
print("test katarina")
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3], ["Juku", "Kati", "Mati"])
plt.savefig("katarina1.png")
plt.clf()