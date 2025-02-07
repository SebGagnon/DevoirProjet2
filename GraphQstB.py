import csv  
import matplotlib.pyplot as plt
import numpy as np

tension=[]
courant=[]
n=np.linspace(1,1000,1000)

with open('Donnees.csv', 'r') as file:
    entete=next(file)
    lecteur=csv.reader(file)
    for row in lecteur :
        tension.append(float(row[0]))
        courant.append(float(row[1]))

moyenne=np.average(tension)
ecart_type=np.std(tension)


fig, ax = plt.subplots()
ax.scatter(n, tension, s=2)

ax.set(xlim=(1, 1000), xticks=[1,100,200,300,400,500,600,700,800,900,1000],
       ylim=(0.9995*np.min(tension), 1.0005*np.max(tension)), yticks=np.linspace(np.min(tension),np.max(tension),8))
ax.tick_params(right=True, top=True, labelright=False, labeltop=False, labelrotation=0)

ax.set_ylabel('Tension (V)', fontsize=15)
ax.set_xlabel('N',fontsize=15)

print('Moyenne : ')
print(moyenne)
print('Écart type : ')
print(ecart_type)

plt.show()