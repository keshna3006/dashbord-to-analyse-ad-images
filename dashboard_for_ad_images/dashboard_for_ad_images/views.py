import pandas as pd
import webbrowser
csv_file_path='sample.csv'
dataframe=pd.read_csv(csv_file_path)
column=dataframe['creative_img']
print(column)


