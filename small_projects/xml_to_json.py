import xmltodict
import json
# import pprint
import pandas as pd

# Read XML data from a file

with open('doc/file.xml', 'r') as file:
    xml_data = file.read()

# Convert XML to OrderedDict
ordered_dict = xmltodict.parse(xml_data)

t_data = []
columns = ["Stock", "Trade", "Account", "Date", "Status"]
# Convert OrderedDict to JSON
json_data = json.dumps(ordered_dict, indent=2)
data = json.loads(json_data)
# pprint.pprint(data.get("div"))
# Print or use the JSON data as needed
for rec in data.get("div").get("div"):
    # print("stock: ", rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[0].get("span")[0].get("#text"),
    #       "Trade: ", rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[0].get("span")[1].get("#text"),
    #       "Date: ", rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[1].get("#text").split('|'),
    #       rec.get("span").get("div").get("button").get("div").get("div")[1].get("span")[0].get("#text"))
    t_data.append({"Stock":
                       rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[0].get("span")[
                           0].get("#text"),
                   "Trade":
                       rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[0].get("span")[
                           1].get("#text"),
                   "Account": rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[1].get(
                       "#text").split('|')[0],
                   "Date": rec.get("span").get("div").get("button").get("div").get("div")[0].get("span")[1].get(
                       "#text").split('|')[1],
                   "Status": rec.get("span").get("div").get("button").get("div").get("div")[1].get("span")[0].get(
                       "#text")})

df = pd.DataFrame(t_data)
print("DataFrame:", df)
df.to_csv('trades.csv')
