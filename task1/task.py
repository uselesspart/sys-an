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
        result = des_csv(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "json":
        result = des_json(sys.argv[2], sys.argv[3])
    print(result)

if __name__ == "__main__":
    main()