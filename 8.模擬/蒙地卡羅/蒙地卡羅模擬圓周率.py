import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

l=2
ax,ay = -1/2,1/2
bx,by = -1/2,1/2
cx,cy = -1/2,1/2
dx,dy = -1/2,1/2

ox,oy = int((ax/cx)/2),int((ay+by)/2)

point_number_list = [10,50,200,500,1000,10000]

rows = 3
cols = 2 
fig,ax = plt.subplots(rows,cols,figsize=(14,8))
fign = 0
fig_label = ['(a)','(b)','(c)','(d)','(e)','(f)']

for i in range(rows):
    for j in range(cols):
        print('Figure #: ', [i, j])
        inside=0
        for _ in range(point_number_list[fign]):
            x_inside =[]
            y_inside = []
            x_outside = []
            y_outside = []
            
            x=random.uniform(-1/2,1/2)
            y=random.uniform(-1/2,1/2)

            if (x-ox)**2+(y-oy)**2 <= (1/2)**2:
                inside +=1
                x_inside.append(x)
                y_inside.append(y)
            else:
                x_outside.append(x)
                y_outside.append(y)

            #畫目前的row*col圖
            sns.scatterplot(x=x_inside,y=y_inside,color='g',ax=ax[i,j])
            sns.scatterplot(x=x_outside,y=y_outside,color='r',ax=ax[i,j])
            

            ax[i,j].set_title(fig_label[fign],loc='left')
            ax[i,j].set_aspect('equal')
            ax[i,j].set_xticks([-1,0,1])
            ax[i,j].set_yticks([-1,0,1])
        #plt.show()
        pi = 4*inside/point_number_list[fign]
        print(f'Estimated pi is {round(pi,4)} based on {point_number_list[fign]} points simulations')
    
        fign+=1
fig.tight_layout()
plt.show()    