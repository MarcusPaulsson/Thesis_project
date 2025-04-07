import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or a tuple.")

        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for actual, total in data:
            if total <= 0:
                reciprocal_ranks.append(0.0)
                continue
            
            first_correct_index = next((i for i, x in enumerate(actual) if x == 1), None)
            if first_correct_index is not None:
                reciprocal_ranks.append(1.0 / (first_correct_index + 1))
            else:
                reciprocal_ranks.append(0.0)

        mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or a tuple.")

        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for actual, total in data:
            if total <= 0:
                average_precisions.append(0.0)
                continue
            
            correct_count = 0
            precision_sum = 0.0

            for i, x in enumerate(actual):
                if x == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)

            average_precision = precision_sum / min(correct_count, total) if correct_count > 0 else 0.0
            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions) if average_precisions else 0.0
        return map_value, average_precisions