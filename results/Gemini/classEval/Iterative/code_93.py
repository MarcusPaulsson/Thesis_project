import numpy as np
from numpy import dot
from numpy.linalg import norm


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
        """
        norm_v1 = norm(vector_1)
        norm_v2 = norm(vector_2)

        if norm_v1 == 0 or norm_v2 == 0:
            return 0.0

        return dot(vector_1, vector_2) / (norm_v1 * norm_v2)

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """
        similarities = []
        norm_v1 = norm(vector_1)

        if norm_v1 == 0:
            return [0.0] * len(vectors_all)

        for vector in vectors_all:
            norm_v2 = norm(vector)
            if norm_v2 == 0:
                similarities.append(0.0)
            else:
                similarities.append(dot(vector_1, vector) / (norm_v1 * norm_v2))
        return similarities

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        """
        if not vector_list_1 or not vector_list_2:
            return 0.0

        sum_sim = 0.0
        count = 0
        for v1 in vector_list_1:
            norm_v1 = norm(v1)
            if norm_v1 == 0:
                continue
            for v2 in vector_list_2:
                norm_v2 = norm(v2)
                if norm_v2 == 0:
                    continue
                sim = dot(v1, v2) / (norm_v1 * norm_v2)
                sum_sim += sim
                count += 1

        return sum_sim / count if count > 0 else 0.0

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        """
        idf_weight_dict = {}
        for key, count in number_dict.items():
            idf_weight_dict[key] = np.log((total_num + 1) / (count + 1))
        return idf_weight_dict