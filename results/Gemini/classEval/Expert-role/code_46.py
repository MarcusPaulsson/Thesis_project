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
                y_interp.append(y[0] + (x_i - x[0]) * (y[1] - y[0]) / (x[1] - x[0]))
            elif x_i >= x[-1]:
                y_interp.append(y[-2] + (x_i - x[-2]) * (y[-1] - y[-2]) / (x[-1] - x[-2]))
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
        for xi, yi in zip(x_interp, y_interp):
            # Find the four closest data points
            x1, x2 = x[0], x[-1]
            y1, y2 = y[0], y[-1]
            
            # Interpolate along x direction
            z1 = Interpolation.interpolate_1d(x, [z[i][0] for i in range(len(z))], [xi])[0]
            z2 = Interpolation.interpolate_1d(x, [z[i][1] for i in range(len(z))], [xi])[0]
            z3 = Interpolation.interpolate_1d(x, [z[i][2] for i in range(len(z))], [xi])[0]

            # Interpolate along y direction            
            z_interp_val = Interpolation.interpolate_1d(y, [z1, z2, z3], [yi])[0]
            z_interp.append(z_interp_val)
        return z_interp