import pandas as pd
import numpy as np
import csv

def task(path):
    df = pd.read_csv(path)
    
    df.columns = ['parent', 'child']

    matrix = []

    for i in range(1, df['child'].max() + 1):
        r1 = df[df['parent'] == i]['child'].count()
        r2 = df[df['child'] == i]['parent'].count()
        r3 = df[df['parent'].isin(df[df['parent'] == i]['child'])]['child'].count()
        r4 = df[df['child'].isin(df[df['child'] == i]['parent'])]['parent'].count()
        r5 = df[df['parent'].isin(df[df['child'] == i]['parent'])]['child'].count()
        
        if r5 != 0:
            r5 -= 1

        matrix.append([r1, r2, r3, r4, r5])

    del matrix[0]

    return np.matrix(matrix)

def main():
    print(task('example.csv'))  

if __name__ == "__main__":
    main()