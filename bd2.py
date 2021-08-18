import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mue = pd.read_csv('mue.csv')
mue =mue.rename(columns={'Porcentaje de perdidas': 'Perdidas', 'Porcentaje de caida en ventas': 'caida_en_ventas',  'Numero de proveedores nacionales': 'Proveedores'})
v=mue.caida_en_ventas.sum()
s=mue.caida_en_ventas.count()
print(v/s)

res = pd.read_csv('res.csv')
res =res.rename(columns={'Porcentaje de perdidas': 'Perdidas', 'Porcentaje de caida en ventas': 'caida_en_ventas'})
v2=res.caida_en_ventas.sum()
s2=res.caida_en_ventas.count()
print(v2/s2)
#lo de arriba es para sacar los valores del csv val
val = pd.read_csv('val.csv')

labels = ['Porsentaje promedio de caida en ventas']
mueV = v/s
resV = v2/s2

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mueV, width, label='Muebles')
rects2 = ax.bar(x + width/2, resV, width, label='Restaurantes')

# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Porcentaje de establecimientos')
#ax.set_xlabel('Porcentaje de caida')
ax.set_title('Porcentaje de caida en ventas')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

#next

data = mue[['Proveedores','Perdidas']]
print ("m es: ")
gkk =data.groupby(['Proveedores'])
print (data.groupby('Proveedores').mean())


valor_por_ciudad = mue.groupby("Proveedores")["Perdidas"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.xlabel('Promedio de perdidas')
plt.ylabel('Num de proveedores')
plt.title('Perdidas segun cuantos proveedores tiene un negocio en muebles')
plt.show()
print("ok2")