import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def _validate_input(data):
        """Validates the input data format."""
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        if not data:
            return data  # Return empty list for consistent handling

        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError(
                    "Each item in the list must be a tuple of (results, ground_truth_num)."
                )

            results, ground_truth_num = item
            if not isinstance(results, list):
                raise TypeError("Results must be a list.")
            if not all(isinstance(r, (int, float)) and r in (0, 1) for r in results):
                raise ValueError("Results list must contain only 0 and 1.")
            if not isinstance(ground_truth_num, int):
                raise TypeError("Ground truth number must be an integer.")
        return data

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is the mean of reciprocal rank.
        :param data: A tuple or list of tuples, where each tuple contains:
                     - A list of 0s and 1s representing the results.
                     - An integer representing the total number of ground truth items.
        :return: A tuple containing:
                 - The mean reciprocal rank (MRR) value.
                 - A list of reciprocal ranks for each input item.
        """
        data = MetricsCalculator2._validate_input(data)
        if not data:
            return 0.0, [0.0]

        reciprocal_ranks = []
        for results, _ in data:
            try:
                rank = next((i + 1 for i, x in enumerate(results) if x == 1), None)
            except TypeError:
                raise TypeError("Results list must contain only 0 and 1.")

            if rank is not None:
                reciprocal_ranks.append(1.0 / rank)
            else:
                reciprocal_ranks.append(0.0)

        mrr_value = np.mean(reciprocal_ranks)
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is the mean of average precision.
        :param data: A tuple or list of tuples, where each tuple contains:
                     - A list of 0s and 1s representing the results.
                     - An integer representing the total number of ground truth items.
        :return: A tuple containing:
                 - The mean average precision (MAP) value.
                 - A list of average precisions for each input item.
        """
        data = MetricsCalculator2._validate_input(data)
        if not data:
            return 0.0, [0.0]

        average_precisions = []
        for results, ground_truth_num in data:
            cumulative_precision = 0.0
            relevant_count = 0
            for i, result in enumerate(results):
                if result == 1:
                    relevant_count += 1
                    cumulative_precision += float(relevant_count) / (i + 1)

            if ground_truth_num > 0:
                average_precision = (
                    cumulative_precision / ground_truth_num
                    if ground_truth_num > 0
                    else 0.0
                )
            else:
                average_precision = 0.0

            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions)
        return map_value, average_precisions