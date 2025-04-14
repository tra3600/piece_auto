import numpy as np

def ajouter_noeud(noeud, T, P_new):
    """
    Ajoute un nouveau nœud au maillage et met à jour la liste des triangles.

    Args:
        noeud (numpy.ndarray): Tableau Nx2 contenant les coordonnées des nœuds existants.
        T (list): Liste des triangles (indices des nœuds).
        P_new (numpy.ndarray): Coordonnées du nouveau point à ajouter.

    Returns:
        list: Nouvelle liste des triangles après ajout et flips nécessaires.
    """
    # Ajouter le nouveau point au tableau des nœuds
    noeud = np.vstack([noeud, P_new])
    n_new = len(noeud) - 1  # Indice du nouveau point

    # Initialiser une nouvelle liste de triangles
    T_new = []

    # Étape 1 : Identifier le triangle contenant P_new
    for triangle in T:
        P0, P1, P2 = [noeud[i] for i in triangle]
        if point_dans_triangle(P_new, P0, P1, P2):
            # Supprimer ce triangle
            T.remove(triangle)

            # Ajouter les trois nouveaux triangles
            T_new.append([triangle[0], triangle[1], n_new])
            T_new.append([triangle[1], triangle[2], n_new])
            T_new.append([triangle[2], triangle[0], n_new])
            break

    # Étape 2 : Vérifier et appliquer les flips
    for triangle in T_new:
        for voisin in trouver_voisins(triangle, T_new):
            if not respecte_delaunay(triangle, voisin, noeud):
                flip(triangle, voisin, T_new)

    # Retourner la liste mise à jour des triangles
    return T_new

def point_dans_triangle(P, P0, P1, P2):
    """
    Vérifie si un point P est dans un triangle défini par P0, P1, P2.
    """
    # Calcul des coordonnées barycentriques
    A = 0.5 * (-P1[1] * P2[0] + P0[1] * (-P1[0] + P2[0]) + P0[0] * (P1[1] - P2[1]) + P1[0] * P2[1])
    s = 1 / (2 * A) * (P0[1] * P2[0] - P0[0] * P2[1] + (P2[1] - P0[1]) * P[0] + (P0[0] - P2[0]) * P[1])
    t = 1 / (2 * A) * (P0[0] * P1[1] - P0[1] * P1[0] + (P0[1] - P1[1]) * P[0] + (P1[0] - P0[0]) * P[1])
    return s >= 0 and t >= 0 and (1 - s - t) >= 0

def flip(triangle, voisin, T):
    """
    Remplace l'arête commune entre deux triangles par une nouvelle arête.
    """
    # Implémentation du flip (basculer l'arête commune)
    pass

def respecte_delaunay(triangle, voisin, noeud):
    """
    Vérifie si deux triangles respectent la condition de Delaunay.
    """
    # Implémentation de la vérification de la condition de Delaunay
    pass

def trouver_voisins(triangle, T):
    """
    Trouve les triangles voisins d'un triangle donné.
    """
    voisins = []
    for t in T:
        if len(set(triangle) & set(t)) == 2:  # Deux sommets en commun
            voisins.append(t)
    return voisins

# Exemple d'utilisation
noeud = np.array([
    [0.0, 0.0],  # P0
    [1.0, 0.0],  # P1
    [0.5, 1.0],  # P2
    [0.5, -1.0]  # P3
])  # Coordonnées des nœuds
T = [[0, 1, 2], [2, 3, 0]]  # Triangles initiaux
P4 = np.array([0.6, 0.2])  # Nouveau nœud P4

T_new = ajouter_noeud(noeud, T, P4)
print("Nouveaux triangles :", T_new)