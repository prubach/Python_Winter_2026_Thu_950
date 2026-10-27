import numpy as np



def gen_matrix(n):
    matrix = []
    for i in range(n):
        #matrix.append(np.random.randint(10000, size=(10000, 10000)))
        matrix.append(np.random.randint(10000, size=(10000, 10000)))
    return matrix

def sum_rows_singleline(points):
    # return a list containing the sums of each row in input 2D list (points)
    return [sum(row) for row in points]

def sum_cols_zip(points):
    return sum_rows_singleline(list(zip(*points)))

def sum_rows_cols(points):
    return sum_rows_singleline(points), sum_cols_zip(points)

def sum_rows_np(points):
    return np.sum(points, axis=1)

def sum_cols_np(points):
    return np.sum(points, axis=0)

def sum_rows_cols_np(points):
    return sum_rows_np(points).tolist(), sum_cols_np(points).tolist()

if __name__=='__main__':
    points = [[3, 5, 3, 6],
              [7, 5, 8, 7],
              [4, 8, 9, 4]]

    #mat = gen_matrix(2)
    #print(mat)
    s_r, s_c = sum_rows_cols(points)
    print(s_r, s_c)
    s_r, s_c = sum_rows_cols_np(points)
    print(s_r, s_c)
    #s_r, s_c = sum_cols_zip(points)
    #print(s_c)
    #print(sum_rows_cols(points))