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
                for i in range(len(x) - 1):
                    for j in range(len(y) - 1):
                        if x[i] <= x_i <= x[i + 1] and y[j] <= y_j <= y[j + 1]:
                            z_ij = z[i][j] + (x_i - x[i]) * (z[i + 1][j] - z[i][j]) / (x[i + 1] - x[i]) + \
                                   (y_j - y[j]) * (z[i][j + 1] - z[i][j]) / (y[j + 1] - y[j]) + \
                                   (x_i - x[i]) * (y_j - y[j]) * (z[i + 1][j + 1] - z[i + 1][j] - z[i][j + 1] + z[i][j]) / \
                                   ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                            z_interp.append(z_ij)
                            break
                    else:
                        continue
                    break
        return z_interp