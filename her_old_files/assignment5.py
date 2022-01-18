from datetime import datetime as dt
import csv
import xlwt
from tempfile import TemporaryFile as TF

read_file = open("C:/python/Rawfile.txt", mode ="r", encoding = "utf-8")

whole_data = read_file.readlines()
# print(len(whole_data))
# print(whole_data[:5])

#to remove the unwanted '\n' from every entry in the data
refined_data = [entry.rstrip("\n") for entry in whole_data]
# print(refined_data[:5])

# sorted explained
# amala = [("High", 3), ("Low", 2), ("nan", 6)]
# bruh = sorted(amala, key = lambda a: a[1])
# print(bruh)

# to sort according to date
sorted_refined_data = sorted(refined_data, key = lambda a: dt.strptime(a.split(" on ")[1], "%d-%m-%Y"))
# print(sorted_refined_data[-5:])

list_of_names = []
list_sales = [] 
list_of_dates = []

for entry in sorted_refined_data:
    extracted_name = entry.split(" : ")[0]
    list_of_names.append(extracted_name)

    extracted_sales = int(entry.split(" ")[3].lstrip("₦"))
    list_sales.append(extracted_sales)

    extracted_dates = entry.split(" on ")[1].replace("-", "/")
    list_of_dates.append(extracted_dates)
    # print(extracted_sales)

new_file = open("C:/python/raveurban.csv", mode = "w", encoding = "utf-8", newline = "")

pen = csv.writer(new_file)
pen.writerow(["name", "sales", "date"])

# for num in range(len(sorted_refined_data)):
#     pen.writerow([list_of_names[num], list_sales[num], list_of_dates[num]])

# new_file.close()

listt = set(list_of_names)
print(len(listt))

name_sales ={}
for name, amount in zip(list_of_names, list_sales):
    name_sales[name] = name_sales.get(name,0) + amount
# print(len(name_sales))
sorted_name_sales = dict(sorted(name_sales.items(), key = lambda a : a[0]))
# print(sorted_name_sales)


# 5a
sorts = dict(sorted(name_sales.items(), key = lambda a: a[1], reverse = True))
best_performing = list(sorts)
# print(sorts)
best_performing[:10]
best_performing = [(key, value) for key, value in sorts.items()]
print(best_performing[:10])


# 5b
work = list(map(lambda a: str(a), list_of_dates))
print(work)
print(len(work))
works = list(map(lambda x: x.split("/")[1], work))
print(works)
print(len(works))
wors = list(map(lambda s: dt.strptime(s, "%m"), works))
print(len(wors))
wow = list(map(lambda k: k.strftime("%B"), wors))
print(len(wow))
print(wow)
tip ={}
for month, amount in zip(wow, list_sales):
    tip[month] = tip.get(month, 0) + amount
done = [(key, values) for key, values in tip.items()]
print(done)

# 5c
sales = sorted(done, key = lambda p: p[1])
print(sales)
low = sales[0][0]
high = sales[-1][0]
print(f"{low} is the month with the lowest sales and {high} is the month with the highest sales")

# 5d
sort_agent_names = dict(sorted(name_sales.items(), key = lambda d: d[0]))
print(sort_agent_names)
agent_names = list(sort_agent_names.keys())
agent_sales = list(sort_agent_names.values())
agent_commission = [amount * 0.055 for amount in agent_sales]

reel = {}
for names, commission in zip(agent_names, agent_commission):
    reel[names] = reel.get(names, 0) + commission
print(reel)
print(len(reel))