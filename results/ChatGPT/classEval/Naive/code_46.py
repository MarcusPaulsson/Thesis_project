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
        result = []
        for xi in x_interp:
            if xi < x[0] or xi > x[-1]:
                raise ValueError("Interpolation point out of bounds.")
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    interpolated_value = y[i] + slope * (xi - x[i])
                    result.append(interpolated_value)
                    break
        return result

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list of lists.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]
        """
        result = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                raise ValueError("Interpolation point out of bounds.")
            x1, x2 = None, None
            y1, y2 = None, None
            
            # Find the surrounding points
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    x1, x2 = x[i], x[i + 1]
                    break
            for j in range(len(y) - 1):
                if y[j] <= yi <= y[j + 1]:
                    y1, y2 = y[j], y[j + 1]
                    break
            
            # Calculate the four corners of the grid
            q11 = z[y.index(y1)][x.index(x1)]
            q21 = z[y.index(y1)][x.index(x2)]
            q12 = z[y.index(y2)][x.index(x1)]
            q22 = z[y.index(y2)][x.index(x2)]

            # Perform bilinear interpolation
            interpolated_value = (q11 * (x2 - xi) * (y2 - yi) +
                                  q21 * (xi - x1) * (y2 - yi) +
                                  q12 * (x2 - xi) * (yi - y1) +
                                  q22 * (xi - x1) * (yi - y1)) / ((x2 - x1) * (y2 - y1))
            result.append(interpolated_value)
        return result