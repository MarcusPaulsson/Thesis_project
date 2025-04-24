class Interpolation:
    """
    A class that implements linear interpolation for one-dimensional and two-dimensional data.
    """

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Performs linear interpolation for one-dimensional data.

        :param x: List of x-coordinates of the data points.
        :param y: List of y-coordinates of the data points.
        :param x_interp: List of x-coordinates for interpolation.
        :return: List of interpolated y-coordinates.
        """
        if not x or not y or not x_interp or len(x) != len(y):
            return []

        y_interp = []
        for xi in x_interp:
            if xi < x[0]:
                # Extrapolate to the left
                slope = (y[1] - y[0]) / (x[1] - x[0])
                y_interp.append(y[0] + slope * (xi - x[0]))
            elif xi > x[-1]:
                # Extrapolate to the right
                slope = (y[-1] - y[-2]) / (x[-1] - x[-2])
                y_interp.append(y[-1] + slope * (xi - x[-1]))
            else:
                # Interpolate
                for i in range(len(x) - 1):
                    if x[i] <= xi <= x[i + 1]:
                        slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_interp.append(y[i] + slope * (xi - x[i]))
                        break

        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Performs linear interpolation for two-dimensional data.

        :param x: List of x-coordinates of the data points.
        :param y: List of y-coordinates of the data points.
        :param z: 2D list of z-coordinates of the data points.
        :param x_interp: List of x-coordinates for interpolation.
        :param y_interp: List of y-coordinates for interpolation.
        :return: List of interpolated z-coordinates.
        """
        if not x or not y or not z or not x_interp or not y_interp or len(x) != len(z[0]) or len(y) != len(z):
            return []

        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                z_interp.append(None)  # Out of bounds
                continue

            # Find the surrounding points for bilinear interpolation
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    for j in range(len(y) - 1):
                        if y[j] <= yi <= y[j + 1]:
                            z11 = z[j][i]
                            z12 = z[j + 1][i]
                            z21 = z[j][i + 1]
                            z22 = z[j + 1][i + 1]

                            # Calculate weights
                            weight_x = (xi - x[i]) / (x[i + 1] - x[i])
                            weight_y = (yi - y[j]) / (y[j + 1] - y[j])

                            # Perform bilinear interpolation
                            z_interp_value = (z11 * (1 - weight_x) * (1 - weight_y) +
                                              z21 * weight_x * (1 - weight_y) +
                                              z12 * (1 - weight_x) * weight_y +
                                              z22 * weight_x * weight_y)
                            z_interp.append(z_interp_value)
                            break
                    break

        return z_interp