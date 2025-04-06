import numpy as np

class MetricsCalculator:
    """
    The class provides methods to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data,
    where MRR measures the ranking quality and MAP measures the average precision.
    """

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data.
        :param data: A tuple or a list of tuples, where each tuple contains the actual results (list of 0s and 1s) and the total number of ground truths.
        :return: A tuple containing the mean MRR and a list of MRR scores for each input.
        """
        if isinstance(data, tuple):
            data = [data]
        
        mrr_scores = []
        
        for actual_results, _ in data:
            if not actual_results:
                mrr_scores.append(0.0)
                continue
            
            reciprocal_rank = next((1 / (idx + 1) for idx, value in enumerate(actual_results) if value == 1), 0.0)
            mrr_scores.append(reciprocal_rank)

        return np.mean(mrr_scores), mrr_scores

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data.
        :param data: A tuple or a list of tuples, where each tuple contains the actual results (list of 0s and 1s) and the total number of ground truths.
        :return: A tuple containing the mean MAP and a list of MAP scores for each input.
        """
        if isinstance(data, tuple):
            data = [data]
        
        map_scores = []
        
        for actual_results, ground_truth_num in data:
            if not actual_results or ground_truth_num == 0:
                map_scores.append(0.0)
                continue
            
            relevant_count = 0
            precision_at_k = []

            for idx, value in enumerate(actual_results):
                if value == 1:
                    relevant_count += 1
                    precision_at_k.append(relevant_count / (idx + 1))
            
            average_precision = np.mean(precision_at_k) if precision_at_k else 0.0
            map_scores.append(average_precision)

        return np.mean(map_scores), map_scores