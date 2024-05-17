from tkinter import *
import random as rd
import numpy as np 
import math
#=== Variables
width = 400
height = 400
dt = 0.2
l_0 = 400 #longueur au repos des ressort
k = 1 #raideur ressort
K = 50000 #Constante de la force centrale
#=== Class
class MyGraphDrawing():
    def __init__(self,graph):
        nodes_pos = list()
        for i in range(len(graph)):
            nodes_pos.append( (rd.uniform(0,width-4),rd.uniform(0,height-4)) )
        self.pos = np.array(nodes_pos)
        self.g = graph
        self.v = np.array([((rd.random()-0.5)*10, (rd.random()-0.5)*10) 
                           for i in range(len(graph))])




#=== Functions



def draw(can,graph_drawing):
    """fonction qui dessine sur le canva un graph dont les noeuds
    ont des positions aléatoire"""
    can.delete('all')
    for i in range(len(graph)):
        for j in graph[i]:  # arc de i a j
            can.create_line(graph_drawing.pos[i][0], graph_drawing.pos[i][1], graph_drawing.pos[j][0], graph_drawing.pos[j][1])
    for (x, y) in graph_drawing.pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="red")
        

def decompose(A,B):
    """fonction qui renvoie la norme et le vecteur unitaire 
    du vecteur AB"""
    AB = B - A
    square = sum([e**2 for e in AB])
    norm = math.sqrt(square)
    return norm , AB/norm 

def compute_spring_force(graph_drawing, F):
    """fonction qui calcule les forces de rappel des ressorts appliquées aux points"""
    for i in range(len(graph_drawing.g)):
        for j in graph_drawing.g[i]:
            norm_ji , u_ji = decompose(graph_drawing.pos[j],graph_drawing.pos[i])
            x_i = graph_drawing.pos[i][0]
            y_i = graph_drawing.pos[i][1]
            #Si le point du graphe est sur un bord il sera renvoyé dans la direction opposé
            if y_i <= 4 or x_i <= 4 or y_i >= 396 or x_i >= 396:
                F[i] += k* (norm_ji - l_0)* u_ji
            F[i] -= k* (norm_ji - l_0)* u_ji
    return F

def apply_spring_force(graph_drawing):
    """fonction modifiant la position et la vitesse des points en fonction de la force de rappel du ressort  """
    F = np.zeros((len(graph),2))
    F = compute_spring_force(graph_drawing , F)
    graph_drawing.v += dt * F
    graph_drawing.pos += (dt**2) * F 
    draw(can,graph_drawing)

def compute_central_force(graph_drawing,F):
    """fonction qui calcule les forces centrales appliquées aux points"""
    for i in range(len(graph_drawing.g)):
        for j in graph_drawing.g[i]:
            norm_ji , u_ji = decompose(graph_drawing.pos[j],graph_drawing.pos[i])
            x_i = graph_drawing.pos[i][0]
            y_i = graph_drawing.pos[i][1]
            #Si le point du graphe est sur un bord il sera renvoyé dans la direction opposé
            if y_i <= 4 or x_i <= 4 or y_i >= 396 or x_i >= 396:
                F[i] -= K* u_ji/(norm_ji**2)
            F[i] += K* u_ji/(norm_ji**2)
    return F

def apply_central_force(graph_drawing):
    """fonction modifiant la position et la vitesse des points en fonction 
    de la force centrale """
    F = np.zeros((len(graph),2))
    F = compute_central_force(graph_drawing , F)
    graph_drawing.v += dt * F
    graph_drawing.pos += (dt**2) * F 
    draw(can,graph_drawing)

#=== Script
if __name__ == 'main':
    graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
        [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    window = Tk()
    window.geometry('600x600')
    graph_drawing = MyGraphDrawing(graph)
    can = Canvas(window, width= width, height= height)
    can.grid(column=0,row=0)
    draw(can,graph_drawing)
    window.bind('<f>',lambda x: apply_spring_force(graph_drawing))
    window.bind('<c>',lambda x: apply_central_force(graph_drawing))
    Label(window, text="Press F to add spring force").grid()
    Label(window, text="Press C to add central force",anchor= "s").grid()
    window.mainloop()

