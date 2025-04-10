import numpy as np

class VectorUtil:
    """
    Class providing various vector operations including cosine similarity, 
    average similarity across vector sets, and IDF weight calculations.
    """
    
    @staticmethod
    def similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
        """
        Compute the cosine similarity between two vectors.
        
        :param vector_1: First vector, expected shape (dim,).
        :param vector_2: Second vector, expected shape (dim,).
        :return: Cosine similarity between `vector_1` and `vector_2`.
        """
        dot_product = np.dot(vector_1, vector_2)
        norm_a = np.linalg.norm(vector_1)
        norm_b = np.linalg.norm(vector_2)
        return dot_product / (norm_a * norm_b) if norm_a and norm_b else 0.0

    @staticmethod
    def cosine_similarities(vector_1: np.ndarray, vectors_all: list) -> np.ndarray:
        """
        Compute cosine similarities between one vector and a set of other vectors.
        
        :param vector_1: Vector for comparison, expected shape (dim,).
        :param vectors_all: List of vectors, each expected shape (dim,).
        :return: Array of cosine similarities between `vector_1` and each vector in `vectors_all`.
        """
        return np.array([VectorUtil.similarity(vector_1, vector) for vector in vectors_all])

    @staticmethod
    def n_similarity(vector_list_1: list, vector_list_2: list) -> float:
        """
        Compute average cosine similarity between two sets of vectors.
        
        :param vector_list_1: List of vectors.
        :param vector_list_2: List of vectors.
        :return: Average cosine similarity.
        """
        if not vector_list_1 or not vector_list_2:
            return 0.0
        similarities = [VectorUtil.similarity(v1, v2) for v1 in vector_list_1 for v2 in vector_list_2]
        return np.mean(similarities) if similarities else 0.0

    @staticmethod
    def compute_idf_weight_dict(total_num: int, number_dict: dict) -> dict:
        """
        Calculate IDF weights using the formula log((total_num + 1) / (count + 1)).
        
        :param total_num: Total number of documents.
        :param number_dict: Dictionary with counts.
        :return: Dictionary with IDF weights.
        """
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}