import pandas

data = pandas.read_csv ("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_s = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_s= len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s = len(data[data["Primary Fur Color"] == "Black"])

new_census = {
    "Fun Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_s, cinnamon_s, black_s]

}

new_frame = pandas.DataFrame(new_census)
new_frame.to_csv("squirrel_count.csv")
print(new_frame)