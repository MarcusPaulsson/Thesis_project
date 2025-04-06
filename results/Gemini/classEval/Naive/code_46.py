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
        y_interp = []
        for x_i in x_interp:
            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    y_i = y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    y_interp.append(y_i)
                    break
            else:
                y_interp.append(None)  # Handle cases where x_i is outside the range of x
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list (2D).
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        """
        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= x_i <= x[i + 1] and y[j] <= y_i <= y[j + 1]:
                        # Bilinear interpolation
                        x1, x2 = x[i], x[i + 1]
                        y1, y2 = y[j], y[j + 1]

                        z11 = z[i][j]
                        z12 = z[i][j + 1]
                        z21 = z[i + 1][j]
                        z22 = z[i + 1][j + 1]

                        z_i = (z11 * (x2 - x_i) * (y2 - y_i) +
                               z21 * (x_i - x1) * (y2 - y_i) +
                               z12 * (x2 - x_i) * (y_i - y1) +
                               z22 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))

                        z_interp.append(z_i)
                        break
                else:
                    continue # Continue to the next y iteration if the inner loop breaks
                break # Break out of x iteration if inner loop breaks, since we found our square
            else:
                z_interp.append(None) # Handle cases where x_i or y_i is outside the range
        return z_interp