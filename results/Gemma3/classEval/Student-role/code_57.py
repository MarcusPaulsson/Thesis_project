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
        if isinstance(data, tuple):
            result, ground_truth_num = data
            rank = 0
            for i, r in enumerate(result):
                if r == 1:
                    rank = i + 1
                    break
            if rank == 0:
                return 0.0, [0.0]
            else:
                return 1.0 / rank, [1.0 / rank]
        elif isinstance(data, list):
            if not data:
                return 0.0, [0.0]
            rr_list = []
            for d in data:
                result, ground_truth_num = d
                rank = 0
                for i, r in enumerate(result):
                    if r == 1:
                        rank = i + 1
                        break
                if rank == 0:
                    rr_list.append(0.0)
                else:
                    rr_list.append(1.0 / rank)
            return np.mean(rr_list), rr_list
        else:
            return 0.0, [0.0]

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
        if isinstance(data, tuple):
            result, ground_truth_num = data
            ap = 0.0
            correct_count = 0
            for i, r in enumerate(result):
                if r == 1:
                    correct_count += 1
                    ap += correct_count / (i + 1)
            if ground_truth_num == 0:
                return 0.0, [0.0]
            else:
                return ap / min(ground_truth_num, correct_count), [ap / min(ground_truth_num, correct_count)]
        elif isinstance(data, list):
            if not data:
                return 0.0, [0.0]
            ap_list = []
            for d in data:
                result, ground_truth_num = d
                ap = 0.0
                correct_count = 0
                for i, r in enumerate(result):
                    if r == 1:
                        correct_count += 1
                        ap += correct_count / (i + 1)
                if ground_truth_num == 0:
                    ap_list.append(0.0)
                else:
                    ap_list.append(ap / min(ground_truth_num, correct_count))
            return np.mean(ap_list), ap_list
        else:
            return 0.0, [0.0]