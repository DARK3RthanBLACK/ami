import pandas as pd
import numpy as np
def ordinal_encoding(series):
   
    unique_values = series.unique()
   
    value_to_ordinal = {value: idx for idx, value in enumerate(unique_values)}
    
   
    encoded_series = series.map(value_to_ordinal)
    
    return encoded_series

# Example usage
data = pd.Series(['low', 'medium', 'high', 'medium', 'low'])
encoded_data = ordinal_encoding(data)
print(encoded_data)


def one_hot_encoding(series):
  
    unique_values = series.unique()
    
    
    one_hot_df = pd.DataFrame(0, index=series.index, columns=unique_values)
    
    
    for idx, value in enumerate(series):
        one_hot_df.loc[idx, value] = 1
    
    return one_hot_df


data = pd.Series(['cat', 'dog', 'bird', 'dog', 'cat'])
encoded_data = one_hot_encoding(data)
print(encoded_data)
