import matplotlib
matplotlib.use("Agg") #et suudaks tekstiekraanil hakkama saada, ei näitaks linuxi aknas
import matplotlib.pyplot as plt #selle asemel kirjuta säärane lühend 'plt'
plt.bar([1, 2, 3], [170, 160, 180]) #teeb 3 tulpa, igale oma väärtus
plt.xticks([1, 2, 3], ["Juku", "Kati", "Mati"]) #annab tulpadele nimed
plt.savefig("kaisa1.png") #teeb pildi
plt.clf() #puhastab joonise loomise tahvli kui hiljem tahad veel midagi teha

fig, ax=plt.subplots() #teksti jaoks eraldi kiht, paneb uue kihi scatterploti peale
plt.scatter([70, 60, 65], [170, 160, 180]) #teeb scatterploti, lisab massid ja nendele vastavad pikkused
plt.title("Laste andmed")
plt.xlabel("mass") #lisab x teljele pealkirja
plt.ylabel("pikkus")
ax.annotate("Kati", (60, 160)) #lisan sõnu/pealkirju mingile numbrile
plt.savefig("kaisa2.png")
plt.clf()