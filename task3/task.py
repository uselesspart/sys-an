import io
import numpy as np
import csv


def task(file_path):
    with open(file_path, 'r') as csvfile:
        r = csv.reader(csvfile, delimiter=';')
        rows = [row for row in r]
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerows(rows)

    csv_string = output.getvalue().strip()
    f = io.StringIO(csv_string)
    r = csv.reader(f, delimiter=',')
    matrix = np.array([[int(num) for num in row] for row in r])
    a, b = matrix.shape
    e = 0
    for j in range(a):
        for i in range(b):
            l_ij = matrix[j, i]
            if l_ij != 0: 
                e -= (l_ij / (a - 1)) * np.log2(l_ij / (b - 1))

    return round(e, 1)

def main():
    print(task("example.csv"))

if __name__ == "__main__":
    main()