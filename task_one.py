import requests
reqGet = requests.get('https://jsonplaceholder.typicode.com/todos')
jsonData = reqGet.json()

print("================================")
print(jsonData[0])
print("================================")
columns = []
for key in jsonData[0].keys():
    columns.append(key)
for i, n in enumerate(columns):
    print(f"Column index: {i}, name: {n}")
print("================================")
print(f"Number of rows in data: {len(jsonData)}")
print("================================")
titlesList = []
for i in range(len(jsonData)):
    if 'qui' in jsonData[i]['title']:
        titlesList.append(jsonData[i]['title'])
print("================================")
for i, n in enumerate(titlesList):
    print(f"Column index: {i}, name: {n}")
print("================================")
print(f"Number of rows in data where 'title' has 'qui': {len(titlesList)}")
print("================================")
titlesOfTypeInt = []
for i in range(len(titlesList)):
    if isinstance(titlesList[i], int):
        titlesOfTypeInt.append(titlesList[i])
if len(titlesOfTypeInt)==0:
    print("Found No Titles of type Int")
else:
    print(f"List of titles of type int{titlesOfTypeInt}")
    

