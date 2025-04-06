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
        y_interp = []
        for x_i in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    y_i = y[i] + (y[i + 1] - y[i]) * (x_i - x[i]) / (x[i + 1] - x[i])
                    y_interp.append(y_i)
                    break
            else:
                y_interp.append(None)  # Handle cases where x_interp is outside the range of x
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
            # Find the four nearest data points
            x1, x2 = None, None
            y1, y2 = None, None
            z11, z12, z21, z22 = None, None, None, None

            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x1 = x[i]
                    x2 = x[i + 1]
                    break

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y1 = y[j]
                    y2 = y[j + 1]
                    break
            
            if x1 is None or x2 is None or y1 is None or y2 is None:
                z_interp.append(None)  # Handle cases where interpolation point is outside data range
                continue

            x_index1 = x.index(x1)
            x_index2 = x.index(x2)
            y_index1 = y.index(y1)
            y_index2 = y.index(y2)
            
            z11 = z[y_index1][x_index1]
            z12 = z[y_index1][x_index2]
            z21 = z[y_index2][x_index1]
            z22 = z[y_index2][x_index2]

            # Bilinear interpolation
            z_i = (z11 * (x2 - x_i) * (y2 - y_i) +
                   z21 * (x_i - x1) * (y2 - y_i) +
                   z12 * (x2 - x_i) * (y_i - y1) +
                   z22 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))
            z_interp.append(z_i)

        return z_interp