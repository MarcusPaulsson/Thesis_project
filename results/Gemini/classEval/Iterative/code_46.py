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
        if not x or not y or not x_interp:
            return []

        if len(x) != len(y):
            return []

        y_interp = []
        for x_i in x_interp:
            # Find the interval containing x_i
            i = 0
            while i < len(x) - 1 and x[i + 1] < x_i:
                i += 1

            if x_i < min(x) or x_i > max(x):
                continue
            # Linear interpolation
            x1, x2 = x[i], x[i + 1]
            y1, y2 = y[i], y[i + 1]
            y_i = y1 + (x_i - x1) * (y2 - y1) / (x2 - x1)
            y_interp.append(y_i)

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
        for x_i, y_i in zip(x_interp, y_interp):
            # Find the grid cell containing (x_i, y_i)
            i = 0
            while i < len(x) - 1 and x[i + 1] < x_i:
                i += 1
            j = 0
            while j < len(y) - 1 and y[j + 1] < y_i:
                j += 1

            if x_i < min(x) or x_i > max(x) or y_i < min(y) or y_i > max(y):
                continue

            # Bilinear interpolation
            x1, x2 = x[i], x[i + 1]
            y1, y2 = y[j], y[j + 1]
            z11, z12 = z[i][j], z[i][j + 1]
            z21, z22 = z[i + 1][j], z[i + 1][j + 1]

            z_i = (z11 * (x2 - x_i) * (y2 - y_i) +
                   z21 * (x_i - x1) * (y2 - y_i) +
                   z12 * (x2 - x_i) * (y_i - y1) +
                   z22 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))
            z_interp.append(z_i)

        return z_interp