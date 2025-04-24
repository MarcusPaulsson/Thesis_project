import numpy as np

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
        """
        Compute the cosine similarity between two vectors.
        :param vector_1: numpy.ndarray, expected shape (dim,).
        :param vector_2: numpy.ndarray, expected shape (dim,).
        :return: float, Cosine similarity between `vector_1` and `vector_2`.
        """
        dot_product = np.dot(vector_1, vector_2)
        norm_a = np.linalg.norm(vector_1)
        norm_b = np.linalg.norm(vector_2)
        return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0.0

    @staticmethod
    def cosine_similarities(vector_1: np.ndarray, vectors_all: list) -> np.ndarray:
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine similarity between `vector_1` and each vector in `vectors_all`.
        """
        return np.array([VectorUtil.similarity(vector_1, vector) for vector in vectors_all])

    @staticmethod
    def n_similarity(vector_list_1: list, vector_list_2: list) -> float:
        """
        Compute average cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy.ndarray
        :param vector_list_2: list of numpy.ndarray
        :return: float, Average similarities between vector_list_1 and vector_list_2.
        """
        if not vector_list_1 or not vector_list_2:
            return 0.0
        
        similarities = [VectorUtil.similarity(v1, v2) for v1 in vector_list_1 for v2 in vector_list_2]
        return np.mean(similarities)

    @staticmethod
    def compute_idf_weight_dict(total_num: int, number_dict: dict) -> dict:
        """
        Calculate IDF weights for each count in number_dict.
        :param total_num: int, total number of documents.
        :param number_dict: dict, counts of occurrences for each key.
        :return: dict, IDF weights for each key in number_dict.
        """
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}