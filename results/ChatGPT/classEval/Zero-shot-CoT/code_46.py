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
        if not x_interp:
            return []
        y_interp = []
        for xi in x_interp:
            if xi < x[0]:
                y_interp.append(y[0] + (y[1] - y[0]) * ((xi - x[0]) / (x[1] - x[0])))
            elif xi > x[-1]:
                y_interp.append(y[-1] + (y[-1] - y[-2]) * ((xi - x[-1]) / (x[-1] - x[-2])))
            else:
                for i in range(len(x) - 1):
                    if x[i] <= xi <= x[i + 1]:
                        slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_interp.append(y[i] + slope * (xi - x[i]))
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
        if not x_interp or not y_interp:
            return []
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            x1_idx = next(i for i, val in enumerate(x) if val >= xi) - 1
            x2_idx = x1_idx + 1
            y1_idx = next(i for i, val in enumerate(y) if val >= yi) - 1
            y2_idx = y1_idx + 1

            x1, x2 = x[x1_idx], x[x2_idx]
            y1, y2 = y[y1_idx], y[y2_idx]
            z11, z12 = z[y1_idx][x1_idx], z[y1_idx][x2_idx]
            z21, z22 = z[y2_idx][x1_idx], z[y2_idx][x2_idx]

            z_interp_value = (
                (z11 * (x2 - xi) * (y2 - yi) +
                 z21 * (xi - x1) * (y2 - yi) +
                 z12 * (x2 - xi) * (yi - y1) +
                 z22 * (xi - x1) * (yi - y1)) / 
                ((x2 - x1) * (y2 - y1))
            )
            z_interp.append(z_interp_value)
        return z_interp