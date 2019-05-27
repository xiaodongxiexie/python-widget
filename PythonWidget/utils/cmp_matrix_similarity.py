"""
比较矩阵相似度。
针对同一位置相同元素才算是相似。
"""


def cmp_matrix(matrix1, matrix2):
    """
    将矩阵细分，比较最大相似，可以解决上面的算法出现的问题
    TODO: 这种耗时比较久
    """
    shape1, shape2 = matrix1.shape
    shape3, shape4 = matrix2.shape

    similarity = 0.0
    for I in range(2, shape1+1):
        for J in range(2, shape2+1):
            for M in range(2, shape3+1):
                for N in range(2, shape4+1):
                    for i in range(shape1-I+1):
                        for j in range(shape2-J+1):
                            tmp_matrix1 = matrix1[i:i+I, j:j+J]
                            for m in range(shape3-M+1):
                                for n in range(shape4-N+1):
                                    tmp_matrix2 = matrix2[m:m+M, n:n+N]
                                    if tmp_matrix1.shape == tmp_matrix2.shape:
                                        cur_similarity = (tmp_matrix1 == tmp_matrix2).sum()/(max(shape1, shape3) * max(shape2, shape4))
                                        if cur_similarity > similarity:
                                            similarity = cur_similarity
    return similarity


# TODO 提前终止
# 对上一算法进行优化，提前终止，提速
def cmp_matrix_fast(matrix1, matrix2, step=1):
    shape1, shape2 = matrix1.shape
    shape3, shape4 = matrix2.shape

    similarity = 0.0
    for I in range(shape1, 1, -step):
        for J in range(shape2, 1, -step):
            for M in range(shape3, 1, -step):
                for N in range(shape4, 1, -step):
                    for i in range(shape1-I+1):
                        for j in range(shape2-J+1):
                            tmp_matrix1 = matrix1[i:i+I, j:j+J]
                            for m in range(shape3-M+1):
                                for n in range(shape4-N+1):
                                    tmp_matrix2 = matrix2[m:m+M, n:n+N]
                                    if tmp_matrix1.shape == tmp_matrix2.shape:
                                        cur_similarity = (tmp_matrix1 == tmp_matrix2).sum()/( max(shape1, shape3) * max(shape2, shape4))
                                        if cur_similarity > similarity:
                                            similarity = cur_similarity
                    if similarity >= min(M*N, I*J)/max(M*N, I*J):
                        break
                if similarity >= min(M*N, I*J)/max(M*N, I*J):
                    break
            if similarity >= min(M*N, I*J)/max(M*N, I*J):
                break
        if similarity >= min(M*N, I*J)/max(M*N, I*J):
            break
    return similarity


# TODO 提前终止
def cmp_matrix_f(matrix1, matrix2, step=1):
    shape1, shape2 = matrix1.shape
    shape3, shape4 = matrix2.shape

    similarity = 0.0
    for I in range(shape1, 1, -step):
        for J in range(shape2, 1, -step):
            for M in range(shape3, 1, -step):
                for N in range(shape4, 1, -step):
                    for i in range(shape1-I, -1, -1):
                        for j in range(shape2-J, -1, -1):
                            tmp_matrix1 = matrix1[i:i+I, j:j+J]
                            for m in range(shape3-M, -1, -1):
                                for n in range(shape4-N, -1, -1):
                                    tmp_matrix2 = matrix2[m:m+M, n:n+N]
                                    if tmp_matrix1.shape == tmp_matrix2.shape:
                                        cur_similarity = (tmp_matrix1 == tmp_matrix2).sum()/( max(shape1, shape3) * max(shape2, shape4))
                                        if cur_similarity > similarity:
                                            similarity = cur_similarity
                    if similarity >= min(M*N, I*J)/max(M*N, I*J):
                        break
                if similarity >= min(M*N, I*J)/max(M*N, I*J):
                    break
            if similarity >= min(M*N, I*J)/max(M*N, I*J):
                break
        if similarity >= min(M*N, I*J)/max(M*N, I*J):
            break
    return similarity


if __name__ == "__main__":
    import numpy as np

    arr = np.arange(24).reshape(4,6)
    arr2 = np.roll(arr, 1, axis=0)
    print(cmp_matrix(arr, arr2))
    print(cmp_matrix_f(arr, arr2))
    print(cmp_matrix_fast(arr, arr2))