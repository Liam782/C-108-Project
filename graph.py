import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
rating_list = df["Avg Rating"].tolist()

fig = ff.create_distplot([rating_list], ["Brand"], show_hist = False)
fig.show()