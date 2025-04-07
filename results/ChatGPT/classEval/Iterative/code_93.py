import numpy as np

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
        :return: float, Contains cosine distance between `vector_1` and `vector_2`
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
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """
        return np.array([VectorUtil.similarity(vector_1, vector) for vector in vectors_all])

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: float, Average similarities between vector_list_1 and vector_list_2.
        """
        if not vector_list_1 or not vector_list_2:
            return 0.0
        similarities = [VectorUtil.similarity(v1, v2) for v1 in vector_list_1 for v2 in vector_list_2]
        return np.mean(similarities) if similarities else 0.0

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        """
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}