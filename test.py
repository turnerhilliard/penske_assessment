import pandas as pd
import numpy as np
def read_data(csv):
        all_data = pd.read_csv(csv)
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        return lap_data

data = read_data("/Users/turnerhilliard/Downloads/Chevrolet Detroit Grand Prix_Practice 2 (1).csv")
def fixData(data):
        newFrame = data.loc[~np.isnan(pd.to_numeric(data['CarNumber'], errors='coerce')),:]
        newnewFrame = newFrame.astype({'CarNumber': int}, errors='ignore')

        # floatFrame = newnewFrame.loc[newnewFrame['Time'].apply(type) != float]
        floatFrame = data.loc[~np.isnan(pd.to_numeric(data['Time'], errors='coerce')),:]
        newfloatFrame = floatFrame.astype({'Time': float}, errors='ignore')
        return newfloatFrame

newfloatFrame = fixData(data)
print(newfloatFrame)
print(newfloatFrame.dtypes)

