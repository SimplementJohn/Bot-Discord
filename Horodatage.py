from datetime import datetime   #import de la librarie de date et d'horodatage




    # Définir une fonction 
def afficherHeureEtAction(action):
    heureActuelle = datetime.now().strftime("%H:%M:%S")
    print(heureActuelle, action)
