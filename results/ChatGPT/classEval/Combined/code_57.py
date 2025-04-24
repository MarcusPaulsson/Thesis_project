import numpy as np


class MetricsCalculator:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data.
    MRR measures the ranking quality, while MAP measures the average precision.
    """

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is the mean of reciprocal rank.
        :param data: A tuple or list of tuples where each tuple contains (actual results, ground truth count).
        :return: A tuple containing the MRR and a list of reciprocal ranks for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for actual, ground_truth_count in data:
            if ground_truth_count == 0:
                reciprocal_ranks.append(0.0)
                continue
            
            rank = next((i + 1 for i, value in enumerate(actual) if value == 1), None)
            reciprocal_rank = 1 / rank if rank is not None else 0.0
            reciprocal_ranks.append(reciprocal_rank)

        mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is the mean of average precision (AP).
        :param data: A tuple or list of tuples where each tuple contains (actual results, ground truth count).
        :return: A tuple containing the MAP and a list of average precision for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for actual, ground_truth_count in data:
            if ground_truth_count == 0:
                average_precisions.append(0.0)
                continue
            
            correct_count = 0
            precision_sum = 0.0
            
            for i, value in enumerate(actual):
                if value == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)

            average_precision = precision_sum / ground_truth_count if ground_truth_count > 0 else 0.0
            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions) if average_precisions else 0.0
        return map_value, average_precisions