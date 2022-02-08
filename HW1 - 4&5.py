import numpy as np
import pandas as pd

# Problem 4, part c
i = 0
while i < 3:
    # create three 3 * 3 matrix in range [-10, 10]
    matrix = np.random.randint(-10, 10, size=(3, 3))
    # calculate the inverse of matrix
    inverse = np.linalg.inv(matrix)
    # compute the product of each matrix with its inverse
    product = np.matmul(matrix, inverse)
    print('matrix:\n', matrix)
    print('inverse matrix:\n', inverse)
    print('product check:\n', product)
    i += 1

    
# Problem 5
# part a
pd.set_option('max_columns', None)  # show all the columns to easier compare
houseData = pd.read_csv('C:/Users/zhaot/Desktop/DS4400/HW1 data/kc_house_data.csv', index_col=False, delimiter=',')
houseData = houseData.drop(columns=['id', 'date', 'zipcode'])
value = houseData.agg(['mean', 'max', 'min', 'var'])
highAve = houseData.mean().max()
lowAve = houseData.mean().min()
highVar = houseData.var().max()
lowVar = houseData.var().min()
print(value)
print('highest average is:', highAve, ' for the feature price')
print('lowest average is:', lowAve, ' for the feature long')
print('highest variance is:', highVar, ' for the feature price')
print('lowest variance is:', lowVar, ' for the feature waterfront')
# part b and c
correlation = houseData.corr()
print(correlation > 0)
print('True represents the two features have positive correlation.\n'
      'False represents the two features have negative correlation.')
