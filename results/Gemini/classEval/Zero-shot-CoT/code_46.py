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
                y_interp.append(y[0])
            elif x_i >= x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        y_i = y[i] + (y[i + 1] - y[i]) * (x_i - x[i]) / (x[i + 1] - x[i])
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
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]

        """
        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            if x_i <= x[0] or x_i >= x[-1] or y_i <= y[0] or y_i >= y[-1]:
                continue

            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x_index_low = i
                    break
            else:
                continue

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y_index_low = j
                    break
            else:
                continue

            z_00 = z[x_index_low][y_index_low]
            z_01 = z[x_index_low][y_index_low + 1]
            z_10 = z[x_index_low + 1][y_index_low]
            z_11 = z[x_index_low + 1][y_index_low + 1]

            x1 = x[x_index_low]
            x2 = x[x_index_low + 1]
            y1 = y[y_index_low]
            y2 = y[y_index_low + 1]

            z_interp_val = (z_00 * (x2 - x_i) * (y2 - y_i) +
                             z_10 * (x_i - x1) * (y2 - y_i) +
                             z_01 * (x2 - x_i) * (y_i - y1) +
                             z_11 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))
            z_interp.append(z_interp_val)

        return z_interp