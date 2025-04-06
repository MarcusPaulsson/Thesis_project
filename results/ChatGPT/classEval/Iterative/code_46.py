import numpy as np
from scipy.interpolate import griddata

class Interpolation:
    """
    This class implements linear interpolation for one-dimensional and two-dimensional data.
    """

    @staticmethod
    def interpolate_1d(x, y, x_interp):
        """
        Linear interpolation of one-dimensional data.

        :param x: The x-coordinates of the data points, list or array-like.
        :param y: The y-coordinates of the data points, list or array-like.
        :param x_interp: The x-coordinates of the interpolation points, list or array-like.
        :return: The y-coordinates of the interpolation points, list.
        """
        if len(x) != len(y):
            raise ValueError("x and y must be of the same length.")
        if not np.all(np.diff(x) > 0):
            raise ValueError("x values must be in strictly increasing order.")
        
        return list(np.interp(x_interp, x, y))

    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        """
        Linear interpolation of two-dimensional data.

        :param x: The x-coordinates of the data points, list or array-like.
        :param y: The y-coordinates of the data points, list or array-like.
        :param z: The z-coordinates of the data points, 2D list or array-like.
        :param x_interp: The x-coordinates of the interpolation points, list or array-like.
        :param y_interp: The y-coordinates of the interpolation points, list or array-like.
        :return: The z-coordinates of the interpolation points, list.
        """
        if len(x) != len(y) or len(y) != len(z):
            raise ValueError("x, y, and z must be of compatible dimensions.")
        if not np.all(np.diff(x) > 0) or not np.all(np.diff(y) > 0):
            raise ValueError("x and y values must be in strictly increasing order.")
        
        points = np.array(list(zip(x, y)))
        z_flat = np.array(z).flatten()
        grid_x, grid_y = np.meshgrid(x, y)
        
        return list(griddata(points, z_flat, (x_interp, y_interp), method='linear'))