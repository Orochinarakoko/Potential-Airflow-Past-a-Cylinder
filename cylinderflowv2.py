#---------------------------------------------- import required libs
import matplotlib.pyplot as mp
from matplotlib.patches import Circle
import numpy as np
from math import pi,sqrt
#---------------------------------------------- initialise required variables
cylinder_radius = float(input("Cylinder Radius >>> "))
uniform_v = float(input("What is the relative speed of airflow >>> "))
num_x = int(input("How many x-coordinates >>> "))
num_y = int(input("How many y-coordinates >>> "))

strength = uniform_v*cylinder_radius**2
#--------------------------------------------- set up a grid

x_coords = np.linspace(1,10*cylinder_radius,num_x)
y_coords = np.linspace(1,3*cylinder_radius,num_y)
Y_coords , X_coords = np.meshgrid(y_coords,x_coords)
speed = []
x_v = []
y_v = []

#-------------------------------------------- set up vector field for each point in grid
for x in x_coords:
    for y in y_coords:

        if sqrt(((x-(5*cylinder_radius))**2+(y-(1.5*cylinder_radius))**2))>= cylinder_radius:
            x_v.append(uniform_v + (strength/2*pi)*((-((x-(5*cylinder_radius))**2)+(y-(1.5*cylinder_radius))**2)/(((x-(5*cylinder_radius))**2)+((y-(1.5*cylinder_radius))**2))**2))
            y_v.append((strength/2*np.pi)*((-2*(x-(5*cylinder_radius))*(y-(1.5*cylinder_radius)))/((((x-(5*cylinder_radius))**2)+((y-(1.5*cylinder_radius))**2))**2)))
            speed.append(sqrt((x_v[-1])**2+(y_v[-1])**2))
        else:
            x_v.append(0)
            y_v.append(0)
            speed.append(0)


#------------------------------------------- create cylinder
Cylinder = mp.Circle((5*cylinder_radius,1.5*cylinder_radius),radius = cylinder_radius,color="black")
mp.quiver(X_coords,Y_coords,x_v,y_v,speed,cmap = "jet",width=0.001)

axes = mp.gca()
axes.add_patch(Cylinder)
axes.set_aspect("equal")
mp.title("Potential Airflow Past a cylinder")
cbar = mp.colorbar()

# display vector field
mp.show()
