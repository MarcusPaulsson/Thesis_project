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
                y_interp.append(y[0] + (y[1] - y[0]) * (xi - x[0]) / (x[1] - x[0]))
            elif xi > x[-1]:
                y_interp.append(y[-1] + (y[-1] - y[-2]) * (xi - x[-1]) / (x[-1] - x[-2]))
            else:
                for i in range(len(x) - 1):
                    if x[i] <= xi <= x[i + 1]:
                        y_interp.append(y[i] + (y[i + 1] - y[i]) * (xi - x[i]) / (x[i + 1] - x[i]))
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
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                z_interp.append(None)  # Out of bounds
                continue
            
            # Find the surrounding points
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    for j in range(len(y) - 1):
                        if y[j] <= yi <= y[j + 1]:
                            # Perform bilinear interpolation
                            z11 = z[j][i]
                            z12 = z[j + 1][i]
                            z21 = z[j][i + 1]
                            z22 = z[j + 1][i + 1]

                            z_interp.append(
                                (z11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                                 z21 * (xi - x[i]) * (y[j + 1] - yi) +
                                 z12 * (x[i + 1] - xi) * (yi - y[j]) +
                                 z22 * (xi - x[i]) * (yi - y[j])) /
                                ((x[i + 1] - x[i]) * (y[j + 1] - y[j])))
                            )
                            break
                    break
        return z_interp