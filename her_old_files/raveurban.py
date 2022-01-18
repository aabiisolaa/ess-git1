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

###FIRST EXCEL SHEET DATA
agent_names = list(sorted_name_sales.keys())
agent_sales = list(sorted_name_sales.values())
agent_commission = [amount * 0.055 for amount in agent_sales]
total_sales = sum(agent_sales)
agent_contribution = list(map(lambda a : str(round((a /total_sales) * 100, 3)) + "%", agent_sales))


##SECOND EXCEL SHEET DATA
total_commission = sum(agent_commission)
total_revenue = sum(agent_sales)
net_revenue = total_revenue - total_commission


###GETTING THE BOOK
book = xlwt.Workbook()

###ADDING THE SHEETS
first_sheet = book.add_sheet("agents' records")
second_sheet = book.add_sheet("net income") 


###WRITING INTO THE FIRST SHEET
first_sheet.write(0, 0, "agent name")
first_sheet.write(0, 1, "agent sales")
first_sheet.write(0, 2, "agent commission")
first_sheet.write(0, 3, "agent contribution")

for index, entry in enumerate(agent_names):
    first_sheet.write(index + 1, 0, entry)

for index, entry in enumerate(agent_sales):
    first_sheet.write(index + 1, 1, entry)

for index, entry in enumerate(agent_commission):
    first_sheet.write(index + 1, 2, entry)

for index, entry in enumerate(agent_contribution):
    first_sheet.write(index +1, 3, entry)

###WRITING INTO THE SECOND SHEET
second_sheet.write(0, 0, "total revenue")
second_sheet.write(0, 1, "net revenue")
second_sheet.write(0, 2, "total commission")

second_sheet.write(1, 0, total_revenue)
second_sheet.write(1, 1, net_revenue)
second_sheet.write(1, 2, total_commission)

book.save("C:/python/raveurban_kalon.xls")
book.save(TF())