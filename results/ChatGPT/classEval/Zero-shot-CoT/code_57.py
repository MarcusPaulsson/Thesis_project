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
        
        reciprocal_ranks = []
        precisions = []
        
        for actual, ground in data:
            if ground == 0:
                reciprocal_ranks.append(0.0)
                precisions.append(0.0)
                continue
            
            rank = next((i + 1 for i, x in enumerate(actual) if x == 1), None)
            if rank is None:
                reciprocal_ranks.append(0.0)
                precisions.append(0.0)
            else:
                reciprocal_ranks.append(1.0 / rank)
                precisions.append(sum(actual[:rank]) / rank)

        mrr_value = np.mean(reciprocal_ranks)
        return mrr_value, precisions

    @staticmethod
    def map(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")
        
        if isinstance(data, tuple):
            data = [data]
        
        average_precisions = []

        for actual, ground in data:
            if ground == 0:
                average_precisions.append(0.0)
                continue
            
            correct = np.cumsum(actual)
            precisions = correct / (np.arange(len(actual)) + 1)
            ap = np.sum(precisions * actual) / ground
            average_precisions.append(ap)

        map_value = np.mean(average_precisions)
        return map_value, average_precisions