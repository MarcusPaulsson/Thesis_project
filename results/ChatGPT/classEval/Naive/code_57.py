import numpy as np

class MetricsCalculator2:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP)
    based on input data. MRR measures the ranking quality, while MAP measures the average precision.
    """

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data.
        
        :param data: A tuple or list containing the actual results and total ground truth.
                     - A tuple: ([1,0,...], 5)
                     - A list of tuples: [([1,0,1,...], 5), ([1,0,...], 6)]
        :return: The MRR value and a list of reciprocal ranks for each input.
        """
        if isinstance(data, tuple):
            data = [data]
        
        reciprocal_ranks = []
        
        for results, ground_truth in data:
            rank = next((i + 1 for i, val in enumerate(results) if val == 1), None)
            reciprocal_rank = 1 / rank if rank else 0
            reciprocal_ranks.append(reciprocal_rank)
        
        mean_reciprocal_rank = np.mean(reciprocal_ranks)
        return mean_reciprocal_rank, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data.
        
        :param data: A tuple or list containing the actual results and total ground truth.
                     - A tuple: ([1,0,...], 5)
                     - A list of tuples: [([1,0,1,...], 5), ([1,0,...], 6)]
        :return: The MAP value and a list of average precision for each input.
        """
        if isinstance(data, tuple):
            data = [data]
        
        average_precisions = []

        for results, ground_truth in data:
            correct_count = 0
            precision_sum = 0
            
            for i, val in enumerate(results):
                if val == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)
            
            average_precision = precision_sum / (correct_count if correct_count > 0 else 1)
            average_precisions.append(average_precision)

        mean_average_precision = np.mean(average_precisions)
        return mean_average_precision, average_precisions