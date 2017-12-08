import matplotlib
print("test jaagup")
matplotlib.use("Agg") #Et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3],["Juku", "Kati", "Mati"])
plt.savefig("jaagup1.png")
plt.clf()