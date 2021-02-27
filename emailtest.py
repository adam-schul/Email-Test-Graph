
import numpy as np
import matplotlib.pyplot as plt
import sys, csv
from matplotlib.pyplot import xkcd

# Create empty lists for data
grade = []
control = []
ego = []
incentive = []
herd = []

# Read the data from the csv file and put it into a variable called "data"
with open('emailtest.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Sort the data into the more specific lists
for i in range(len(data)):
    if i == 0:
        pass
    else:
        grade.append(data[i][0])
        control.append(float(data[i][1]))
        ego.append(float(data[i][2]))
        incentive.append(float(data[i][3]))
        herd.append(float(data[i][4]))

# Calculate the average of each treatment's proportion
control_avg = sum(control) / len(control)
ego_avg = sum(ego) / len(ego)
incentive_avg = sum(incentive) / len(incentive)
herd_avg = sum(herd) / len(herd)

# Create a range of numbers based on the number of grades to be used later to place the x-ticks
n_grades = int(len(grade))
index = np.arange(n_grades)

# Change colors
Herd_color = 'green'
Control_color = 'yellow'
Ego_color = 'blue'
Incentive_color = 'red'

Highlight_color = 'yellow'
Background = '#a4ede4'

# Edit the fonts to be used later
csfont = {'fontname': 'Orator Std', 'weight': 'heavy', 'size': 22, 'backgroundcolor': Highlight_color}
psfont = {'fontname': 'Orator Std', 'size': 14}

# Width of bars
width = 0.2
opacity = 0.7
fruit = index

# Set size of figure and color of background
fig = plt.figure(figsize=(12, 8), facecolor=Background)

wego = 0
wcontrol = 0
wincentive = 0
wherd = 0

# Order the bars from tallest to shortest based on the averages calculated earlier
for i in range(n_grades):
    if incentive_avg > herd_avg and incentive_avg > ego_avg and incentive_avg > control_avg:
        wincentive = fruit
        incentive_avg = 0
        fruit = fruit + width

    elif herd_avg > incentive_avg and herd_avg > ego_avg and herd_avg > control_avg:
        wherd = fruit
        herd_avg = 0
        fruit = fruit + width

    elif ego_avg > incentive_avg and ego_avg > herd_avg and ego_avg > control_avg:
        wego = fruit
        ego_avg = 0
        fruit = fruit + width

    elif control_avg > incentive_avg and control_avg > herd_avg and control_avg > ego_avg:
        wcontrol = fruit
        control_avg = 0
        fruit = fruit + width

    else:
        pass

# Create the bars of the graph
pcontrol = plt.bar(wcontrol, control, width, color=Control_color, alpha=opacity, edgecolor='navy', label='Control')
pego = plt.bar(wego, ego, width, color=Ego_color, alpha=opacity, edgecolor='navy', label='Ego')
pincentive = plt.bar(wincentive, incentive, width, color=Incentive_color, alpha=opacity, edgecolor='navy',
                     label='Incentive')
pherd = plt.bar(wherd, herd, width, color=Herd_color, alpha=opacity, edgecolor='navy', label='Herd')

# Put final details onto the graph
plt.xlabel("Grade", **csfont)
plt.ylabel("Response Rate (%)", **csfont)
plt.xticks(index + width + (width / 2), grade, **psfont)
plt.title("Effect of Different Subject Lines on Responsiveness", **csfont)
plt.legend()

# Show the graph
plt.show()
