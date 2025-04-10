import numpy as np

class MetricsCalculator:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data,
    where MRR measures the ranking quality and MAP measures the average precision.
    """

    @staticmethod
    def validate_data(data):
        if not isinstance(data, (list, tuple)) or (isinstance(data, tuple) and len(data) != 2):
            raise ValueError("Input data must be a list or tuple of (result, ground_truth).")

    @staticmethod
    def mrr(data):
        """
        Compute the Mean Reciprocal Rank (MRR) of the input data.
        
        :param data: A list of tuples where each tuple contains a list of results (0s and 1s) and an integer ground truth.
        :return: A tuple containing the MRR value and a list of reciprocal ranks for each input.
        """
        MetricsCalculator.validate_data(data)
        
        if isinstance(data, tuple):
            data = [data]

        reciprocal_ranks = []
        for result, ground_truth in data:
            if ground_truth <= 0:
                reciprocal_ranks.append(0.0)
                continue
            
            ranks = [i + 1 for i, val in enumerate(result) if val == 1]
            reciprocal_ranks.append(1.0 / ranks[0] if ranks else 0.0)

        mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0.0
        return mrr_value, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the Mean Average Precision (MAP) of the input data.
        
        :param data: A list of tuples where each tuple contains a list of results (0s and 1s) and an integer ground truth.
        :return: A tuple containing the MAP value and a list of average precision values for each input.
        """
        MetricsCalculator.validate_data(data)

        if isinstance(data, tuple):
            data = [data]

        average_precisions = []
        for result, ground_truth in data:
            if ground_truth <= 0:
                average_precisions.append(0.0)
                continue

            correct_count = 0
            precision_sum = 0.0
            for i, val in enumerate(result):
                if val == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)

            average_precision = precision_sum / correct_count if correct_count > 0 else 0.0
            average_precisions.append(average_precision)

        map_value = np.mean(average_precisions) if average_precisions else 0.0
        return map_value, average_precisions