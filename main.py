import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

notas = pd.read_csv("data/ratings.csv")
print(notas)

notas['rating'].describe()

notas.columns = ['IdUsuario', 'IdFilme', 'Nota', 'Hora']

print(notas.head())

notas['Nota'].plot(kind='hist')
plt.show()

sns.boxplot(notas['Nota'])
plt.show()


#%%
filmes = pd.read_csv("data/movies.csv")

print(filmes.columns)
filmes.columns = ['IdFilme', 'Titulo', 'Genero']
print(filmes.head())



#%%
mediaFilme2 = notas.query('IdFilme==2')['Nota'].mean()
print(mediaFilme2)
#%%
medias = notas.groupby('IdFilme')['Nota'].mean()
print(medias)
#%%
medias.plot(kind='hist')
plt.show()
#%%
sns.displot(medias, kde=True)
plt.title("Histograma das medias por filme")
plt.show()