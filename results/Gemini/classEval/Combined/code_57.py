import numpy as np


class MetricsCalculator2:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data.
    MRR measures the ranking quality, and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        Computes the Mean Reciprocal Rank (MRR) of the input data.

        :param data: A tuple or list of tuples, where each tuple contains:
                     - results: A list of integers (0 or 1) representing the correctness of ranked results. 1 indicates a correct result, 0 indicates an incorrect result.
                     - ground_truth_num: An integer representing the total number of relevant items.

        :return: A tuple containing:
                 - mean_rr: The mean reciprocal rank.
                 - reciprocal_ranks: A list of reciprocal ranks for each input tuple.

        :raises TypeError: If input data is not a list or tuple, or if 'results' is not a list, or if elements in 'results' are not 0 or 1.
        :raises ValueError: If items in the list are not tuples of (results, ground_truth_num).
        """

        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        if not data:
            return 0.0, [0.0]

        reciprocal_ranks = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (results, ground_truth_num).")

            results, ground_truth_num = item

            if not isinstance(results, list):
                raise TypeError("Results must be a list.")

            if not all(isinstance(r, (int, np.integer)) and r in (0, 1) for r in results):
                raise ValueError("Results must be a list of 0s and 1s.")

            rr = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    rr = 1.0 / (i + 1)
                    break  # Stop after the first relevant result
            reciprocal_ranks.append(rr)

        mean_rr = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mean_rr, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Computes the Mean Average Precision (MAP) of the input data.

        :param data: A tuple or list of tuples, where each tuple contains:
                     - results: A list of integers (0 or 1) representing the correctness of ranked results. 1 indicates a correct result, 0 indicates an incorrect result.
                     - ground_truth_num: An integer representing the total number of relevant items.

        :return: A tuple containing:
                 - mean_ap: The mean average precision.
                 - average_precisions: A list of average precisions for each input tuple.

        :raises TypeError: If input data is not a list or tuple, or if 'results' is not a list, or if elements in 'results' are not 0 or 1.
        :raises ValueError: If items in the list are not tuples of (results, ground_truth_num).
        """

        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        if not data:
            return 0.0, [0.0]

        average_precisions = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (results, ground_truth_num).")

            results, ground_truth_num = item

            if not isinstance(results, list):
                raise TypeError("Results must be a list.")

            if not all(isinstance(r, (int, np.integer)) and r in (0, 1) for r in results):
                raise ValueError("Results must be a list of 0s and 1s.")

            relevant_count = 0
            precision_sum = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    relevant_count += 1
                    precision_sum += float(relevant_count) / (i + 1)

            if ground_truth_num == 0:
                ap = 0.0
            else:
                ap = precision_sum / ground_truth_num

            average_precisions.append(ap)

        mean_ap = np.mean(average_precisions) if average_precisions else 0.0
        return mean_ap, average_precisions