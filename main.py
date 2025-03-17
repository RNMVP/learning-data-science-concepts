import pandas as pd
import seaborn as sns

notas = pd.read_csv("data/ratings.csv")
print(notas)

notas['rating'].describe()

notas['rating'].plot(kind='hist')

sns.boxplot(notas['rating'])