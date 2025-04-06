import numpy as np

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, expected shape (dim,).
        :param vector_2: numpy.ndarray, expected shape (dim,).
        :return: float, cosine similarity between `vector_1` and `vector_2`.
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
        norm_1 = np.linalg.norm(vector_1)
        norm_2 = np.linalg.norm(vector_2)
        if norm_1 == 0 or norm_2 == 0:
            return 0.0
        return np.dot(vector_1, vector_2) / (norm_1 * norm_2)

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, expected shape (num_vectors, dim).
        :return: numpy.ndarray, cosine similarities between `vector_1` and each row in `vectors_all`.
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        array([0.97463185, 0.95941195])
        """
        return np.array([VectorUtil.similarity(vector_1, vector) for vector in vectors_all])

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute average cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy.ndarray.
        :param vector_list_2: list of numpy.ndarray.
        :return: float, average cosine similarity between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
        similarities = [VectorUtil.similarity(v1, v2) for v1 in vector_list_1 for v2 in vector_list_2]
        return np.mean(similarities) if similarities else 0.0

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log((total_num + 1) / (count + 1)) for each count in number_dict.
        :param total_num: int, total number of documents.
        :param number_dict: dict, counts of documents containing each term.
        :return: dict, IDF weights for each term.
        >>> num_dict = {'key1': 1, 'key2': 2}
        >>> VectorUtil.compute_idf_weight_dict(3, num_dict)
        {'key1': 1.0986122886681098, 'key2': 0.8109302162163288}
        """
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}