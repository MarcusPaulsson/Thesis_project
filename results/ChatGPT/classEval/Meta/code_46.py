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
            if xi < x[0] or xi > x[-1]:
                raise ValueError("Interpolation point out of bounds")
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    yi = y[i] + slope * (xi - x[i])
                    y_interp.append(yi)
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
                raise ValueError("Interpolation point out of bounds")
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        # Bilinear interpolation
                        z_11 = z[j][i]
                        z_12 = z[j + 1][i]
                        z_21 = z[j][i + 1]
                        z_22 = z[j + 1][i + 1]
                        
                        z_interp_value = (z_11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                                          z_21 * (xi - x[i]) * (y[j + 1] - yi) +
                                          z_12 * (x[i + 1] - xi) * (yi - y[j]) +
                                          z_22 * (xi - x[i]) * (yi - y[j])) / \
                                          ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                        z_interp.append(z_interp_value)
                        break
        return z_interp