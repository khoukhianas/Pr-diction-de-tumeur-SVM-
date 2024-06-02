import tkinter as tk
import joblib
import pandas as pd
import numpy as np
from tkinter import messagebox

# Charger le modèle SVM sauvegardé
loaded_model = joblib.load('C:/Users/HP/SVM_MODEL.pkl')
# Charger le scaler
loaded_scaler = joblib.load('C:/Users/HP/scaler_model.pkl')

def valider():
    # Collecter les valeurs des champs d'entrée utilisateur
    input_values = []
    for field in fields: 
        entry_value = entry_fields[field].get()
        try:
            value = float(entry_value)
        except ValueError:
            messagebox.showerror("Erreur", f"La valeur pour '{field}' n'est pas valide.")
            return
        input_values.append(value)
    
    # Convertir les valeurs en un tableau NumPy 
    input_array = np.array(input_values).reshape(1, -1)

    # Normaliser les valeurs avec le même scaler
    input_array_scaled = loaded_scaler.transform(input_array)

    # Faire une prédiction avec le modèle SVM chargé
    prediction = loaded_model.predict(input_array_scaled)
    
    # Afficher le résultat de la prédiction dans une boîte de message
    if prediction[0] == 'M':
        messagebox.showinfo("Résultat", "La tumeur est maligne.")
    else:
        messagebox.showinfo("Résultat", "La tumeur est bénigne.")

def remplir_aleatoire():
    # Remplir les champs avec des valeurs aléatoires
    for field in fields:  
        random_value = np.random.uniform(0, 10)  
        entry_fields[field].delete(0, tk.END)  
        entry_fields[field].insert(0, f"{random_value:.2f}") 

# Création de la fenêtre principale
root = tk.Tk()
root.title("Prédiction de tumeur")

# Cadre pour le canvas et la scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Création d'un canvas avec une scrollbar verticale
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Ajout de la scrollbar verticale au canvas
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Cadre intérieur pour placer les champs
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

# Liste des noms de champs
fields = [
        'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst'
]
 
entry_fields = {}

# Ajouter les champs 
for i, field in enumerate(fields):
    label = tk.Label(inner_frame, text=field)
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

    entry = tk.Entry(inner_frame, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)

    entry_fields[field] = entry

# Configurer le canvas pour le défilement
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

inner_frame.bind("<Configure>", on_frame_configure)

# Ajouter un bouton "Valider"
validate_button = tk.Button(root, text="Valider", command=valider)
validate_button.pack(pady=10)

# Ajouter un bouton "Remplir aléatoire"
random_button = tk.Button(root, text="Remplir aléatoire", command=remplir_aleatoire)
random_button.pack(pady=10)

root.mainloop()
