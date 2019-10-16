import random, matplotlib.pyplot as plt, numpy as np
from operator import itemgetter

#tunable parameters
cells, steps, death_chance, area = 200, 50, 0.15, [-4, 4, -3, 3] #x1,x2,y1,y2
z = lambda x,y:  (      #uncomment only one of functions
#x**2 + y**2
1/(x**2 + y**2 + 1) * np.cos(np.pi * x) * np.cos(np.pi * y)
#x**2 - y**2 
)

#other parameters
x,y = np.meshgrid(np.linspace(area[0], area[1], 50),
                  np.linspace(area[2], area[3], 50))
step_length = (area[1]-area[0]+area[3]-area[2]) / 20
cell = [[random.uniform(area[0],area[1]), random.uniform(area[2],area[3]),
         random.uniform(0, 2*np.pi), 0, 0, 0] for i in range(cells)]

#plotting
fig = plt.gcf()
fig.show()
for i in range(steps):
    fig.clf()
    curr_length = step_length*(steps-i)/steps
    plt.contourf(x, y, z(x,y), cmap=plt.get_cmap("jet"))
    for j in cell:                                      #chemotaxis
        j[3],j[4] = curr_length * np.cos(j[2]), curr_length * np.sin(j[2])
        if z(j[0]+j[3],j[1]+j[4]) < z(j[0],j[1]):
            j[0],j[1],j[5] = j[0] + j[3], j[1] + j[4], j[5] + z(j[0],j[1])
        else:
            j[2]=random.uniform(0,2*np.pi)
        plt.axis(area)
        plt.scatter(j[0], j[1])
    cell.sort(key=itemgetter(5))
    if not(i % 5):                                      #reproduction
        for n in range(cells//2):
            cell[n+cells//2][0], cell[n+cells//2][1] = cell[n][0], cell[n][1]
    if not(i % 10):                                     #elimination & dispersal
        for n in range(int(round(cells*death_chance))):
            aim = int(random.random()*cells)
            cell[aim][0] = random.uniform(area[0],area[1])
            cell[aim][1] = random.uniform(area[2],area[3])
    fig.canvas.draw()
plt.show() #prevent closing
