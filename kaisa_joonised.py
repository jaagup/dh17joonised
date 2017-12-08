import matplotlib
matplotlib.use("Agg") #et suudaks tekstiekraanil hakkama saada, ei näitaks linuxi aknas
import matplotlib.pyplot as plt #selle asemel kirjuta säärane lühend 'plt'
plt.bar([1, 2, 3], [170, 160, 180]) #teeb 3 tulpa, igale oma väärtus
plt.xticks([1, 2, 3], ["Juku", "Kati", "Mati"]) #annab tulpadele nimed
plt.savefig("kaisa1.png") #teeb pildi
plt.clf() #puhastab joonise loomise tahvli kui hiljem tahad veel midagi teha