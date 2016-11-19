#!/usr/bin/python


class Matrix(object):
    def __init__(self, *args):
        self.size = len(args) / 2
        if self.size % 2 != 0.0:
            print("Invalid number of arguments")
            pass
        self.matrix = [[[] for i in range(int(self.size))] for i in range(int(self.size))]
        for i in range(int(self.size)):
            for j in range(int(self.size)):
                self.matrix[i][j] = args[i + j]

    def __add__(self, other):
        if other.size != self.size:
            print("Invalid matrix size")
        else:
            result = [[0 for row in range(int(self.size))] for col in range(int(self.size))]
            for i in range(int(self.size)):
                for j in range(int(self.size)):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def mat_product(self, other):
        product = [[0 for row in range(int(self.size))] for col in range(int(self.size))]
        for i in range(int(self.size)):
            for j in range(int(self.size)):
                for k in range(int(self.size)):
                    product[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return product

    def __mul__(self, other):
        for i in range(int(self.size)):
            for j in range(int(self.size)):
                for k in range(int(self.size)):
                    self.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return self.matrix

    def __str__(self):
        matrix_str = ''
        for i in range(int(self.size)):
            for j in range(int(self.size)):
                matrix_str += (str(self.matrix[i][j]) + " ")
            matrix_str += "\n"
        return matrix_str

    def generator_matrix(self):
        for i in self.matrix:
            for j in i:
                yield j

    def generate_vector(self):
        for i in self.generator_matrix():
            print(i)


def main():
    matrix_1 = Matrix(4, 5, 6, 7)
    matrix_2 = Matrix(2, 2, 2, 1)

    print(matrix_1)
    print(matrix_2)

    matrix_3 = matrix_1 + matrix_2

    print(matrix_3)

    matrix_3 = matrix_1 * matrix_2
    print(matrix_3)

    print(matrix_1.mat_product(matrix_2))
    print(matrix_1.mat_product(matrix_2))

    matrix_1.generate_vector()

if __name__ == '__main__':
    main()
