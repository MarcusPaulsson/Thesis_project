import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        Compute the Mean Reciprocal Rank (MRR) of the input data.

        Args:
            data: A tuple or list of tuples. Each tuple should be in the format
                  (results, ground_truth_num), where:
                  - results is a list of 1s and 0s, representing correct and
                    incorrect answers, respectively.
                  - ground_truth_num is the total number of ground truth items.

        Returns:
            A tuple containing:
            - The mean reciprocal rank (float).
            - A list of reciprocal ranks for each input tuple.
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
                raise ValueError(
                    "Each item in the list must be a tuple of (results, ground_truth_num)."
                )

            results, ground_truth_num = item
            if not isinstance(results, list):
                raise TypeError("Results must be a list.")

            try:
                rank = next(i + 1 for i, x in enumerate(results) if x == 1)
                reciprocal_rank = 1.0 / rank
            except StopIteration:
                reciprocal_rank = 0.0
            reciprocal_ranks.append(reciprocal_rank)

        mean_reciprocal_rank = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mean_reciprocal_rank, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the Mean Average Precision (MAP) of the input data.

        Args:
            data: A tuple or list of tuples. Each tuple should be in the format
                  (results, ground_truth_num), where:
                  - results is a list of 1s and 0s, representing correct and
                    incorrect answers, respectively.
                  - ground_truth_num is the total number of ground truth items.

        Returns:
            A tuple containing:
            - The mean average precision (float).
            - A list of average precisions for each input tuple.
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
                raise ValueError(
                    "Each item in the list must be a tuple of (results, ground_truth_num)."
                )

            results, ground_truth_num = item
            if not isinstance(results, list):
                raise TypeError("Results must be a list.")

            relevant_count = 0
            precision_sum = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    relevant_count += 1
                    precision_sum += float(relevant_count) / (i + 1)

            if ground_truth_num == 0:
                average_precision = 0.0
            else:
                average_precision = precision_sum / ground_truth_num

            average_precisions.append(average_precision)

        mean_average_precision = np.mean(average_precisions) if average_precisions else 0.0
        return mean_average_precision, average_precisions