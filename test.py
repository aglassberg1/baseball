import numpy as np
import pandas as pd
from IPython.display import display


df=pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\NYA2022.ros", header=None,
               names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position'])

display(df.head(10))
