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
        Compute the Mean Reciprocal Rank (MRR) of the input data.

        Args:
            data: A tuple or list of tuples. Each tuple contains:
                - result: A list or numpy array of 1s and 0s, where 1 indicates a correct answer and 0 indicates a wrong answer.
                - ground_truth_num: The total number of relevant items.

        Returns:
            A tuple containing:
                - The mean MRR across all input tuples.
                - A list of MRR values for each input tuple. Returns (0.0, []) if input data is invalid or empty.
        """
        if not data:
            return 0.0, []

        if isinstance(data, tuple):
            data = [data]

        if not isinstance(data, list):
            print("Warning: Input data should be a tuple or a list of tuples.")
            return 0.0, []

        rr_list = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                print("Warning: Each item in the list should be a tuple of (result, ground_truth_num).")
                return 0.0, []

            result, ground_truth_num = item

            if not isinstance(result, (list, np.ndarray)):
                print("Warning: Result should be a list or numpy array.")
                return 0.0, []

            if not all(r in [0, 1] for r in result):
                print("Warning: Result should contain only 0s and 1s.")
                return 0.0, []

            if not isinstance(ground_truth_num, int):
                print("Warning: ground_truth_num should be an integer.")
                return 0.0, []

            rr = 0
            for i, r in enumerate(result):
                if r == 1:
                    rr = 1 / (i + 1)
                    break
            rr_list.append(rr)

        return np.mean(rr_list) if rr_list else 0.0, rr_list

    @staticmethod
    def map(data):
        """
        Compute the Mean Average Precision (MAP) of the input data.

        Args:
            data: A tuple or list of tuples. Each tuple contains:
                - result: A list or numpy array of 1s and 0s, where 1 indicates a correct answer and 0 indicates a wrong answer.
                - ground_truth_num: The total number of relevant items.

        Returns:
            A tuple containing:
                - The mean MAP across all input tuples.
                - A list of MAP values for each input tuple.
        """
        if not data:
            return 0.0, []

        if isinstance(data, tuple):
            data = [data]

        if not isinstance(data, list):
            print("Warning: Input data should be a tuple or a list of tuples.")
            return (0.0, [])

        ap_list = []
        for item in data:
            if not isinstance(item, tuple) or len(item) != 2:
                print("Warning: Each item in the list should be a tuple of (result, ground_truth_num).")
                return (0.0, [])

            result, ground_truth_num = item

            if not isinstance(result, (list, np.ndarray)):
                print("Warning: Result should be a list or numpy array.")
                return (0.0, [])

            if not all(r in [0, 1] for r in result):
                print("Warning: Result should contain only 0s and 1s.")
                return (0.0, [])

            if not isinstance(ground_truth_num, int):
                print("Warning: ground_truth_num should be an integer.")
                return (0.0, [])
            
            if ground_truth_num < 0:
                print("Warning: ground_truth_num should be non-negative.")
                return (0.0, [])

            precision_sum = 0
            correct_count = 0
            for i, r in enumerate(result):
                if r == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)

            if ground_truth_num > 0:
                ap = precision_sum / ground_truth_num
            else:
                ap = 0.0
            ap_list.append(ap)

        return np.mean(ap_list) if ap_list else 0.0, ap_list