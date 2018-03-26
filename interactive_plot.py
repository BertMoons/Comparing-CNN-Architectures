import matplotlib.pyplot as plt
import numpy as np
import mpld3

from comparison_data import data

degrees = 65
bottom_adjustment = 0.2
fsize = 10

hfont = {'fontname':'Arial'}

legend_x = np.log10(np.asarray([800,1500, 2500, 7000, 35000]))
legend_y = np.asarray([40,40, 40, 40, 40])
legend_values =  np.asarray([0.1,1, 10, 50, 100])
legend_names = np.asarray(['nan','1M','10M','50M','100M'])

N = len(data[:,0])
area = np.pi*(20*data[:,1].astype('float'))



# weights, ops, accuracy
fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
ax.scatter(np.log10(data[:,2].astype('float')),data[:,3],s=area, c=1000 * np.linspace(0,1,num=N),alpha=0.3,cmap=plt.cm.jet)
ax.scatter(legend_x,legend_y, legend_values*(area[0]/data[0,1]),c=[1,1,1])
scatter = ax.scatter(np.log10(data[:,2].astype('float')).astype(float),data[:,3].astype(float),s=25, c=[1,1,1])
ax.grid()

for i, txt in enumerate(legend_names):
  ax.annotate(txt,xy=(legend_x[i],legend_y[i]),**hfont)

ax.set_xlabel('Log10(# Operations [M-ops])',**hfont)
ax.set_ylabel('IMAGENET top-1 [%]',**hfont)



#labels = ['{} , {} M-ops, {} M-wghts, {}%'.format(data[i,0],data[i,2],data[i,1],data[i,3]) for i in range(N)]
labels = [data[i,0] for i in range(N)]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)

mpld3.save_html(plt.gcf(),"interactive_plot.html")

mpld3.show()
