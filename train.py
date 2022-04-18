import json
from tkinter.tix import Y_REGION
import zipfile
import pickle
import pandas as pd
import os
import json
from sklearn import model_selection
os.chdir(os.path.dirname(__file__))

with open('model/my_model_l', 'rb') as archivo_entrada:
        modelo_local = pickle.load(archivo_entrada)

with open('model/my_model_e', 'rb') as archivo_entrada:
        modelo_empate = pickle.load(archivo_entrada)

with open('model/my_model_v', 'rb') as archivo_entrada:
        modelo_visitante = pickle.load(archivo_entrada)

# Data train-scaled
X_train_scaled = pd.read_csv('Processed/x_train.csv')

# Gana Local Modelo - Entrenamiento
Y_train_L = pd.read_csv('Processed/Y_train_L.csv')
modelo_local.fit(X_train_scaled,Y_train_L)

with open('model/entrenados/my_model_l', 'wb') as archivo_salida:
    pickle.dump(modelo_local, archivo_salida)

# Gana Visitante Modelo - Entrenamiento
Y_train_V = pd.read_csv('Processed/Y_train_V.csv')
modelo_visitante.fit(X_train_scaled,Y_train_V)

with open('model/entrenados/my_model_v', 'wb') as archivo_salida:
    pickle.dump(modelo_visitante, archivo_salida)

# Gana Local Modelo - Entrenamiento
Y_train_E = pd.read_csv('Processed/Y_train_E.csv')
modelo_empate.fit(X_train_scaled,Y_train_E)

with open('model/entrenados/my_model_e', 'wb') as archivo_salida:
    pickle.dump(modelo_empate, archivo_salida)