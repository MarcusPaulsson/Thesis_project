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
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        if not data:
            return 0.0, [0.0]

        reciprocal_ranks = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (list, int).")

            results, ground_truth_num = item
            if not isinstance(results, list):
                raise TypeError("The first element of the tuple must be a list.")
            if not isinstance(ground_truth_num, int):
                raise TypeError("The second element of the tuple must be an integer.")

            rr = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    rr = 1.0 / (i + 1)
                    break
            reciprocal_ranks.append(rr)

        return np.mean(reciprocal_ranks), reciprocal_ranks

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
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        if not data:
            return 0.0, [0.0]

        average_precisions = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (list, int).")

            results, ground_truth_num = item
            if not isinstance(results, list):
                raise TypeError("The first element of the tuple must be a list.")
            if not isinstance(ground_truth_num, int):
                raise TypeError("The second element of the tuple must be an integer.")

            relevant_count = 0
            precision_sum = 0.0
            for i, result in enumerate(results):
                if result == 1:
                    relevant_count += 1
                    precision_sum += float(relevant_count) / (i + 1)

            ap = 0.0
            if min(ground_truth_num, len(results)) > 0:
                ap = precision_sum / min(ground_truth_num, len(results))
            
            average_precisions.append(ap)

        return np.mean(average_precisions), average_precisions