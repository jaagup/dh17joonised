#print("Tere, Kairi!")

import matplotlib
print("Tere, Kairi!")
matplotlib.use("Agg") #et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3],["Juku", "Kati", "Mati"])
plt.savefig("kairi.png")
plt.clf() #puhastab joonise loomise tahvli

plt.scatter([70, 60, 65], [170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
plt.savefig("kairi2.png")
plt.clf()