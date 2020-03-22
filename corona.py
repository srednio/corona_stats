import json

with open('data/timeseries.json') as json_file:
    data = json.load(json_file)

print('loading done')

print(data["Poland"])
for x in (data["Poland"]):
    print(x)

print(data["Poland"][59])
print(len(data["Poland"]))

i = 1
for x in {"Poland", "Germany", "Korea, South", "United Kingdom", "France", "Spain"}:
    l = len(data[x])
    first_count = 0
    second_count = 0
    for a in range(0, l):
        if data[x][a]["confirmed"] >= 200:
            current = data[x][l - 1]
            death_ratio = current["deaths"] / current["confirmed"]
            print(i, x, first_count, second_count, '{:.2f}'.format(death_ratio * 100))
            if l - a > 5:
                print(data[x][a + 5]["confirmed"])
            i += 1
            break
        if data[x][a]["confirmed"] >= 100:
            second_count += 1
        elif data[x][a]["confirmed"] > 10:
            first_count += 1

print(data["Germany"][54])
