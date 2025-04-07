import numpy as np
from gensim import matutils
from numpy import dot

class VectorUtil:
    """
    Provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between two vectors.

        Args:
            vector_1 (numpy.ndarray): Vector from which similarities are to be computed, expected shape (dim,).
            vector_2 (numpy.ndarray): Vector from which similarities are to be computed, expected shape (dim,).

        Returns:
            float: Cosine similarity between `vector_1` and `vector_2`.  Returns 0 if either vector is all zeros.

        Raises:
            TypeError: if inputs are not numpy arrays.
            ValueError: if inputs are not 1D arrays or have different dimensions.

        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
        if not isinstance(vector_1, np.ndarray) or not isinstance(vector_2, np.ndarray):
            raise TypeError("Inputs must be numpy arrays.")

        if vector_1.ndim != 1 or vector_2.ndim != 1:
            raise ValueError("Inputs must be 1D arrays.")

        if vector_1.shape != vector_2.shape:
            raise ValueError("Vectors must have the same dimension.")

        vector_1 = matutils.unitvec(vector_1)
        vector_2 = matutils.unitvec(vector_2)

        return np.dot(vector_1, vector_2)



    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.

        Args:
            vector_1 (numpy.ndarray): Vector from which similarities are to be computed, expected shape (dim,).
            vectors_all (list of numpy.ndarray or numpy.ndarray): For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim) or (dim,).

        Returns:
            numpy.ndarray: Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,). Returns array of 0s if vector_1 is all zeros

        Raises:
            TypeError: if vector_1 is not a numpy array or vectors_all is not a list/numpy array.
            ValueError: if vector_1 is not 1D or vectors in vectors_all do not have the same dimension as vector_1.

        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        array([0.97463185, 0.95941195])
        """
        if not isinstance(vector_1, np.ndarray):
            raise TypeError("vector_1 must be a numpy array.")

        if not isinstance(vectors_all, (list, np.ndarray)):
            raise TypeError("vectors_all must be a list or numpy array.")

        if vector_1.ndim != 1:
            raise ValueError("vector_1 must be a 1D array.")

        if isinstance(vectors_all, list):
            for v in vectors_all:
                if not isinstance(v, np.ndarray):
                    raise TypeError("All elements in vectors_all must be numpy arrays.")
                if v.shape != vector_1.shape:
                    raise ValueError("Vectors in vectors_all must have the same dimension as vector_1.")
            vectors_all = np.array(vectors_all)
        elif isinstance(vectors_all, np.ndarray):
            if vectors_all.ndim == 1:
                if vectors_all.shape != vector_1.shape:
                    raise ValueError("Vectors in vectors_all must have the same dimension as vector_1.")
                vectors_all = vectors_all[np.newaxis, :] # Reshape to 2D array
            elif vectors_all.ndim == 2:
                if vectors_all.shape[1] != vector_1.shape[0]:
                    raise ValueError("Vectors in vectors_all must have the same dimension as vector_1.")
            else:
                raise ValueError("vectors_all must be a 1D or 2D array.")
        else:
            raise TypeError("vectors_all must be a list or numpy array.")


        vector_1 = matutils.unitvec(vector_1)
        vectors_all = matutils.unitvec(vectors_all)


        if vectors_all.ndim == 1:
            return np.array([np.dot(vector_1, vectors_all)])  # Ensure it returns a NumPy array
        else:
            return np.dot(vectors_all, vector_1)


    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute average cosine similarity between two sets of vectors.

        Args:
            vector_list_1 (list of numpy.ndarray): List of numpy vectors.
            vector_list_2 (list of numpy.ndarray): List of numpy vectors.

        Returns:
            float: Average cosine similarity between vector_list_1 and vector_list_2. Returns 0 if either list is empty.

        Raises:
            TypeError: if inputs are not lists or elements are not numpy arrays.
            ValueError: if vectors within a list have inconsistent dimensions.

        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
        if not isinstance(vector_list_1, list) or not isinstance(vector_list_2, list):
            raise TypeError("Inputs must be lists.")

        if not vector_list_1 or not vector_list_2:
            return 0.0

        for v in vector_list_1 + vector_list_2:
            if not isinstance(v, np.ndarray):
                raise TypeError("All elements in the lists must be numpy arrays.")
            if v.ndim != 1:
                raise ValueError("All vectors must be 1D arrays.")

        if len(vector_list_1) > 0:
            dim1 = vector_list_1[0].shape[0]
            for v in vector_list_1:
                if v.shape[0] != dim1:
                    raise ValueError("Vectors in vector_list_1 must have the same dimension.")

        if len(vector_list_2) > 0:
            dim2 = vector_list_2[0].shape[0]
            for v in vector_list_2:
                if v.shape[0] != dim2:
                    raise ValueError("Vectors in vector_list_2 must have the same dimension.")


        vector_list_1 = [matutils.unitvec(v) for v in vector_list_1]
        vector_list_2 = [matutils.unitvec(v) for v in vector_list_2]

        sum_sim = 0.0
        for v1 in vector_list_1:
            for v2 in vector_list_2:
                sum_sim += np.dot(v1, v2)

        return sum_sim / (len(vector_list_1) * len(vector_list_2))


    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log((total_num + 1) / (count + 1)) for each count in number_dict.

        Args:
            total_num (int): Total number of documents.
            number_dict (dict): Dictionary where keys are terms and values are document frequencies.

        Returns:
            dict: Dictionary with the same keys as number_dict and IDF weights as values.

        Raises:
            TypeError: if total_num is not an integer or number_dict is not a dictionary.
            ValueError: if total_num is negative or values in number_dict are not numeric.


        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
        if not isinstance(total_num, int):
            raise TypeError("total_num must be an integer.")

        if not isinstance(number_dict, dict):
            raise TypeError("number_dict must be a dictionary.")

        if total_num < 0:
            raise ValueError("total_num cannot be negative.")

        for key, count in number_dict.items():
            if not isinstance(count, (int, float)):
                raise ValueError("Values in number_dict must be numeric.")

        idf_weight = {}
        for key, count in number_dict.items():
            idf_weight[key] = np.log((total_num + 1) / (count + 1))
        return idf_weight