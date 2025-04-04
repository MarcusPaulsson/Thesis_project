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
        for xi in x_interp:
            if xi < x[0] or xi > x[-1]:
                raise ValueError(f"x_interp value {xi} is out of bounds.")
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
        Linear interpolation of two-dimensional data
        :param x: The x-coordinate of the data point, list.
        :param y: The y-coordinate of the data point, list.
        :param z: The z-coordinate of the data point, list of lists.
        :param x_interp: The x-coordinate of the interpolation point, list.
        :param y_interp: The y-coordinate of the interpolation point, list.
        :return: The z-coordinate of the interpolation point, list.
        """
        z_interp = []
        for xi, yi in zip(x_interp, y_interp):
            if xi < x[0] or xi > x[-1] or yi < y[0] or yi > y[-1]:
                raise ValueError(f"Interpolation point ({xi}, {yi}) is out of bounds.")
            
            # Find the bounding box for the interpolation point
            for i in range(len(x) - 1):
                for j in range(len(y) - 1):
                    if x[i] <= xi <= x[i + 1] and y[j] <= yi <= y[j + 1]:
                        # Perform bilinear interpolation
                        z11 = z[j][i]     # z value at (x[i], y[j])
                        z12 = z[j][i + 1] # z value at (x[i + 1], y[j])
                        z21 = z[j + 1][i] # z value at (x[i], y[j + 1])
                        z22 = z[j + 1][i + 1] # z value at (x[i + 1], y[j + 1])
                        
                        # Calculate the interpolation
                        z_value = (z11 * (x[i + 1] - xi) * (y[j + 1] - yi) +
                                   z12 * (xi - x[i]) * (y[j + 1] - yi) +
                                   z21 * (x[i + 1] - xi) * (yi - y[j]) +
                                   z22 * (xi - x[i]) * (yi - y[j])) / \
                                   ((x[i + 1] - x[i]) * (y[j + 1] - y[j]))
                        z_interp.append(z_value)
                        break
                else:
                    continue
                break
        return z_interp