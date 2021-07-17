class Matrix:

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        try:
            for i in range(len(self.data)):
                for k in range(len(self.data[i])):
                    self.data[i][k] += other.data[i][k]
        except IndexError:
            print('В линейной алгебре разрешается складывать матрицы только одинакового размера')
            return None
        else:
            return Matrix(self.data)

    def matrix_build(self):
        matrix = ''
        for row_ in self.data:
            row = map(str, row_)
            matrix += f"| {' '.join(row)} |\n"
        return matrix

    def __str__(self):
        return Matrix.matrix_build(self)


some_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 11, 14, 15], [2, 3]]
some_other = [[1, 4, 5, 2], [7, 8, 6, 4], [3, 1, 5, 7], [2, 2]]
print(Matrix(some_list))
print(Matrix(some_list) + Matrix(some_other))
