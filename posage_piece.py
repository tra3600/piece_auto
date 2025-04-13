def retourner_piece(P):
    """
    Effectue une rotation de 180° autour de l'axe y pour retourner la pièce.
    Cela revient à inverser les éléments de la liste.

    Args:
        P (list): Liste des altitudes de la pièce.

    Returns:
        list: Liste retournée.
    """
    return P[::-1]

# Exemple d'utilisation
P1 = [2., 3., 2., 3.]
P2 = [1., 2., 1., 3.]

P2_retournee = retourner_piece(P2)
print("Pièce 1:", P1)
print("Pièce 2 retournée:", P2_retournee)

def droite(Ls, n, p, Delta_x=1.0):
    """
    Calcule la pente et l'ordonnée à l'origine d'une droite passant par deux points.

    Args:
        Ls (list): Liste des altitudes.
        n (int): Indice du premier point de contact.
        p (int): Indice du second point de contact.
        Delta_x (float): Longueur élémentaire associée à la discrétisation spatiale (par défaut 1.0).

    Returns:
        list: Une liste contenant la pente (a) et l'ordonnée à l'origine (b) de la droite.
    """
    # Altitudes des points n et p
    zn = Ls[n]
    zp = Ls[p]
    
    # Calcul du coefficient directeur (pente) a
    a = (zn - zp) / ((n - p) * Delta_x)
    
    # Calcul de l'ordonnée à l'origine b
    b = zn - n * a * Delta_x
    
    return [a, b]

# Exemple d'utilisation
P1 = [2., 3., 2., 3.]  # Liste des altitudes de la pièce 1
n = 0
p = 1
resultat = droite(P1, n, p)
print("Pente et ordonnée à l'origine:", resultat)

def posage(Ls1, Ls2, n, p, Delta_x=1.0):
    """
    Calcule les distances algébriques maximale et minimale entre deux pièces discrétisées
    dans une situation de posage.

    Args:
        Ls1 (list): Liste des altitudes des points de la pièce 1 (située en dessous).
        Ls2 (list): Liste des altitudes des points de la pièce 2 retournée (située au-dessus).
        n (int): Indice du premier point de contact.
        p (int): Indice du second point de contact.
        Delta_x (float): Longueur élémentaire associée à la discrétisation spatiale (par défaut 1.0).

    Returns:
        list: Une liste contenant la distance algébrique maximale et minimale entre les deux pièces.
    """
    # Calcul de la pente et de l'ordonnée à l'origine de la droite associée à Ls1
    [a, b] = droite(Ls1, n, p, Delta_x)

    # Initialiser les distances algébriques maximales et minimales
    distance_max = float('-inf')  # Très petite valeur initiale
    distance_min = float('inf')   # Très grande valeur initiale

    # Parcourir tous les points des listes Ls1 et Ls2
    for k in range(len(Ls1)):
        # Calculer les altitudes par rapport à la droite pour chaque pièce
        altitude_Ls1 = Ls1[k] - (a * k * Delta_x + b)
        altitude_Ls2 = Ls2[k] - (a * k * Delta_x + b)

        # Calculer la distance algébrique entre les deux pièces
        distance = altitude_Ls2 - altitude_Ls1

        # Mettre à jour les distances maximales et minimales
        distance_max = max(distance_max, distance)
        distance_min = min(distance_min, distance)

    # Retourner les distances maximale et minimale
    return [distance_max, distance_min]

# Exemple d'utilisation
P1 = [2., 3., 2., 3.]  # Liste des altitudes de la pièce 1
P2 = [-3., -1., -2., -1.]  # Liste des altitudes de la pièce 2 (retournée)
n = 0
p = 3

resultat = posage(P1, P2, n, p)
print("Distances algébriques maximale et minimale:", resultat)