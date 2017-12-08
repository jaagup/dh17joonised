
import matplotlib
print("Tere, Sandra!")
matplotlib.use("Agg") #Et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3], ["Juku", "Mati", "Kati"])
plt.savefig("sandra.png")
plt.clf()

fig, ax=plt.subplots() #teksti jaoks eraldi kiht
plt.scatter([70, 60, 65], [170, 160, 180])
plt.title("laste andmed")
plt.xlabel("mass")
plt.ylabel("pikkus")
ax.annotate("Kati", (60, 160))
plt.savefig("sandra2.png")
plt.clf()
