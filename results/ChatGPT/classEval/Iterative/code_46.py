class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data.
    """

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data.
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :return: The y-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]
        """
        if not x_interp or not x or not y or len(x) != len(y):
            return []

        y_interp = []
        for xi in x_interp:
            if xi < x[0]:
                # Extrapolate before the first point
                y_interp.append(y[0] + (y[1] - y[0]) * ((xi - x[0]) / (x[1] - x[0])))
            elif xi > x[-1]:
                # Extrapolate after the last point
                y_interp.append(y[-1] + (y[-1] - y[-2]) * ((xi - x[-1]) / (x[-1] - x[-2])))
            else:
                for i in range(len(x) - 1):
                    if x[i] <= xi <= x[i + 1]:
                        y_interp.append(y[i] + (y[i + 1] - y[i]) * ((xi - x[i]) / (x[i + 1] - x[i])))
                        break
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data.
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
        if not x_interp or not y_interp or not x or not y or not z or len(x) != len(z[0]) or len(y) != len(z):
            return []

        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                z_interp.append(None)
                continue
            
            # Perform bilinear interpolation
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        q11 = z[j][i]
                        q21 = z[j][i + 1]
                        q12 = z[j + 1][i]
                        q22 = z[j + 1][i + 1]

                        z_interp_value = (q11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                                          q21 * (xi - x[i]) * (y[j + 1] - yi) +
                                          q12 * (x[i + 1] - xi) * (yi - y[j]) +
                                          q22 * (xi - x[i]) * (yi - y[j])) / \
                                          ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                        z_interp.append(z_interp_value)
                        break
                else:
                    continue
                break
        return z_interp