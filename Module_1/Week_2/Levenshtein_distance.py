def build_matrix_d (source, target):
    matrix_d = [[j if i == 0 else None for j in range(len(target) + 1)] for i in range(len(source) + 1)]
   
    for i in range(1, len(source) + 1):
        matrix_d[i][0] =  i

    refill_matrix(matrix_d, source, target)
    return matrix_d[-1][-1]


def refill_matrix (matrix_d, source, target):
    for i in range(len(matrix_d)):
        for j in range(len(matrix_d[0])):
            if source[i - 1] == target[j - 1] and matrix_d[i][j] == None:
                matrix_d[i][j] = matrix_d[i - 1][j - 1]
            elif matrix_d[i][j] == None:
                matrix_d[i][j] = 1 + min(matrix_d[i - 1][j],
                                         matrix_d[i][j - 1],
                                         matrix_d[i - 1][j - 1])
    return matrix_d

source = 'yu'
target = 'you'
print (f"Levenshtein Distance = {build_matrix_d(source, target)}")