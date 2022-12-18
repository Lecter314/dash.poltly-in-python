import pandas as pd
import numpy as np

#Reading a file
pth_a = './views/bike.xlsx' # Path to data
CARSA = pd.read_excel(pth_a)
# Transform data classes
CARSA = CARSA.astype({'temp':np.float64,'hum':np.float64,'windspeed':np.float64, 'cnt':np.float64,'season':'category',
                      'holiday':'category', 'weathersit':'category'})
df_d = CARSA.select_dtypes(include='float')
df_c = CARSA.select_dtypes(include='category')
df = CARSA.copy()