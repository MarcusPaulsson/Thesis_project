import numpy as np
from numpy import dot
from numpy.linalg import norm


class VectorUtil:
    """
    Provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between two vectors.

        Args:
            vector_1 (numpy.ndarray): The first vector (dim,).
            vector_2 (numpy.ndarray): The second vector (dim,).

        Returns:
            float: The cosine similarity between the two vectors.  Returns 0.0 if either vector has a norm of 0.
        """
        vector_1 = np.asarray(vector_1)
        vector_2 = np.asarray(vector_2)

        norm_1 = norm(vector_1)
        norm_2 = norm(vector_2)

        if norm_1 == 0.0 or norm_2 == 0.0:
            return 0.0

        return dot(vector_1, vector_2) / (norm_1 * norm_2)

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a list of other vectors.

        Args:
            vector_1 (numpy.ndarray): The vector from which similarities are computed (dim,).
            vectors_all (list of numpy.ndarray): A list of vectors to compare against (num_vectors, dim).

        Returns:
            list of float: A list containing the cosine similarity between `vector_1` and each vector in `vectors_all`.
        """
        vector_1 = np.asarray(vector_1)
        vectors_all = [np.asarray(v) for v in vectors_all]

        similarities = []
        for vector_2 in vectors_all:
            norm_1 = norm(vector_1)
            norm_2 = norm(vector_2)

            if norm_1 == 0.0 or norm_2 == 0.0:
                similarities.append(0.0)
            else:
                similarities.append(dot(vector_1, vector_2) / (norm_1 * norm_2))
        return similarities

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute the average maximum cosine similarity between two sets of vectors.

        For each vector in vector_list_1, finds the maximum cosine similarity with any vector in vector_list_2.
        The function then returns the average of these maximum similarities.

        Args:
            vector_list_1 (list of numpy.ndarray): A list of vectors.
            vector_list_2 (list of numpy.ndarray): A list of vectors.

        Returns:
            float: The average maximum cosine similarity between the two sets of vectors. Returns 0.0 if either list is empty.
        """
        if not vector_list_1 or not vector_list_2:
            return 0.0

        vector_list_1 = [np.asarray(v) for v in vector_list_1]
        vector_list_2 = [np.asarray(v) for v in vector_list_2]

        sum_similarity = 0.0
        for vector1 in vector_list_1:
            max_similarity = 0.0
            for vector2 in vector_list_2:
                norm_1 = norm(vector1)
                norm_2 = norm(vector2)
                if norm_1 == 0.0 or norm_2 == 0.0:
                    similarity = 0.0
                else:
                    similarity = dot(vector1, vector2) / (norm_1 * norm_2)
                max_similarity = max(max_similarity, similarity)
            sum_similarity += max_similarity

        return sum_similarity / len(vector_list_1)

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate the Inverse Document Frequency (IDF) weight for each key in a dictionary.

        IDF is calculated as log((total_num + 1) / (count + 1)) for each count in number_dict.

        Args:
            total_num (int): The total number of documents.
            number_dict (dict): A dictionary where keys are terms and values are their counts.

        Returns:
            dict: A dictionary containing the IDF weight for each term.
        """
        idf_weight_dict = {}
        for key, count in number_dict.items():
            idf_weight_dict[key] = np.log((total_num + 1) / (count + 1))
        return idf_weight_dict