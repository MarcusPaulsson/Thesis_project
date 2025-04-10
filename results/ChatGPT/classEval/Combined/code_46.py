class Interpolation:
    """
    This class implements linear interpolation for one-dimensional and two-dimensional data.
    """

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Perform linear interpolation of one-dimensional data.
        
        :param x: List of x-coordinates of the data points.
        :param y: List of y-coordinates of the data points.
        :param x_interp: List of x-coordinates for interpolation.
        :return: List of interpolated y-coordinates.
        """
        if not x or not y or not x_interp or len(x) != len(y):
            return []

        y_interp = []
        n = len(x)

        for xi in x_interp:
            if xi < x[0]:
                y_interp.append(y[0])
            elif xi > x[-1]:
                y_interp.append(y[-1])
            else:
                for i in range(n - 1):
                    if x[i] <= xi <= x[i + 1]:
                        slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        yi = y[i] + slope * (xi - x[i])
                        y_interp.append(yi)
                        break

        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Perform linear interpolation of two-dimensional data.
        
        :param x: List of x-coordinates of the data points.
        :param y: List of y-coordinates of the data points.
        :param z: 2D list of z-coordinates for the data points.
        :param x_interp: List of x-coordinates for interpolation.
        :param y_interp: List of y-coordinates for interpolation.
        :return: List of interpolated z-coordinates.
        """
        if not x or not y or not z or not x_interp or not y_interp or len(x) != len(z[0]) or len(y) != len(z):
            return []

        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                z_interp.append(None)
                continue
            
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    for j in range(len(y) - 1):
                        if y[j] <= yi <= y[j + 1]:
                            z_interp_value = Interpolation._bilinear_interpolate(xi, yi, x[i], x[i + 1], y[j], y[j + 1],
                                                                                  z[j][i], z[j][i + 1], z[j + 1][i], z[j + 1][i + 1])
                            z_interp.append(z_interp_value)
                            break
                    break

        return z_interp

    @staticmethod
    def _bilinear_interpolate(xi, yi, x1, x2, y1, y2, z11, z12, z21, z22):
        """
        Helper method to perform bilinear interpolation.

        :param xi: x-coordinate for interpolation.
        :param yi: y-coordinate for interpolation.
        :param x1: Lower x-bound.
        :param x2: Upper x-bound.
        :param y1: Lower y-bound.
        :param y2: Upper y-bound.
        :param z11: Value at (x1, y1).
        :param z12: Value at (x2, y1).
        :param z21: Value at (x1, y2).
        :param z22: Value at (x2, y2).
        :return: Interpolated z-coordinate.
        """
        return (z11 * (x2 - xi) * (y2 - yi) +
                z12 * (xi - x1) * (y2 - yi) +
                z21 * (x2 - xi) * (yi - y1) +
                z22 * (xi - x1) * (yi - y1)) / ((x2 - x1) * (y2 - y1))