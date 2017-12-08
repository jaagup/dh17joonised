import matplotlib
import pandas as pd
print("Tere, Liisi!!")
matplotlib.use("Agg")  #et suudaks teksitekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3],[170, 160, 180])
plt.xticks([1, 2, 3],["juku", "kati", "mati"])
plt.savefig("liisi.png")
plt.clf() #puhastab joonise loomise tahvli

fig, ax=plt.subplots()  #teksti jaoks eraldi kiht
plt.scatter([70, 60, 65], [170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
ax.annotate("kati", (60, 160))
plt.savefig("liisi2.png")
plt.clf()

lapsed=pd.read_csv("http://www.tlu.ee/~jaagup/andmed/muu/5klass.txt")
plt.hist(lapsed.pikkus)
plt.savefig("liisi4.png")
plt.clf()