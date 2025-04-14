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
        if not isinstance(data, list) and not isinstance(data, tuple):
            raise TypeError("Input data must be a list or tuple.")

        if not data:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (result_list, ground_truth_num).")

            result_list, ground_truth_num = item
            if not isinstance(result_list, list):
                raise TypeError("Result list must be a list.")

            try:
                ground_truth_num = int(ground_truth_num)
            except:
                raise TypeError("ground_truth_num must be int.")

            if ground_truth_num == 0:
                reciprocal_ranks.append(0.0)
                continue

            rank = 0
            for i, result in enumerate(result_list):
                if result == 1:
                    rank = i + 1
                    break

            if rank > 0:
                reciprocal_ranks.append(1.0 / rank)
            else:
                reciprocal_ranks.append(0.0)

        if not reciprocal_ranks:
            return 0.0, [0.0]

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
        if not isinstance(data, list) and not isinstance(data, tuple):
            raise TypeError("Input data must be a list or tuple.")

        if not data:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in the list must be a tuple of (result_list, ground_truth_num).")

            result_list, ground_truth_num = item
            if not isinstance(result_list, list):
                raise TypeError("Result list must be a list.")
            try:
                ground_truth_num = int(ground_truth_num)
            except:
                raise TypeError("ground_truth_num must be int.")

            if ground_truth_num == 0:
                average_precisions.append(0.0)
                continue

            cumulative_precision = 0.0
            relevant_count = 0
            for i, result in enumerate(result_list):
                if result == 1:
                    relevant_count += 1
                    cumulative_precision += float(relevant_count) / (i + 1)

            if relevant_count > 0:
                average_precision = cumulative_precision / ground_truth_num
                average_precisions.append(average_precision)
            else:
                average_precisions.append(0.0)

        if not average_precisions:
            return 0.0, [0.0]

        return np.mean(average_precisions), average_precisions