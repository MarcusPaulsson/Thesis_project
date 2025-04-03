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
        :return: if input data is list, return the MRR of this list. if the input data is list of list, return the
        average MRR on all list. The second return value is a list of precision for each input.
        """
        if isinstance(data, tuple):
            data = [data]

        mrr_list = []
        for actual, ground_truth in data:
            rank = next((i + 1 for i, val in enumerate(actual) if val == 1), None)
            reciprocal_rank = 1 / rank if rank is not None else 0
            mrr_list.append(reciprocal_rank)

        mean_mrr = np.mean(mrr_list)
        return mean_mrr, mrr_list

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the MAP of this list. if the input data is list of list, return the
        average MAP on all list. The second return value is a list of precision for each input.
        """
        if isinstance(data, tuple):
            data = [data]

        map_list = []
        for actual, ground_truth in data:
            relevant_count = 0
            precision_sum = 0
            
            for i, val in enumerate(actual):
                if val == 1:
                    relevant_count += 1
                    precision_sum += relevant_count / (i + 1)

            avg_precision = precision_sum / min(relevant_count, ground_truth) if relevant_count > 0 else 0
            map_list.append(avg_precision)

        mean_map = np.mean(map_list)
        return mean_map, map_list