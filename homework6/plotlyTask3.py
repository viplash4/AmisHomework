import re
import plotly
import plotly.graph_objs as go
with open("C:\\Users\\shand\\PycharmProjects\\AmisHomework\\homework6\\dataset.csv") as file:
    dataset = dict()
    file.readline()

    for line in file:
        columns = line.split(",")

        country = columns[11]
        category = columns[2]
        name = columns[1]
        goal = columns[6]
        if country not in dataset:
            dataset[country] = dict()
        if category not in dataset[country]:
            dataset[country][category] = dict()
        if name not in dataset[country][category]:
            dataset[country][category][name] = goal

diagram = [go.Bar(x = list(dataset[country][category].keys()),
                  y = list(dataset[country][category].values()))]
plotly.offline.plot(diagram, filename="3diagram.html")