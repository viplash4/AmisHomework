import plotly
import plotly.graph_objs as go
import re
def getCountry(line):
    result = re.split(r",",line,maxsplit=1)
    return result[0], result[1]
def getName(line):
    result = re.split(r",",line, maxsplit=1)
    return result[0], result[1]
dataset = dict()
current_line = 0
try:
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

except ValueError as value_error:
    print(value_error)
for key in dataset:
    dataset[key] = len(dataset[key])
diagram = [go.Bar(x = list(dataset.keys()),
                  y = list(dataset.values()))]
plotly.offline.plot(diagram, filename="1diagram.html")




