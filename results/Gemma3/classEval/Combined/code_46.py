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
        if not x or not y or len(x) != len(y):
            return []

        y_interp = []
        for x_val in x_interp:
            if x_val < x[0]:
                y_interp.append(y[0])
            elif x_val > x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_val <= x[i + 1]:
                        y_val = y[i] + (x_val - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_interp.append(y_val)
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
        if not x or not y or not z or len(x) != len(y) or len(x) != len(z) or len(y) != len(z[0]):
            return []

        z_interp = []
        for x_val, y_val in zip(x_interp, y_interp):
            if x_val < x[0] or y_val < y[0]:
                z_interp.append(z[0][0])
            elif x_val > x[-1] or y_val > y[-1]:
                z_interp.append(z[-1][-1])
            else:
                for i in range(len(x) - 1):
                    for j in range(len(y) - 1):
                        if x[i] <= x_val <= x[i + 1] and y[j] <= y_val <= y[j + 1]:
                            z_val = z[i][j] + (x_val - x[i]) * (z[i + 1][j] - z[i][j]) / (x[i + 1] - x[i]) + \
                                    (y_val - y[j]) * (z[i][j + 1] - z[i][j]) / (y[j + 1] - y[j])
                            z_interp.append(z_val)
                            break
                    else:
                        continue
                    break
        return z_interp