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

        #  Sorting the data
        final_frame = pd.DataFrame()
        for i in range (1,8):
                sector_string = "S"+ str(i)
                sector_lap_data = newlapFrame.loc[all_data['ShortName'] == sector_string]
                sector_sorted_data = sector_lap_data.nsmallest(len(all_data),'Time')
                sector_ranked = sector_sorted_data.drop_duplicates(subset=['ShortName'], keep='first')
                final_frame = pd.concat([final_frame, sector_ranked])


        return final_frame


newfloatFrame = fixData(data)
fastTimes = np.round(newfloatFrame['Time'].sum(), 3)
print(newfloatFrame)
print(fastTimes)

