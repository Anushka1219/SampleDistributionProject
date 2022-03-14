import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

sample=[]

df=pd.read_csv("medium_data.csv")
print(statistics.mean(df["claps"].tolist()))
print(statistics.stdev(df["claps"].tolist()))
fig=ff.create_distplot([df["claps"]],["average"])
fig.show()

for i in range(0,1000):
    randomindex=random.randint(0,len(df["claps"]))
    sample.append(df["claps"].tolist()[randomindex])

print(sample)
print(statistics.mean(sample))
print(statistics.stdev(sample))

fig=ff.create_distplot([sample],["average"])
fig.show()


