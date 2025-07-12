# Etape 2 : Creation des relations
    print("\nEtape 2 : Creation des relations entre les noeuds")
    while True:
        print("Definir une relation (ou tapez '0' pour terminer) :")
        source = input("  - Noeud source : ")
        if source == '0':
            break
        destination = input("  - Noeud destination : ")
        if destination == '0':
            break
        relation = input("  - Type ou nom de la relation : ")
        G.add_edge(source, destination, label=relation)