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
        """
        if not data:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            result, num_relevant = data
            ranks = np.where(np.array(result) == 1)[0]
            if len(ranks) > 0:
                rr = 1.0 / (ranks[0] + 1)
                return rr, [rr]
            else:
                return 0.0, [0.0]
        else:
            rr_list = []
            for item in data:
                result, num_relevant = item
                ranks = np.where(np.array(result) == 1)[0]
                if len(ranks) > 0:
                    rr = 1.0 / (ranks[0] + 1)
                    rr_list.append(rr)
                else:
                    rr_list.append(0.0)
            return np.mean(rr_list), rr_list

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
        """
        if not data:
            return 0.0, [0.0]

        if isinstance(data, tuple):
            result, num_relevant = data
            ap = 0.0
            relevant_count = 0
            for i, val in enumerate(result):
                if val == 1:
                    relevant_count += 1
                    ap += relevant_count / (i + 1)
            if num_relevant > 0:
                ap /= num_relevant
            return ap, [ap]
        else:
            ap_list = []
            for item in data:
                result, num_relevant = item
                ap = 0.0
                relevant_count = 0
                for i, val in enumerate(result):
                    if val == 1:
                        relevant_count += 1
                        ap += relevant_count / (i + 1)
                if num_relevant > 0:
                    ap /= num_relevant
                ap_list.append(ap)
            return np.mean(ap_list), ap_list