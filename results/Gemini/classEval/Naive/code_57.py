import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
        if not isinstance(data, list):
            data = [data]

        reciprocal_ranks = []
        for item in data:
            results, ground_truth_num = item
            try:
                first_relevant_rank = results.index(1) + 1
                reciprocal_rank = 1.0 / first_relevant_rank
            except ValueError:
                reciprocal_rank = 0.0
            reciprocal_ranks.append(reciprocal_rank)

        mrr_value = np.mean(reciprocal_ranks)
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
        if not isinstance(data, list):
            data = [data]

        average_precisions = []
        for item in data:
            results, ground_truth_num = item
            relevant_count = 0
            precision_sum = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    relevant_count += 1
                    precision_sum += float(relevant_count) / (i + 1)

            if ground_truth_num > 0:
                average_precision = precision_sum / ground_truth_num
            else:
                average_precision = 0.0
            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions)
        return map_value, average_precisions