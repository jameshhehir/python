import numpy as np
from stl import mesh
import tkinter as tk
from tkinter.filedialog import askopenfilename
# Using an existing closed stl file:
your_mesh = mesh.Mesh.from_file(askopenfilename(filetypes=[('stl', '*.stl')]))

volume, cog, inertia = your_mesh.get_mass_properties()
volume = volume/1000
price = volume*1.24
print("Volume                                  = {0}".format(volume)+"cm^3")
print("Position of the center of gravity (COG) = {0}".format(cog))
print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
print("                                          {0}".format(inertia[1,:]))
print("                                          {0}".format(inertia[2,:]))
print("Price                                   = €{0}".format(price))

