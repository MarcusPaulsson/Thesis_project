class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the counts for true positives, false positives, false negatives, and true negatives.
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts of true positives, false positives, false negatives, and true negatives
        based on the predicted and true labels.

        :param predicted_labels: list, predicted results (0 or 1)
        :param true_labels: list, true labels (0 or 1)
        :raises ValueError: if the lengths of predicted_labels and true_labels are not equal.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("The lengths of predicted_labels and true_labels must be equal.")

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted not in (0, 1) or true not in (0, 1):
                raise ValueError("predicted_labels and true_labels must contain only 0 or 1")
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            else:  # predicted == 0 and true == 0
                self.true_negatives += 1

    def _calculate_precision(self):
        """
        Calculate precision based on the stored counts.
        :return: float, precision
        """
        tp = self.true_positives
        fp = self.false_positives
        if tp + fp == 0:
            return 0.0
        return tp / (tp + fp)

    def _calculate_recall(self):
        """
        Calculate recall based on the stored counts.
        :return: float, recall
        """
        tp = self.true_positives
        fn = self.false_negatives
        if tp + fn == 0:
            return 0.0
        return tp / (tp + fn)

    def _calculate_accuracy(self):
        """
        Calculate accuracy based on the stored counts.
        :return: float, accuracy
        """
        correct = self.true_positives + self.true_negatives
        total = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        if total == 0:
            return 0.0
        return correct / total

    def precision(self):
        """
        Calculate precision using the accumulated counts.
        :return: float, precision
        """
        return self._calculate_precision()

    def recall(self):
        """
        Calculate recall using the accumulated counts.
        :return: float, recall
        """
        return self._calculate_recall()

    def f1_score(self):
        """
        Calculate F1 score, the harmonic mean of precision and recall, using the accumulated counts.
        :return: float, F1 score
        """
        precision_val = self._calculate_precision()
        recall_val = self._calculate_recall()
        if precision_val + recall_val == 0:
            return 0.0
        return 2 * (precision_val * recall_val) / (precision_val + recall_val)

    def accuracy(self):
        """
        Calculate accuracy using the accumulated counts.
        :return: float, accuracy
        """
        return self._calculate_accuracy()