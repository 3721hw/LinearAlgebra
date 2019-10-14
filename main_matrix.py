from playLA.Matrix import Matirx

if __name__ == "__main__":

    matrix = Matirx([[1, 2],[3, 4]])
    print(matrix)
    print("Matrix.shape  = {}".format(matrix.shape()))
    print("Matrix.size  = {}".format(matrix.size()))
    print("len(Matrix)  = {}".format(len(matrix)))
    print("Matrix[0][0]  = {}".format(matrix[0, 0]))
    print("Matrix col_vector[1] = {}".format(matrix.col_vector(1)))





