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
        
        for actual, ground_truth_num in data:
            if ground_truth_num == 0:
                reciprocal_ranks.append(0.0)
                continue
            
            rank = next((i + 1 for i, val in enumerate(actual) if val == 1), None)
            if rank is None:
                reciprocal_ranks.append(0.0)
            else:
                reciprocal_ranks.append(1 / rank)
        
        mean_reciprocal_rank = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mean_reciprocal_rank, reciprocal_ranks

    @staticmethod
    def map(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or a tuple.")
        
        if isinstance(data, tuple):
            data = [data]
        
        average_precisions = []
        
        for actual, ground_truth_num in data:
            if ground_truth_num == 0:
                average_precisions.append(0.0)
                continue
            
            correct_count = 0
            precision_sum = 0.0
            
            for i, val in enumerate(actual):
                if val == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)
            
            average_precision = precision_sum / ground_truth_num if ground_truth_num > 0 else 0.0
            average_precisions.append(average_precision)
        
        mean_average_precision = np.mean(average_precisions) if average_precisions else 0.0
        return mean_average_precision, average_precisions