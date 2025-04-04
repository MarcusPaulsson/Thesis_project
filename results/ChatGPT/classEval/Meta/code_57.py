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
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  
        In each tuple (actual result, ground truth num), ground truth num is the total ground num.
        :return: if input data is list, return the MRR of this list. if the input data is list of list, return the
        average MRR on all lists. The second return value is a list of MRR for each input.
        """
        if isinstance(data[0], tuple):
            results = []
            for result in data:
                actual, ground_truth = result
                rank = np.where(np.array(actual) == 1)[0]
                if len(rank) > 0:
                    mrr_value = 1 / (rank[0] + 1)
                else:
                    mrr_value = 0.0
                results.append(mrr_value)
            return np.mean(results), results
        else:
            actual, ground_truth = data
            rank = np.where(np.array(actual) == 1)[0]
            if len(rank) > 0:
                return 1 / (rank[0] + 1), [1 / (rank[0] + 1)]
            else:
                return 0.0, [0.0]

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  
        In each tuple (actual result, ground truth num), ground truth num is the total ground num.
        :return: if input data is list, return the MAP of this list. if the input data is list of list, return the
        average MAP on all lists. The second return value is a list of MAP for each input.
        """
        if isinstance(data[0], tuple):
            results = []
            for result in data:
                actual, ground_truth = result
                precision_sum = 0.0
                relevant_count = 0
                for i in range(len(actual)):
                    if actual[i] == 1:
                        relevant_count += 1
                        precision_sum += relevant_count / (i + 1)
                map_value = precision_sum / relevant_count if relevant_count > 0 else 0.0
                results.append(map_value)
            return np.mean(results), results
        else:
            actual, ground_truth = data
            precision_sum = 0.0
            relevant_count = 0
            for i in range(len(actual)):
                if actual[i] == 1:
                    relevant_count += 1
                    precision_sum += relevant_count / (i + 1)
            return precision_sum / relevant_count if relevant_count > 0 else 0.0, [precision_sum / relevant_count if relevant_count > 0 else 0.0]