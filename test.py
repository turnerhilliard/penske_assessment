from re import I
import pandas as pd
import numpy as np
def read_data(csv):
        all_data = pd.read_csv(csv)
        return all_data

data = read_data("/Users/turnerhilliard/Downloads/Chevrolet Detroit Grand Prix_Practice 2.csv")
def fixData(all_data):
        newFrame = all_data.loc[~np.isnan(pd.to_numeric(all_data['CarNumber'], errors='coerce')),:]
        correctedFrame = newFrame.astype({'CarNumber': int}, errors='ignore')
        floatFrame = correctedFrame.loc[~np.isnan(pd.to_numeric(correctedFrame['Time'], errors='coerce')),:]
        newfloatFrame = floatFrame.astype({'Time': float}, errors='ignore')
        entryFrame = newfloatFrame.loc[~np.isnan(pd.to_numeric(newfloatFrame['EntryTime'], errors='coerce')),:]
        newentryFrame = entryFrame.astype({'EntryTime': float}, errors='ignore')
        exitFrame = newentryFrame.loc[~np.isnan(pd.to_numeric(newentryFrame['ExitTime'], errors='coerce')),:]
        newexitFrame = exitFrame.astype({'ExitTime': float}, errors='ignore')
        lapFrame = newexitFrame.loc[~np.isnan(pd.to_numeric(newexitFrame['Lap'], errors='coerce')),:]
        newlapFrame = lapFrame.astype({'Lap': int}, errors='ignore')

        return newlapFrame

def superLapSorter(newlapFrame):
        lap_data = newlapFrame.loc[newlapFrame['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(len(newlapFrame),'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')
        
        return ranked


newfloatFrame = fixData(data)
newnewfloatFrame = superLapSorter(newfloatFrame)

newnewfloatFrame.astype({'Flag':'string','LastName':'string'})

print(newnewfloatFrame)
newnewfloatFrame.dtypes()



