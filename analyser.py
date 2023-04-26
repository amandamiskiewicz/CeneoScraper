import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = 96693065 #input("Podaj kod produktu: ")
opinions = pd.read_json(f"./opinions/{product_code}.json")
opinions.rating = opinions.rating.map(lambda x: float(x.split("/")[0].replace(",",".")))
# print(type(opinions))
print(opinions)
# podstawowe statystyki opinii
# opinions_count = opinions.opinion_id.count()
# opinions_count = len(opinions)
opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avg_rating = opinions.rating.mean()
print(f"""Dla produktu o kodze {product_code} pobrano {opinions_count} opini/opinie.
Dla  {pros_count} opinii dostępna jest lista zalet, 
a dla {cons_count} opinii dostępna jest lista wad. 
Średnia ocena produktu wynosi {avg_rating}.""" )

# histogram częstości ocen produktu
ratings = opinions.rating.value_counts().reindex(list(np.arange(0,5.5,0.5)),fill_value = 0)
print(ratings)
ratings.plot.bar()
# plt.show()
plt.savefig(f"./plots/{product_code}_rating.png")
plt.close()

# udział rekomendacji w opiniach
recommendations = opinions.recommendation.value_counts(dropna=False)
recommendations.plot.pie(label="", autopct="%1.1f%%")
plt.title("Rekomendacje")
plt.savefig(f"./plots/{product_code}_recommendations.png")
plt.close()

