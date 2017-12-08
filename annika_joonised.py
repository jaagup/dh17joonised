import matplotlib
import pandas as pd
print("Tere, mina olen Annika!!")
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3], ["Juku", "Kati", "Mati"])
plt.savefig("annika1.png")
plt.clf()

fig, ax=plt.subplots()
plt.scatter([70, 60, 65],[170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
ax.annotate ("Kati", (60, 160))
plt.savefig("annika2.png")
plt.clf()

lapsed=pd.read_csv("http://www.tlu.ee/~jaagup/andmed/muu/5klass.txt")
plt.hist(lapsed.pikkus)
plt.savefig("annika3.png")
plt.clf