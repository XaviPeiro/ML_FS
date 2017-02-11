# http://machinelearningmastery.com/machine-learning-in-python-step-by-step/ tutorial

# Load libs loader
from load_libraries import *

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)