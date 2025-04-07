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
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]

        """
        if not x or not y or not x_interp:
            return []

        y_interp = []
        for x_i in x_interp:
            if x_i <= x[0]:
                y_interp.append(y[0] + (x_i - x[0]) * (y[1] - y[0]) / (x[1] - x[0]))
            elif x_i >= x[-1]:
                y_interp.append(y[-2] + (x_i - x[-2]) * (y[-1] - y[-2]) / (x[-1] - x[-2]))
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        y_interp_i = y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_interp.append(y_interp_i)
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
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            x_lower_index = -1
            x_upper_index = -1
            y_lower_index = -1
            y_upper_index = -1

            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x_lower_index = i
                    x_upper_index = i + 1
                    break
            if x_lower_index == -1:
                if x_i <= x[0]:
                    x_lower_index = 0
                    x_upper_index = 1
                elif x_i >= x[-1]:
                    x_lower_index = len(x) - 2
                    x_upper_index = len(x) - 1
                else:
                    return []

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y_lower_index = j
                    y_upper_index = j + 1
                    break

            if y_lower_index == -1:
                if y_i <= y[0]:
                    y_lower_index = 0
                    y_upper_index = 1
                elif y_i >= y[-1]:
                    y_lower_index = len(y) - 2
                    y_upper_index = len(y) - 1
                else:
                    return []

            z1 = z[x_lower_index][y_lower_index] + (x_i - x[x_lower_index]) * (z[x_upper_index][y_lower_index] - z[x_lower_index][y_lower_index]) / (x[x_upper_index] - x[x_lower_index])
            z2 = z[x_lower_index][y_upper_index] + (x_i - x[x_lower_index]) * (z[x_upper_index][y_upper_index] - z[x_lower_index][y_upper_index]) / (x[x_upper_index] - x[x_lower_index])
            z_interp_i = z1 + (y_i - y[y_lower_index]) * (z2 - z1) / (y[y_upper_index] - y[y_lower_index])
            z_interp.append(z_interp_i)
        return z_interp