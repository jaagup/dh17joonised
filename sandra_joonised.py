#print("Tere, Sandra!")

import matplotlib
print("Tere, Sandra!")
matplotlib.use("Agg") #Et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [170, 160, 180])
plt.xticks([1, 2, 3], ["Juku", "Mati", "Kati"])
plt.savefig("sandra.png")
plt.clf()