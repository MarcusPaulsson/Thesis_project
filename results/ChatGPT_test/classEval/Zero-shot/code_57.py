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
            raise ValueError("Input data must be a list or tuple.")
        
        if isinstance(data, tuple):
            data = [data]

        mrr_values = []
        for actual, ground_truth in data:
            if ground_truth == 0:
                mrr_values.append(0.0)
                continue
            
            reciprocal_rank = 0.0
            for idx, value in enumerate(actual):
                if value == 1:
                    reciprocal_rank = 1 / (idx + 1)
                    break
            
            mrr_values.append(reciprocal_rank)

        mean_mrr = np.mean(mrr_values) if mrr_values else 0.0
        return mean_mrr, mrr_values

    @staticmethod
    def map(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")
        
        if isinstance(data, tuple):
            data = [data]

        ap_values = []
        for actual, ground_truth in data:
            if ground_truth == 0:
                ap_values.append(0.0)
                continue
            
            correct_count = 0
            precision_sum = 0.0
            
            for idx, value in enumerate(actual):
                if value == 1:
                    correct_count += 1
                    precision_sum += correct_count / (idx + 1)

            average_precision = precision_sum / min(correct_count, ground_truth) if correct_count > 0 else 0.0
            ap_values.append(average_precision)

        mean_map = np.mean(ap_values) if ap_values else 0.0
        return mean_map, ap_values