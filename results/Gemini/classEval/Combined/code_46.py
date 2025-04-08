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
        :param x: The x-coordinate of the data points, list. Must be sorted.
        :param y: The y-coordinate of the data points, list.
        :param x_interp: The x-coordinate of the interpolation points, list.
        :return: The y-coordinate of the interpolation points, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        [1.5, 2.5]
        """
        if not x or not y or not x_interp:
            return []

        if len(x) != len(y):
            raise ValueError("x and y must have the same length")

        if len(x) < 2:
            return [y[0]] * len(x_interp)  # Or raise an exception

        y_interp = []
        for x_i in x_interp:
            if x_i < x[0]:
                y_interp.append(y[0] + (x_i - x[0]) * (y[1] - y[0]) / (x[1] - x[0]))
            elif x_i > x[-1]:
                y_interp.append(y[-1] + (x_i - x[-1]) * (y[-1] - y[-2]) / (x[-1] - x[-2]))
            else:
                for i in range(len(x) - 1):
                    if x[i] <= x_i <= x[i + 1]:
                        y_i = y[i] + (x_i - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                        y_interp.append(y_i)
                        break
                else:
                    # Should not happen if x is properly sorted and x_i is within the range
                    return []  # Or raise an exception
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Bilinear interpolation of two-dimensional data on a rectangular grid.
        :param x: The x-coordinates of the grid points, list. Must be sorted.
        :param y: The y-coordinates of the grid points, list. Must be sorted.
        :param z: The z-values at the grid points, 2D list. z[i][j] corresponds to (x[i], y[j]).
        :param x_interp: The x-coordinates of the interpolation points, list.
        :param y_interp: The y-coordinates of the interpolation points, list.
        :return: The z-coordinates of the interpolation points, list.
        >>> interpolation = Interpolation()
        >>> interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        [3.0, 7.0]
        """

        if not x or not y or not z or not x_interp or not y_interp:
            return []

        if len(z) != len(x) or any(len(row) != len(y) for row in z):
            raise ValueError("Dimensions of x, y, and z are inconsistent.")

        z_interp = []
        for x_i, y_i in zip(x_interp, y_interp):
            # Find the grid cell containing (x_i, y_i)
            x_index = -1
            y_index = -1

            for i in range(len(x) - 1):
                if x[i] <= x_i <= x[i + 1]:
                    x_index = i
                    break

            for j in range(len(y) - 1):
                if y[j] <= y_i <= y[j + 1]:
                    y_index = j
                    break

            if x_index == -1 or y_index == -1:
                # Interpolation point is outside the grid
                # Handle edge cases: extrapolate, return a default value, or skip the point
                # For now, we skip the point
                continue

            # Bilinear interpolation within the grid cell
            x1, x2 = x[x_index], x[x_index + 1]
            y1, y2 = y[y_index], y[y_index + 1]

            z11 = z[x_index][y_index]
            z12 = z[x_index][y_index + 1]
            z21 = z[x_index + 1][y_index]
            z22 = z[x_index + 1][y_index + 1]

            z_i = (z11 * (x2 - x_i) * (y2 - y_i) +
                   z21 * (x_i - x1) * (y2 - y_i) +
                   z12 * (x2 - x_i) * (y_i - y1) +
                   z22 * (x_i - x1) * (y_i - y1)) / ((x2 - x1) * (y2 - y1))

            z_interp.append(z_i)

        return z_interp