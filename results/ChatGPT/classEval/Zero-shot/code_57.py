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
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        mrr_sum = 0.0
        precisions = []

        for item in data:
            results, ground_truth_num = item
            if not isinstance(results, list) or len(results) == 0:
                precisions.append(0.0)
                continue

            rank = next((i + 1 for i, value in enumerate(results) if value == 1), None)
            reciprocal_rank = 1.0 / rank if rank is not None else 0.0
            mrr_sum += reciprocal_rank

            precision = sum(results[:ground_truth_num]) / min(len(results[:ground_truth_num]), ground_truth_num) if ground_truth_num > 0 else 0.0
            precisions.append(precision)

        return (mrr_sum / len(data), precisions)

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),
        ground truth num is the total ground num. ([1,0,...],5), or list of tuple eg. 
        [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)]. 1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        map_sum = 0.0
        average_precisions = []

        for item in data:
            results, ground_truth_num = item
            if not isinstance(results, list) or len(results) == 0:
                average_precisions.append(0.0)
                continue

            num_relevant = 0
            precision_sum = 0.0

            for i, value in enumerate(results):
                if value == 1:
                    num_relevant += 1
                    precision_sum += num_relevant / (i + 1)

            average_precision = precision_sum / num_relevant if num_relevant > 0 else 0.0
            average_precisions.append(average_precision)
            map_sum += average_precision

        return (map_sum / len(data), average_precisions)