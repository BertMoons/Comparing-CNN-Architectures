import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from comparison_data import data
import matplotlib.cm as cm

degrees = 65
bottom_adjustment = 0.2

hfont = {'fontname':'Arial'}

np.random.seed(1)
colors = cm.hsv(np.linspace(0,255,data.shape[0]).astype(int))
area = np.pi *(20*data[:,1].astype(float))

legend_x = np.asarray([800,1500, 2500, 7000, 35000])
legend_y = np.asarray([40,40, 40, 40, 40])
legend_values =  np.asarray([0.1,1, 10, 50, 100])
legend_names = np.asarray(['nan','1M','10M','50M','100M'])


# weights, ops, accuracy
fig, ax = plt.subplots()
ax.scatter(data[:,2].astype(float),data[:,3].astype(float),s=area, c=colors)
ax.scatter(legend_x,legend_y, legend_values*(area[0]/data[0,1]),c=[1,1,1])
ax.scatter(data[:,2].astype(float),data[:,3].astype(float),s=5, c=[1,1,1])
ax.grid()
ax.set_xscale('log')

for i, txt in enumerate(data[:,0]):
  ax.annotate(txt,xy=(data[:,2][i]+5,data[:,3][i]),**hfont)

for i, txt in enumerate(legend_names):
  ax.annotate(txt,xy=(legend_x[i]+5,legend_y[i]-2),**hfont)

plt.xlim(xmin=10)

plt.xlabel('# Operations [M-ops]',**hfont)
plt.ylabel('IMAGENET top-1 [%]',**hfont)

plt.savefig('./figures/accuracy_ops_modelsize.eps', format='eps')
plt.savefig('./figures/accuracy_ops_modelsize.png', format='png')


np.random.seed(1)
area = np.pi *(0.1*data[:,2].astype(float))

legend_x = np.asarray([15, 25, 70, 350])
legend_y = np.asarray([40,40, 40, 40])
legend_values =  np.asarray([1e1,.1e3, 10e3, 30e3])
legend_names = np.asarray(['nan','.1G','10G','30G'])



# weights, ops, accuracy
fig, ax = plt.subplots()
ax.scatter(data[:,1].astype(float),data[:,3].astype(float),s=area, c=colors)
ax.scatter(legend_x,legend_y, legend_values*(area[0]/data[0,2]),c=[1,1,1])
ax.scatter(data[:,1].astype(float),data[:,3].astype(float),s=5, c=[1,1,1])
ax.grid()
ax.set_xscale('log')

for i, txt in enumerate(data[:,0]):
  ax.annotate(txt,xy=(data[:,1][i],data[:,3][i]),**hfont)

for i, txt in enumerate(legend_names):
  ax.annotate(txt,xy=(legend_x[i],legend_y[i]-2),**hfont)

plt.xlim(xmin=0.1)

plt.xlabel('Model Size [M-weights]',**hfont)
plt.ylabel('IMAGENET top-1 [%]',**hfont)
plt.savefig('./figures/accuracy_modelsize_ops.eps', format='eps')
plt.savefig('./figures/accuracy_modelsize_ops.png', format='png')

# accuracy / ops
fig, ax = plt.subplots()
accuracy_ops_data = np.sort(np.divide(data[:,3].astype(float),data[:,2].astype(float)))
I = np.argsort(np.divide(data[:,3].astype(float),data[:,2].astype(float)))
ax.bar(range(data.shape[0]),accuracy_ops_data,color=colors[I])
ax.grid()
ax.set_yscale('log')
plt.xticks(np.arange(data.shape[0]), data[I,0],rotation=degrees)
plt.gcf().subplots_adjust(bottom=bottom_adjustment)

plt.ylabel('Accuracy / M-Ops',**hfont)
plt.savefig('./figures/accuracy_per_op.eps', format='eps')
plt.savefig('./figures/accuracy_per_op.png', format='png')

# accuracy / M-weights
fig, ax = plt.subplots()
accuracy_weight_data = np.sort(np.divide(data[:,3].astype(float),data[:,1].astype(float)))
I = np.argsort(np.divide(data[:,3].astype(float),data[:,1].astype(float)))
ax.bar(range(data.shape[0]),accuracy_weight_data,color=colors[I])
ax.grid()
ax.set_yscale('log')
plt.xticks(np.arange(data.shape[0]), data[I,0],rotation=degrees)
plt.gcf().subplots_adjust(bottom=bottom_adjustment)

plt.ylabel('Accuracy / M-Weights',**hfont)
plt.savefig('./figures/accuracy_per_weight.eps', format='eps')
plt.savefig('./figures/accuracy_per_weight.png', format='png')

# weights
fig, ax = plt.subplots()
ops = np.sort(data[:,1].astype(float))
I = np.argsort(data[:,1].astype(float))
ax.bar(range(data.shape[0]),ops,color=colors[I])
ax.grid()
ax.set_yscale('log')
plt.xticks(np.arange(data.shape[0]), data[I,0],rotation=degrees)
plt.gcf().subplots_adjust(bottom=bottom_adjustment)

plt.ylabel('Number of Weights [M-Weights]',**hfont)
plt.savefig('./figures/weights.eps', format='eps')
plt.savefig('./figures/weights.png', format='png')

# operations
fig, ax = plt.subplots()
ops = np.sort(data[:,2].astype(float))
I = np.argsort(data[:,2].astype(float))
ax.bar(range(data.shape[0]),ops,color=colors[I])
ax.grid()
ax.set_yscale('log')
plt.xticks(np.arange(data.shape[0]), data[I,0],rotation=degrees)
plt.gcf().subplots_adjust(bottom=bottom_adjustment)

plt.ylabel('Number of Operations [M-Ops]',**hfont)
plt.savefig('./figures/operations.eps', format='eps')
plt.savefig('./figures/operations.png', format='png')

# accuracy
fig, ax = plt.subplots()
ops = np.sort(data[:,3].astype(float))
I = np.argsort(data[:,3].astype(float))
ax.bar(range(data.shape[0]),ops,color=colors[I])
ax.grid()
plt.xticks(np.arange(data.shape[0]), data[I,0],rotation=degrees)
plt.gcf().subplots_adjust(bottom=bottom_adjustment)
plt.ylim(ymin=30,ymax=90)
plt.ylabel('ImageNet top-1 accuracy [%]',**hfont)
plt.savefig('./figures/top1_accuracy.eps', format='eps')
plt.savefig('./figures/top1_accuracy.png', format='png')


plt.show()
