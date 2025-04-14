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

        y_interp = []
        for x_i in x_interp:
            if x_i <= x[0]:
                y_interp.append(y[0])
            elif x_i >= x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        y_i = y[i] + (y[i + 1] - y[i]) * (x_i - x[i]) / (x[i + 1] - x[i])
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
        """
        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            if x_i <= x[0] or x_i >= x[-1] or y_i <= y[0] or y_i >= y[-1]:
                continue

            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= x_i <= x[i + 1] and y[j] <= y_i <= y[j + 1]:
                        # Linear interpolation (bilinear interpolation can be implemented here for better accuracy)
                        z_00 = z[i][j]
                        z_01 = z[i][j + 1]
                        z_10 = z[i + 1][j]
                        z_11 = z[i + 1][j + 1]

                        x1 = x[i]
                        x2 = x[i+1]
                        y1 = y[j]
                        y2 = y[j+1]

                        z_interp_val = (
                            z_00 * (x2 - x_i) * (y2 - y_i) +
                            z_10 * (x_i - x1) * (y2 - y_i) +
                            z_01 * (x2 - x_i) * (y_i - y1) +
                            z_11 * (x_i - x1) * (y_i - y1)
                        ) / ((x2 - x1) * (y2 - y1))
                        
                        z_interp.append(z_interp_val)
                        break
                else:
                    continue
                break
        return z_interp