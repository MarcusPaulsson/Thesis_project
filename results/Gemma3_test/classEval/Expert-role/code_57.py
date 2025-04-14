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
            rank = np.where(np.array(result) == 1)[0]
            if rank.size > 0:
                return 1.0 / (rank[0] + 1), [1.0 / (rank[0] + 1)]
            else:
                return 0.0, [0.0]
        elif isinstance(data, list):
            rr_list = []
            precision_list = []
            for item in data:
                result, ground_truth_num = item
                rank = np.where(np.array(result) == 1)[0]
                if rank.size > 0:
                    rr_list.append(1.0 / (rank[0] + 1))
                    precision_list.append(1.0 / (rank[0] + 1))
                else:
                    rr_list.append(0.0)
                    precision_list.append(0.0)
            return np.mean(rr_list), precision_list
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
            relevant_count = 0
            for i, item in enumerate(result):
                if item == 1:
                    relevant_count += 1
                    ap += relevant_count / (i + 1)
            if ground_truth_num > 0:
                return ap / ground_truth_num, [ap / ground_truth_num]
            else:
                return 0.0, [0.0]
        elif isinstance(data, list):
            ap_list = []
            for item in data:
                result, ground_truth_num = item
                ap = 0.0
                relevant_count = 0
                for i, res in enumerate(result):
                    if res == 1:
                        relevant_count += 1
                        ap += relevant_count / (i + 1)
                if ground_truth_num > 0:
                    ap_list.append(ap / ground_truth_num)
                else:
                    ap_list.append(0.0)
            return np.mean(ap_list), ap_list
        else:
            return 0.0, [0.0]