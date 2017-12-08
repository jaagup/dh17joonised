#print("Tere Liisi")
import matplotlib
print("Tere, Liisi!!")
matplotlib.use("Agg")  #et suudaks teksitekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bat([1, 2, 3],[170, 160, 180])
plt.xticks([1, 2, 3],["juku", "kati", mati"])
plt.savefig("liisi.png")
plt.clf()
