class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        """
        y_interp = []
        for x_i in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    y_i = y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    y_interp.append(y_i)
                    break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        """
        z_interp = []
        for x_i in x_interp:
            for y_j in y_interp:
                x_index = -1
                y_index = -1

                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        x_index = i
                        break

                for j in range(len(y) - 1):
                    if y[j] <= y_j <= y[j + 1]:
                        y_index = j
                        break

                if x_index != -1 and y_index != -1:
                    z_ij = z[x_index][y_index] + (x_i - x[x_index]) * (z[x_index + 1][y_index] - z[x_index][y_index]) / (
                            x[x_index + 1] - x[x_index]) + \
                           (y_j - y[y_index]) * (z[x_index][y_index + 1] - z[x_index][y_index]) / (
                                   y[y_index + 1] - y[y_index])
                    z_interp.append(z_ij)
        return z_interp