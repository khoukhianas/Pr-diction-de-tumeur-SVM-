# Prédiction-de-tumeur-SVM
# **Application de Prédiction de Tumeur**
Cette application utilise un modèle de Support Vector Machine (SVM) pour prédire si une tumeur est bénigne ou maligne en fonction de divers attributs des cellules tumorales.

# **Prérequis**
Avant de pouvoir exécuter cette application, assurez-vous d'avoir les éléments suivants installés sur votre machine :

**Python 3.x**
Bibliothèques Python nécessaires :
  * tkinter
  * joblib
  * numpy
  * pandas
Vous pouvez installer les bibliothèques nécessaires en utilisant pip :

* pip install joblib numpy pandas
**Fichiers Nécessaires**
Assurez-vous d'avoir les fichiers suivants dans le répertoire spécifié :

  * SVM_MODEL.pkl : Le modèle SVM pré-entrainé.
  * scaler_model.pkl : Le scaler utilisé pour normaliser les données.
Ces fichiers doivent être placés dans le répertoire C:/Users/HP/.

# **Utilisation**
Exécution de l'application

Lancez le script Python pour démarrer l'application :

  * python votre_script.py
**Interface utilisateur**

L'application ouvrira une fenêtre avec plusieurs champs d'entrée correspondant aux attributs des cellules tumorales. Vous pouvez remplir manuellement ces champs ou utiliser le bouton "Remplir aléatoire" pour les remplir avec des valeurs aléatoires.

# **Validation**

Une fois les champs remplis, cliquez sur le bouton "Valider" pour effectuer la prédiction. Une boîte de dialogue apparaîtra pour afficher si la tumeur est bénigne ou maligne.

# **Description du Code**
Chargement des Modèles :

loaded_model = joblib.load('C:/Users/HP/SVM_MODEL.pkl')
loaded_scaler = joblib.load('C:/Users/HP/scaler_model.pkl')
Ces lignes chargent le modèle SVM et le scaler sauvegardés.

Fonction valider :
Cette fonction collecte les valeurs des champs d'entrée, les normalise en utilisant le scaler chargé, et fait une prédiction en utilisant le modèle SVM. Elle affiche ensuite le résultat de la prédiction dans une boîte de message.

Fonction remplir_aleatoire :
Cette fonction remplit les champs d'entrée avec des valeurs aléatoires pour faciliter les tests.

Création de l'Interface :
Le reste du code crée une interface graphique en utilisant tkinter, avec des champs d'entrée pour chaque attribut et des boutons pour valider les données ou remplir les champs avec des valeurs aléatoires.

# **Remarques**
Assurez-vous que les chemins vers les fichiers modèles sont corrects.
Vous pouvez modifier la liste des attributs (fields) si nécessaire, en fonction des attributs utilisés pour entraîner votre modèle SVM.
# **Auteur**
***Khoukhi ANAS***
