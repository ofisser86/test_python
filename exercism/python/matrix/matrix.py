class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")


    def row(self, index):
        pass


    def column(self, index):
        pass


matrix = Matrix("9 8 7\n1 2 3")
print(matrix.matrix_string)

