import numpy as np

class MetricsCalculator:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP)
    based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is the mean of reciprocal rank.
        :param data: A tuple or list of tuples containing binary results and ground truth size.
        :return: Tuple of overall MRR and list of MRR for each input.
        """
        MetricsCalculator._validate_input(data)

        mrr_values = []
        
        for result, ground_truth in data:
            reciprocal_rank = MetricsCalculator._compute_reciprocal_rank(result)
            mrr_values.append(reciprocal_rank if ground_truth > 0 else 0.0)

        overall_mrr = np.mean(mrr_values) if mrr_values else 0.0
        return overall_mrr, mrr_values

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is the mean of average precision (AP).
        :param data: A tuple or list of tuples containing binary results and ground truth size.
        :return: Tuple of overall MAP and list of MAP for each input.
        """
        MetricsCalculator._validate_input(data)

        ap_values = []
        
        for result, ground_truth in data:
            average_precision = MetricsCalculator._compute_average_precision(result, ground_truth)
            ap_values.append(average_precision)

        overall_map = np.mean(ap_values) if ap_values else 0.0
        return overall_map, ap_values

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input data must be a list or tuple.")
        
        if isinstance(data, tuple):
            data = [data]

    @staticmethod
    def _compute_reciprocal_rank(result):
        for idx, value in enumerate(result):
            if value == 1:
                return 1.0 / (idx + 1)
        return 0.0

    @staticmethod
    def _compute_average_precision(result, ground_truth):
        precision_sum = 0.0
        correct_count = 0
        
        for idx, value in enumerate(result):
            if value == 1:
                correct_count += 1
                precision_sum += correct_count / (idx + 1)
        
        return precision_sum / min(correct_count, ground_truth) if correct_count > 0 else 0.0