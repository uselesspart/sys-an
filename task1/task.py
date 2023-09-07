import csv
import json
import sys
from jsonpath_ng import jsonpath, parse

def des_csv(s, a, b):
    data = []
    with open(s, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data[a][b]

def des_json(s, path):
    with open(s) as file:
        data = json.load(file)
    jsonpath_expression = parse(path)
    m = jsonpath_expression.find(data)
    return m

def main():
    if sys.argv[1] == "csv":
        result = des_csv("example.csv", int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "json":
        result = des_json("example.json", sys.argv[2])
    print(result)

if __name__ == "__main__":
    main()