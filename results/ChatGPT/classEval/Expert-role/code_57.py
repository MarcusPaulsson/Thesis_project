import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, 
    where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if not isinstance(data, (tuple, list)):
            raise ValueError("Input must be a tuple or list.")
        
        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for actual, ground_truth_num in data:
            if ground_truth_num <= 0:
                reciprocal_ranks.append(0.0)
                continue
            
            rank = next((i + 1 for i, value in enumerate(actual) if value == 1), None)
            if rank is not None:
                reciprocal_ranks.append(1 / rank)
            else:
                reciprocal_ranks.append(0.0)
        
        mrr_value = np.mean(reciprocal_ranks)
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        if not isinstance(data, (tuple, list)):
            raise ValueError("Input must be a tuple or list.")
        
        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for actual, ground_truth_num in data:
            if ground_truth_num <= 0:
                average_precisions.append(0.0)
                continue
            
            precision_sum = 0.0
            correct_count = 0
            for i, value in enumerate(actual):
                if value == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)

            average_precision = precision_sum / ground_truth_num
            average_precisions.append(average_precision)
        
        map_value = np.mean(average_precisions)
        return map_value, average_precisions