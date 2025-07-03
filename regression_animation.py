import numpy as np
import matplotlib.pyplot as plt

# Données (étudiants A, B, C)
x = np.array([2, 3, 1])  # Heures d'étude
y = np.array([0.3, 0.5, 0.4])  # Scores

# Calcul des moyennes
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calcul coefficients a (pente) et b (ordonnée à l'origine)
numerateur = np.sum((x - x_mean) * (y - y_mean))
denominateur = np.sum((x - x_mean) ** 2)
a = numerateur / denominateur
b = y_mean - a * x_mean

print(f"Equation de la droite : y = {a:.2f} * x + {b:.2f}")

# Prédiction pour 4 heures d'étude
x_pred = 4
y_pred = a * x_pred + b
print(f"Prediction pour 4h : y = {y_pred:.2f}")

# Préparation de la droite de regression
x_line = np.linspace(0, 5, 100)
y_line = a * x_line + b

# Visualisation
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Données (étudiants)')
# Annotation des points
etiquettes = ['A (2h)', 'B (3h)', 'C (1h)']
for i, txt in enumerate(etiquettes):
    plt.annotate(txt, (x[i] + 0.05, y[i] + 0.01))

plt.plot(x_line, y_line, color='green', label=f'Droite: y = {a:.2f}x + {b:.2f}')
plt.scatter(x_pred, y_pred, color='red', label=f'Prédiction (4h → {y_pred:.2f})', s=100, marker='x')

plt.xlabel("Heures d'étude")
plt.ylabel("Score de réussite")
plt.title("Régression linéaire simple (étudiants A, B, C)")
plt.legend()
plt.grid(True)
plt.xlim(0, 5)
plt.ylim(0, 1)
plt.show()
