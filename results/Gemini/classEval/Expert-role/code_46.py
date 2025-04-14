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
            # Find the bounding box
            x_idx = -1
            y_idx = -1
            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x_idx = i
                    break
            if x_idx == -1:
                x_idx = len(x) - 2

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y_idx = j
                    break
            if y_idx == -1:
                y_idx = len(y) - 2

            # Interpolate
            x1, x2 = x[x_idx], x[x_idx + 1]
            y1, y2 = y[y_idx], y[y_idx + 1]

            z11 = z[x_idx][y_idx]
            z12 = z[x_idx][y_idx + 1]
            z21 = z[x_idx + 1][y_idx]
            z22 = z[x_idx + 1][y_idx + 1]

            z_interp_i = (z11 * (x2 - x_i) * (y2 - y_i) +
                          z21 * (x_i - x1) * (y2 - y_i) +
                          z12 * (x2 - x_i) * (y_i - y1) +
                          z22 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))

            z_interp.append(z_interp_i)

        return z_interp