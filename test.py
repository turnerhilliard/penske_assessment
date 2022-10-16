import pandas as pd

def read_data(csv):
        all_data = pd.read_csv(csv)
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        return lap_data

data = read_data("/Users/turnerhilliard/Downloads/Chevrolet Detroit Grand Prix_Practice 2.csv")


# format_data = data.to_json(orient='records')
format_data = pd.DataFrame.to_json(data, orient='records')
print(format_data)



# /Users/turnerhilliard/Downloads/Chevrolet Detroit Grand Prix_Practice 2.csv

