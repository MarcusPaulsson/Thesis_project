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
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),
         ground truth num is the total ground num. ([1,0,...],5), or list of tuple eg. 
         [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]. 1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the MRR of this list. if the input data is list of list, return the
        average MRR on all lists. The second return value is a list of MRR for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        1.0, [1.0]
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.75, [1.0, 0.5]
        """
        if isinstance(data, tuple):
            results, ground_truth = data
            ranks = [1 / (i + 1) for i in range(len(results)) if results[i] == 1]
            mrr_value = np.mean(ranks) if ranks else 0.0
            return mrr_value, [mrr_value]
        elif isinstance(data, list):
            mrr_values = []
            for results, ground_truth in data:
                ranks = [1 / (i + 1) for i in range(len(results)) if results[i] == 1]
                mrr_value = np.mean(ranks) if ranks else 0.0
                mrr_values.append(mrr_value)
            return np.mean(mrr_values), mrr_values
        else:
            raise ValueError("Input data must be a tuple or a list of tuples.")

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),
         ground truth num is the total ground num. ([1,0,...],5), or list of tuple eg. 
         [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]. 1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the MAP of this list. if the input data is list of list, return the
        average MAP on all lists. The second return value is a list of MAP for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        0.41666666666666663, [0.41666666666666663]
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        if isinstance(data, tuple):
            results, ground_truth = data
            ap = MetricsCalculator2._average_precision(results, ground_truth)
            return ap, [ap]
        elif isinstance(data, list):
            aps = []
            for results, ground_truth in data:
                ap = MetricsCalculator2._average_precision(results, ground_truth)
                aps.append(ap)
            return np.mean(aps), aps
        else:
            raise ValueError("Input data must be a tuple or a list of tuples.")

    @staticmethod
    def _average_precision(results, ground_truth):
        """
        Compute the Average Precision (AP) for a single results list.
        :param results: List of binary values indicating correct (1) or incorrect (0) answers.
        :param ground_truth: Total number of relevant items.
        :return: Average Precision value.
        """
        if ground_truth == 0:
            return 0.0
        
        relevant_count = 0
        precision_sum = 0.0
        for i, result in enumerate(results):
            if result == 1:
                relevant_count += 1
                precision_sum += relevant_count / (i + 1)

        return precision_sum / min(ground_truth, relevant_count) if relevant_count > 0 else 0.0