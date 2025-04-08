class Interpolation:
    """
    This is a class that implements the Linear interpolation operation for one-dimensional and two-dimensional data.
    """

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data.
        :param x: The x-coordinates of the data points, list.
        :param y: The y-coordinates of the data points, list.
        :param x_interp: The x-coordinates of the interpolation points, list.
        :return: The y-coordinates of the interpolation points, list.
        """
        if not x or not y or not x_interp or len(x) != len(y):
            return []

        y_interp = []
        for xi in x_interp:
            if xi < x[0] or xi > x[-1]:  # Out of bounds
                y_interp.append(None)
                continue

            # Find the interval [x[i], x[i+1]]
            for i in range(len(x) - 1):
                if x[i] <= xi <= x[i + 1]:
                    # Linear interpolation formula
                    slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                    y_value = y[i] + slope * (xi - x[i])
                    y_interp.append(y_value)
                    break

        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data.
        :param x: The x-coordinates of the data points, list.
        :param y: The y-coordinates of the data points, list.
        :param z: The z-coordinates of the data points (2D grid), list of lists.
        :param x_interp: The x-coordinates of the interpolation points, list.
        :param y_interp: The y-coordinates of the interpolation points, list.
        :return: The z-coordinates of the interpolation points, list.
        """
        if not x or not y or not z or not x_interp or not y_interp or len(z) != len(y) or any(len(row) != len(x) for row in z):
            return []

        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:  # Out of bounds
                z_interp.append(None)
                continue

            # Find the surrounding points
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        # Bilinear interpolation
                        z11 = z[j][i]
                        z12 = z[j + 1][i]
                        z21 = z[j][i + 1]
                        z22 = z[j + 1][i + 1]

                        # Calculate weights
                        weight_x = (xi - x[i]) / (x[i + 1] - x[i])
                        weight_y = (yi - y[j]) / (y[j + 1] - y[j])

                        z_value = (z11 * (1 - weight_x) * (1 - weight_y) +
                                   z21 * weight_x * (1 - weight_y) +
                                   z12 * (1 - weight_x) * weight_y +
                                   z22 * weight_x * weight_y)
                        z_interp.append(z_value)
                        break

        return z_interp