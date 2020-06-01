import networkx as nx
import matplotlib as plt
import numpy as np
import random

def hierarchy_pos2(G, root, levels=None, width=1., height=1.):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node
       levels: a dictionary
               key: level number (starting from 0)
               value: number of nodes in this level
       width: horizontal space allocated for drawing
       height: vertical space allocated for drawing'''
    TOTAL = "total"
    CURRENT = "current"
    def make_levels(levels, node=root, currentLevel=0, parent=None):
        """Compute the number of nodes for each level
        """
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                levels =  make_levels(levels, neighbor, currentLevel + 1, node)
        return levels
    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1/levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((left + dx*levels[currentLevel][CURRENT])*width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        for neighbor in neighbors:
            if not neighbor == parent:
                pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc-vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = height / (max([l for l in levels])+1)
    return make_pos({})

'''
# ejemplo de uso de la funcion siguiente:
G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
                  (5,11), (5,12), (6,13)])
pos = hierarchy_pos(G,1)    
nx.draw(G, pos=pos, with_labels=True)
'''

# TODAVIA NO LAS USO...
# esta funcion devuelve la ciudad de menor costo de transporte desde la ciudad variable <inicio>
def calcMenCost(cantCiu,mat_costCiu,inicio,listExceptuadas):
    listExceptuadas.append(inicio)
    vec_costCiu_aux = mat_costCiu[inicio-1]
    #print("vec cost Ciu: {}".format(vec_costCiu_aux))
    menor = -1
    dest = -1
    a = 0
    while (menor == -1 and dest == -1):
        if (a+1) not in listExceptuadas:
            menor = vec_costCiu_aux[a]
            dest = (a+1)
        else:
            a += 1
    for a in range(cantCiu-1):
        if (a+1) in listExceptuadas:
            continue
        aux = vec_costCiu_aux[a]
        if menor > aux and aux != 0:
            menor = aux
            dest = (a+1)
    return dest,listExceptuadas

def graficar(ax, datox, datoy, param_dicc):
    '''
    A helper function to make a graph
    Parameters
    ----------
    ax : Axes
        The axes to draw to
    datox : array
       The x data
    datoy : array
       The y data
    param_dicc : dict
       Dictionary of kwargs to pass to ax.plot
    Returns
    -------
    out : list
        list of artists added
   '''
    out = ax.plot(datox, datoy, **param_dicc)
    return out

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    G: the graph (must be a tree)
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    width: horizontal space allocated for this branch - avoids overlap with other branches
    vert_gap: gap between levels of hierarchy
    vert_loc: vertical location of root
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))
    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        '''
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


''' OBSOLETO
def calcularHn(mat_costCiu,vec_costCiu,nodo_n,nodo_m,nivel):
    # se copia el vector vec_costCiu en aux
    aux = [a for a in vec_costCiu] # vec_costCiu = [5,15,17,7,6,19,20,7,21,5]
    # se le quita el costo que tendria dicho recorrido
    aux.remove(costoDeNaM(mat_costCiu,nodo_n,m))
    # se ordena ascendentemente dicho vector
    aux.sort(reverse=False)
    # se toman los primeros (5-nivel) valores y se los sumariza en Hn
    Hn = 0
    for a in (aux[:len(mat_costCiu[0])-nivel]): #len(mat_costCiu[0]) es la cantidad de ciudades ya que representa la cantidad de columnas de la matriz
        Hn += a
    return Hn
'''


''' Se deja como posible funcion a utilizar en algun momento
# Se obtienen las conexiones de los nodos adyacentes entre sí y los parientes del nodo_n
for n, nbrsdict in grafoG.adjacency():
   for nbr, eattr in nbrsdict.items():
         adyacentes.append((n,nbr))
'''