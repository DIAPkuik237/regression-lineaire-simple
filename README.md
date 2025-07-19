# Regression-lineaire-simple
Premier projet de vulgarisation : prédire une note avec la régression linéaire simple
| Étudiant | Xi (Étude(h)) | Yi Réussite (score)  | 
| -------- | -----         | -----                | 
| A        | 2             | 0.3                  |
| B        | 3             | 0.5                  | 
| C        | 1             | 0.4                  | 
| D        | 4             | ?                    | 
Tabelau de données etudiants
# 🧮 Détails des calculs
Ce projet utilise une régression linéaire pour approximer une relation entre deux variables.
# Formule utilisée :
y = a * x + b
# Étapes de calcul :
1. Étape 1: Calcul des moyennes de x et y:
x̄=2+3+1/3=2; ȳ= 0.3+0.5+0.4/3 =0.4
2. Étape 2: Calcul de la pente `a` :
a = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)^2

| Étudiant | Xi    | Yi    | Xi- x̄    |  Yi- ȳ   | Produit ( Xi- x̄)(Yi- ȳ)|
| -------- | ----- | ----- | -------- | ---------| -----------------------|
| A        | 2     | 0.3   | 0        | -0.1     | 0                      |
| B        | 3     | 0.5   | +1       | +0.1     | 0.1                    |
| C        | 1     | 0.4   | -1       | 0        | 0                      |

Numérateur : 0+0.1+0=0.1
Dénominateur : 0²+1²+(−1)²=2
a= 0.1/2=0.05
3. Étape 3: Calcul de l'ordonnée à l’origine `b` : b = ȳ - a * x̄
 b= 0.4−0.05⋅2=0.4−0.1=0.3
🧠 Fonction trouvée
 ȳ=0.05x+0.3
🔮 Prédiction pour l’étudiant D (4h d’étude)
𝑦𝐷=0.05⋅4+0.3=0.5
4. Tracé de la droite de régression
5. Animation des résultats (voir le script `regression_animation.py`)

Remarque: x̄=Xmoy  et ȳ=Ymoy
