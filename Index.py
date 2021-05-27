import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd 
import csv

df = pd.read_csv("medium_data.csv")
data = df["id"].tolist()

population_mean = statistics.mean(data)
print("Population mean :-",population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        rand_index = random.randint(0,len(data)-1)
        value = data[rand_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df= mean_list
    fig = ff.create_distplot([df],["Average"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
setup()


def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("sampling Mean :-",std_deviation)

standard_deviation()
    


