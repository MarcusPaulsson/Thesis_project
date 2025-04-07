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
            raise ValueError("Input data must be a tuple or list")
        
        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for actual, ground_truth in data:
            if ground_truth <= 0:
                reciprocal_ranks.append(0.0)
                continue
            
            try:
                rank = next(i + 1 for i, value in enumerate(actual) if value == 1)
                reciprocal_ranks.append(1.0 / rank)
            except StopIteration:
                reciprocal_ranks.append(0.0)

        mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        if not isinstance(data, (tuple, list)):
            raise ValueError("Input data must be a tuple or list")
        
        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for actual, ground_truth in data:
            if ground_truth <= 0:
                average_precisions.append(0.0)
                continue
            
            num_correct = 0
            precision_sum = 0
            
            for i, value in enumerate(actual):
                if value == 1:
                    num_correct += 1
                    precision_sum += num_correct / (i + 1)

            average_precision = precision_sum / min(num_correct, ground_truth) if num_correct > 0 else 0.0
            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions) if average_precisions else 0.0
        return map_value, average_precisions