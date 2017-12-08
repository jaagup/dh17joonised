import matplotlib
print("test kristina")
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.bar ([1, 2, 3], [170, 160, 150])
plt.xticks ([1, 2, 3],["Juku", "Kati", "Mati"])
plt.savefig("kristina1.png")
plt.clf()