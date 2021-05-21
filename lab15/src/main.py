import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math as m


def graphs():
    # Y(x)=10*cos(x^2)/x^2, x=[0...4]

    x1 = np.arange(1.0, 5.0, 0.1)
    y1 = []

    for X in x1:
        Y = (10 * m.cos(X ** 2)) / X ** 2
        y1.append(Y)

    figA, axe = plt.subplots()
    axe.plot(x1, y1, marker='o')
    axe.set_xlabel('x')
    axe.set_ylabel('y')
    figA.savefig('A.png')

    # Y(x)=5*sin(x)*cos(x^2+1/x)^2, x=[1...10]

    x2 = np.arange(1.0, 10.0, 0.1)
    y2 = []

    for X in x2:
        Y = 5 * m.sin(X) * (m.cos((X ** 2 + 1) / X) ** 2)
        y2.append(Y)

    figB = px.line(x=x2, y=y2)

    figB.write_html('B.html')
    figB.write_image('B.pdf')

    # CSV

    df = pd.read_csv('../../lab13_14/src/api.csv', usecols=['title', 'first_publish_year'])
    figCSV = make_subplots(rows=2, cols=1, subplot_titles=['BooksInYear', 'CountTitles'])

    publishes = set(df['first_publish_year'])
    publish_count = [0] * len(publishes)
    result_publishes = {}
    k = 0

    for year in publishes:
        for i in df['first_publish_year']:
            if i == year:
                publish_count[k] += 1

        result_publishes[year] = publish_count[k]
        k += 1

    del result_publishes[0]

    figCSV.append_trace(go.Bar(x=list(result_publishes.keys()), y=list(result_publishes.values()), name='Count Of Publishes'), row=1, col=1)

    titles = set(df['title'])
    title_count = [0] * len(titles)
    result_titles = {}
    k = 0

    for book in titles:
        for i in df['title']:
            if i == book:
                title_count[k] += 1

        result_titles[book] = title_count[k]
        k += 1

    figCSV.append_trace(go.Scatter(x=list(result_titles.keys()), y=list(result_titles.values()), name='Count Of Titles'), row=2, col=1)
    figCSV.update_layout(height=2000, xaxis_title='Year', yaxis_title='Count', xaxis2_title='Title', yaxis2_title='Count')
    figCSV.show()


if __name__ == '__main__':
    graphs()