import matplotlib
print("Tere, Liisi!!")
matplotlib.use("Agg")  #et suudaks teksitekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3],[170, 160, 180])
plt.xticks([1, 2, 3],["juku", "kati", "mati"])
plt.savefig("liisi.png")
plt.clf() #puhastab joonise loomise tahvli

plt.scatter([70, 60, 65], [170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
plt.savefig("liisi2.png")
plt.clf()