import numpy as np
import matplotlib.pyplot as plt
x = np.random.randint(0,2,(42,42))

# %% [markdown]
# o x o  
# o o x  
# x x x

x[1][2] = 1
x[2][3] = 1
x[3][1:4] = 1

# %%
def fresh():
    global x
    global y
    y = np.zeros([42,42],dtype=int)
    for i in range(40):
        for j in range(40):
            center = x[i+1,j+1]
            num = np.sum(x[i:i+3,j:j+3])
            if (center==0 and num==3):
                y[i+1,j+1]=1
                continue
            if center:
                if num<3:
                    y[i+1,j+1]=0
                elif num<5:
                    y[i+1,j+1]=1
                else:
                    y[i+1,j+1]=0
    x = y
    
for i in range(150):
    plt.clf()
    fresh()
    #plt.imshow(x,cmap="gray")
    plt.imshow(x)
    plt.pause(0.01)
    plt.ioff()



