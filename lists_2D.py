points = [[3, 5, 3],
          [7, 5, 8],
          [4, 8, 9]]

print(points[1][0])
print(type(points[1][0]))
print(points[1])
print(type(points[1]))

def sum_rows(points):
    # return a list containing the sums of each row in input 2D list (points)
    row_sum = []
    for row in points:
        row_sum.append(sum(row))
    return row_sum

def sum_rows_singleline(points):
    # return a list containing the sums of each row in input 2D list (points)
    return [sum(row) for row in points]


#def sum_cols(points):
    # return a list containing the sums of each column in input 2D list (points)

#def sum_all(points):
    # return a number - sum of all elements in input 2D list (points)


print('-'*60)
print(points)
print(f'sum rows: {sum_rows(points)}')
print(f'sum rows: {sum_rows_singleline(points)}')

print('-'*60)
l_1 = [1, 2, 3]
l_2 = [x*x for x in l_1]
print(l_1)
print(l_2)
