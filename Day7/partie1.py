# %% [markdown]
# # Titre 
# Voici ma partie 1 du day 7

# %%
print("Hello World!")

# %%
my_list = [10, 20, 30, 40, 50]
my_list

# %% [markdown]
# # La cellule calcule et affiche dans un tuple :
# o La somme de toutes les valeurs  
# o La moyenne arrondie à la deuxième décimale  
# o La valeur maximale  
# o La valeur minimale  

# %%
somme = sum(my_list)
moyenne = round(sum(my_list) / len(my_list), 2)
valmax = max(my_list)
valmin = min(my_list)
(somme, moyenne, valmax, valmin)

# %%
import pandas as pd

%time df = pd.read_csv('flights.csv')

# %%
%%timeit -r 20 -n 25

df['FL_DATE'].value_counts()

df.groupby('FL_DATE')['ARR_DELAY'].mean()

df.sort_values(by='DEP_DELAY', ascending=False).head(1000)



