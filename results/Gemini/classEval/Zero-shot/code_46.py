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
                y_interp.append(y[0] + (x_i - x[0]) * (y[1] - y[0]) / (x[1] - x[0]) if len(x) > 1 else y[0])
            elif x_i >= x[-1]:
                y_interp.append(y[-2] + (x_i - x[-2]) * (y[-1] - y[-2]) / (x[-1] - x[-2]) if len(x) > 1 else y[-1])
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        y_i = y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
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
            # Find the four nearest data points
            x1, x2 = None, None
            y1, y2 = None, None

            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x1, x2 = i, i + 1
                    break
            else:
                if x_i < x[0]:
                    x1, x2 = 0, 1
                else:
                    x1, x2 = len(x) - 2, len(x) - 1

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y1, y2 = j, j + 1
                    break
            else:
                if y_i < y[0]:
                    y1, y2 = 0, 1
                else:
                    y1, y2 = len(y) - 2, len(y) - 1

            if x1 is None or x2 is None or y1 is None or y2 is None:
                z_interp.append(0.0)  # Or some other default value
                continue

            # Bilinear interpolation
            Q11 = z[x1][y1]
            Q12 = z[x1][y2]
            Q21 = z[x2][y1]
            Q22 = z[x2][y2]

            x1_val = x[x1]
            x2_val = x[x2]
            y1_val = y[y1]
            y2_val = y[y2]

            if x1_val == x2_val or y1_val == y2_val:
                if x1_val == x2_val and y1_val == y2_val:
                    z_interp_val = Q11
                elif x1_val == x2_val:
                    z_interp_val = (Q11 * (y2_val - y_i) + Q12 * (y_i - y1_val)) / (y2_val - y1_val)
                else:
                    z_interp_val = (Q11 * (x2_val - x_i) + Q21 * (x_i - x1_val)) / (x2_val - x1_val)
            else:
                z_interp_val = (Q11 * (x2_val - x_i) * (y2_val - y_i) +
                                Q21 * (x_i - x1_val) * (y2_val - y_i) +
                                Q12 * (x2_val - x_i) * (y_i - y1_val) +
                                Q22 * (x_i - x1_val) * (y_i - y1_val)) / \
                               ((x2_val - x1_val) * (y2_val - y1_val))

            z_interp.append(z_interp_val)

        return z_interp