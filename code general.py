Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import networkx as nx
import matplotlib.pyplot as plt

def creer_graphe():
    print("=== Création d’un graphe pour un domaine universitaire ===")
... 
...     G = nx.DiGraph()
...     couleurs_noeuds = {}
... 
...     # Étape 1 : Création des nœuds
...     print("\nÉtape 1 : Création des nœuds")
...     while True:
...         nom_noeud = input("Entrez le nom du nœud (ou '0' pour terminer) : ")
...         if nom_noeud == '0':
...             break
...         couleur = input(f"Entrez une couleur pour le nœud '{nom_noeud}' : ")
...         G.add_node(nom_noeud)
...         couleurs_noeuds[nom_noeud] = couleur
... 
...     # Étape 2 : Création des relations
...     print("\nÉtape 2 : Création des relations entre les nœuds")
...     while True:
...         print("Définir une relation (ou tapez '0' pour terminer) :")
...         source = input("  - Nœud source : ")
...         if source == '0':
...             break
...         destination = input("  - Nœud destination : ")
...         if destination == '0':
...             break
...         relation = input("  - Type ou nom de la relation : ")
...         G.add_edge(source, destination, label=relation)
... 
...     # Étape 3 : Affichage du graphe
...     print("\nAffichage du graphe...")
... 
...     couleurs = [couleurs_noeuds.get(node, 'gray') for node in G.nodes()]
...     pos = nx.spring_layout(G)
...     nx.draw(G, pos, with_labels=True, node_color=couleurs, node_size=1500, font_size=10, font_weight='bold')
...     edge_labels = nx.get_edge_attributes(G, 'label')
...     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
... 
...     plt.title("Graphe du domaine universitaire")
...     plt.show()
... 
... # Boucle principale
... while True:
...     creer_graphe()
    continuer = input("\nVoulez-vous créer un graphe pour un autre domaine ? (oui/non) : ")
    if continuer.lower() not in ['oui', 'o', 'yes', 'y']:
        print("Fin du programme. Merci !")
        break
