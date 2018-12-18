import plotly
import plotly.graph_objs as go
import re



dataset = dict()


with open("C:\\Users\\shand\\PycharmProjects\\test\\smth\\dataset.csv")as file:
    file.readline()

    for line in file:
        columns = line.split(',')

        name = columns[1]
        country = columns[11]
        goal = columns[6]
        if country not in dataset:
            dataset[country] = list()
        if name not in dataset[country]:
            dataset[country].append(name)




roundDiag = [go.pie(x = list(dataset.keys()),
                    y = list(dataset.values()))]
plotly.offline.plot(roundDiag, filename="2diagram.html")