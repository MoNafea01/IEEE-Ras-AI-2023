import pandas as pd
import numpy as np
wine = pd.read_csv('winequality_edited.csv')
def levels (ph):
    x=wine['pH'].describe()
    if ph <= x['25%']:
        return 'High'
    elif ph <= x['50%']:
        return 'Mod_High'
    elif ph <= x['75%']:
        return 'Medium'
    else:
        return 'Low'
wine['acidity_levels'] = wine['pH'].apply(levels)
x=wine.drop(columns=['fixed_acidity','volatile_acidity'])
print(x)