import numpy as np

class Interpolation:
    """
    This is a class that implements the Linear interpolation operation of one-dimensional and two-dimensional data
    """

    def __init__(self):
        pass

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data.  Uses numpy for efficiency and handles edge cases.

        :param x: The x-coordinate of the data points, list or numpy array.  Must be sorted.
        :param y: The y-coordinate of the data points, list or numpy array.
        :param x_interp: The x-coordinate of the interpolation points, list or numpy array.
        :return: The y-coordinate of the interpolation points, numpy array. Returns NaN if x_interp is outside the range of x.

        >>> Interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        array([1.5, 2.5])
        >>> Interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [0.5, 3.5])
        array([nan, nan])
        """
        x = np.asarray(x)
        y = np.asarray(y)
        x_interp = np.asarray(x_interp)

        if x.ndim != 1 or y.ndim != 1 or x_interp.ndim != 1:
            raise ValueError("x, y, and x_interp must be one-dimensional arrays.")

        if x.shape != y.shape:
            raise ValueError("x and y must have the same shape.")

        y_interp = np.interp(x_interp, x, y, left=np.nan, right=np.nan)  # Use numpy's interp for efficiency and edge handling
        return y_interp

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Bilinear interpolation of two-dimensional data. Uses numpy for efficiency and readability.
        Handles out-of-bounds cases by returning NaN.

        :param x: The x-coordinates of the data points, list or numpy array (1D). Must be sorted.
        :param y: The y-coordinates of the data points, list or numpy array (1D). Must be sorted.
        :param z: The z-coordinates of the data points, list or numpy array (2D). z[i][j] corresponds to (x[i], y[j]).
        :param x_interp: The x-coordinates of the interpolation points, list or numpy array (1D).
        :param y_interp: The y-coordinates of the interpolation points, list or numpy array (1D).
        :return: The z-coordinates of the interpolation points, numpy array (1D). Returns NaN if interpolation point is out of bounds.

        >>> Interpolation.interpolate_2d([1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1.5, 2.5], [1.5, 2.5])
        array([3., 7.])
        >>> Interpolation.interpolate_2d([1, 2], [1, 2], [[1, 2], [3, 4]], [0, 3], [0, 3])
        array([nan, nan])
        """
        x = np.asarray(x)
        y = np.asarray(y)
        z = np.asarray(z)
        x_interp = np.asarray(x_interp)
        y_interp = np.asarray(y_interp)

        if x.ndim != 1 or y.ndim != 1 or x_interp.ndim != 1 or y_interp.ndim != 1:
            raise ValueError("x, y, x_interp, and y_interp must be one-dimensional arrays.")

        if z.ndim != 2:
            raise ValueError("z must be a two-dimensional array.")

        if z.shape != (len(x), len(y)):
            raise ValueError("z must have shape (len(x), len(y)).")

        z_interp = np.zeros_like(x_interp, dtype=np.float64)
        z_interp[:] = np.nan  # Initialize with NaN

        for idx, (xi, yi) in enumerate(zip(x_interp, y_interp)):
            # Find the grid cell containing the point (xi, yi)
            i = np.searchsorted(x, xi, side="right") - 1
            j = np.searchsorted(y, yi, side="right") - 1

            if 0 <= i < len(x) - 1 and 0 <= j < len(y) - 1:
                # Bilinear interpolation
                x1, x2 = x[i], x[i + 1]
                y1, y2 = y[j], y[j + 1]

                Q11 = z[i, j]
                Q12 = z[i, j + 1]
                Q21 = z[i + 1, j]
                Q22 = z[i + 1, j + 1]

                z_interp[idx] = (
                    (Q11 * (x2 - xi) * (y2 - yi))
                    + (Q21 * (xi - x1) * (y2 - yi))
                    + (Q12 * (x2 - xi) * (yi - y1))
                    + (Q22 * (xi - x1) * (yi - y1))
                ) / ((x2 - x1) * (y2 - y1))

        return z_interp