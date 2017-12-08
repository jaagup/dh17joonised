import matplotlib
print ("tere")
matplotlib.use ("Agg") #et suudaks tekstiekraanil hakkama saada
import matplotlib.pyplot as plt
plt.bar ([1,2,3],[170, 160, 180])
plt.xticks ([1,2,3], ["Juku", "Kati", "Mati"]) 
plt.savefig("hagi.png") #teeb pildi
plt.clf() #puhastab joonise loomise tahvli