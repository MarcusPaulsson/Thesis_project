import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data,
    where MRR measures the ranking quality and MAP measures the average precision.
    """

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a list of tuples, where each tuple contains (actual result, ground truth num).
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: A tuple of the mean MRR value and a list of reciprocal ranks for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for actual, total in data:
            if total <= 0:
                reciprocal_ranks.append(0.0)
                continue

            rank = next((i + 1 for i, value in enumerate(actual) if value == 1), None)
            reciprocal_ranks.append(1 / rank if rank is not None else 0.0)

        mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a list of tuples, where each tuple contains (actual result, ground truth num).
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: A tuple of the mean MAP value and a list of average precisions for each input.
        """
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")

        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for actual, total in data:
            if total <= 0:
                average_precisions.append(0.0)
                continue

            relevant_count = 0
            precision_sum = 0.0
            for i, value in enumerate(actual):
                if value == 1:
                    relevant_count += 1
                    precision_sum += relevant_count / (i + 1)

            ap_value = precision_sum / relevant_count if relevant_count > 0 else 0.0
            average_precisions.append(ap_value)

        map_value = np.mean(average_precisions) if average_precisions else 0.0
        return map_value, average_precisions