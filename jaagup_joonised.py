import matplotlib
import pandas as pd
print("test jaagup")
matplotlib.use("Agg") #Et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3],["Juku", "Kati", "Mati"])
plt.savefig("jaagup1.png")
plt.clf() #puhastab joonise loomise tahvli

fig, ax=plt.subplots() #teksti jaoks eraldi kiht
plt.scatter([70, 60, 65], [170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
ax.annotate("Kati", (60, 160))
plt.savefig("jaagup2.png")
plt.clf()

lapsed=pd.read_csv("http://www.tlu.ee/~jaagup/andmed/muu/5klass.txt")
plt.hist(lapsed.pikkus)
plt.savefig("jaagup3.png")
plt.clf()