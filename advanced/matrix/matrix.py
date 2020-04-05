
class Matrix:

    def __init__(self,mat):
        self.mat = mat


    def tuples(self):
        """Displays matrix as a tuple"""
        return(tuple(self.mat))


    def __repr__(self):
        """print the matrix
                """
        return str(self.mat)


    def __add__(self, mat_2):
        """Addition matrix
                """
        if type(mat_2) == tuple:
            result = (tuple([self.mat[i][j] + mat_2[i][j] for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))
        else:
            mat_2 = mat_2.tuples()
            result = (tuple([self.mat[i][j] + mat_2[i][j] for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))

        return tuple(result)


    def __radd__(self, mat_2):
        """Addition matrix
                """
        if type(mat_2) == tuple:
            result = (tuple([self.mat[i][j] + mat_2[i][j] for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))
        else:
            mat_2 = mat_2.tuples()
            result = (tuple([self.mat[i][j] + mat_2[i][j] for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))

        return tuple(result)


    def __sub__(self, mat_2):
        """Subtraction matrix
                """
        if type(mat_2) == tuple:
            result = (tuple([self.mat[i][j] - mat_2[i][j] for j in range(len(self.mat[0]))]) for i in
                      range(len(self.mat)))
        else:
            mat_2 = mat_2.tuples()
            result = (tuple([self.mat[i][j] - mat_2[i][j] for j in range(len(self.mat[0]))]) for i in
                      range(len(self.mat)))

        return tuple(result)


    def __rsub__(self, mat_2):
        """Subtraction matrix
                """
        if type(mat_2) == tuple:
            result = (tuple([self.mat[i][j] - mat_2[i][j] for j in range(len(self.mat[0]))]) for i in
                      range(len(self.mat)))
        else:
            mat_2 = mat_2.tuples()
            result = (tuple([self.mat[i][j] - mat_2[i][j] for j in range(len(self.mat[0]))]) for i in
                      range(len(self.mat)))

        return tuple(result)


    def ones(self,row):
        """ones matrix
                        """
        one = 1
        result = (tuple([1 for j in range(row)]) for i in range(row))
        return tuple(result)


    def unity(self, row):
        """unity matrix
                               """
        one = 1
        result = (tuple([1 if i==j else 0 for j in range(row)])for i in range(row))
        return tuple(result)


    def __mul__(self,mat_2):
        """Multiplication matrices and Multiplication matrice by scalar
                               """
        if type(mat_2) == int:
            result = (tuple([self.mat[i][j]*mat_2 for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))

        elif type(mat_2) == tuple:
            result = (tuple([sum(a*b for a,b in zip(mat_row, mat_2_col)) for mat_2_col in zip(*mat_2)]) for  mat_row in self.mat)
        else:
            mat_2 = mat_2.tuples()
            result = (tuple([sum(a*b for a,b in zip(mat_row, mat_2_col)) for mat_2_col in zip(*mat_2)]) for  mat_row in self.mat)

        return tuple(result)


    def __rmul__(self, mat_2):
        """ Multiplication  scalar by matrice
                                       """
        result = (tuple([self.mat[i][j] * mat_2 for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))
        return tuple(result)


    def __truediv__(self, mat_2):
        """Multiplication Division by scalar
                                       """
        if mat_2 !=0:
            result = (tuple([self.mat[i][j] / mat_2 for j in range(len(self.mat[0]))]) for i in range(len(self.mat)))
            return tuple(result)
        else:
            result = 'error'
            return result


    def __hash__(self):
        """dictionary
                                               """
        return hash(self.mat)


    def __eq__(self, mat_2):
        """check matrices Comparision
                                               """
        mat_2 = mat_2.tuples()
        flaf_dif = 0
        for i in range(len(self.mat)):
            if flaf_dif == 1:
             break
            for j in range(len(self.mat)):
                 if self.mat[i][j] == mat_2[i][j]:
                     result = True
                     flaf_dif = 0
                 else:
                    result = False
                    flaf_dif = 1
                    break

        return result