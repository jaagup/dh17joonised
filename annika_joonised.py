import matplotlib
print("Tere, mina olen Annika!")
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3], ["Juku", "Kati", "Mati"])
plt.savefig("annika1.png")
plt.clf()

plt.scatter([70, 60, 65],[170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
plt.savefig("annika2.png")
plt.clf()