import csv
import json
import sys

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
    return data[path]

def main():
    if sys.argv[1] == "csv":
        result = des_csv("example.csv", 2, 2)
    elif sys.argv[1] == "json":
        result = des_json("example.json", "str")
    print(result)

if __name__ == "__main__":
    main()