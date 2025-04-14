import numpy as np
from gensim import matutils
from numpy import dot, array
import logging
from numpy.linalg import norm
import math

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
        if not isinstance(vector_1, np.ndarray) or not isinstance(vector_2, np.ndarray):
            logging.error("Inputs must be numpy arrays.")
            return 0.0

        if vector_1.shape != vector_2.shape:
            logging.warning("Vectors have different dimensions.")
            return 0.0

        norm_1 = norm(vector_1)
        norm_2 = norm(vector_2)

        if norm_1 == 0 or norm_2 == 0:
            return 0.0

        return dot(vector_1, vector_2) / (norm_1 * norm_2)


    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
        if not isinstance(vector_1, np.ndarray) or not isinstance(vectors_all, list):
            logging.error("Inputs must be a numpy array and a list of numpy arrays.")
            return np.array([])

        if not all(isinstance(v, np.ndarray) for v in vectors_all):
            logging.error("vectors_all must be a list of numpy arrays.")
            return np.array([])

        similarities = []
        for vector_2 in vectors_all:
            similarities.append(VectorUtil.similarity(vector_1, vector_2))
        return np.array(similarities)


    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
        if not isinstance(vector_list_1, list) or not isinstance(vector_list_2, list):
            logging.error("Inputs must be lists of numpy arrays.")
            return 0.0

        if not all(isinstance(v, np.ndarray) for v in vector_list_1) or not all(isinstance(v, np.ndarray) for v in vector_list_2):
            logging.error("Inputs must be lists of numpy arrays.")
            return 0.0

        if not vector_list_1 or not vector_list_2:
            return 1.0

        similarity_sum = 0.0
        for vector1 in vector_list_1:
            for vector2 in vector_list_2:
                similarity_sum += VectorUtil.similarity(vector1, vector2)

        return similarity_sum / (len(vector_list_1) * len(vector_list_2))


    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
        if not isinstance(total_num, int):
            logging.error("total_num must be an integer.")
            return {}

        if not isinstance(number_dict, dict):
            logging.error("number_dict must be a dictionary.")
            return {}

        idf_weight_dict = {}
        for key, count in number_dict.items():
            idf_weight_dict[key] = math.log((total_num + 1) / (count + 1))
        return idf_weight_dict