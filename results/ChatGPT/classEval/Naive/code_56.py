class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples (true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None
        """
        for pred, true in zip(predicted_labels, true_labels):
            if pred == 1 and true == 1:
                self.true_positives += 1
            elif pred == 1 and true == 0:
                self.false_positives += 1
            elif pred == 0 and true == 1:
                self.false_negatives += 1
            elif pred == 0 and true == 0:
                self.true_negatives += 1

    def precision(self):
        """
        Calculate precision
        :return: float
        """
        total_predicted_positives = self.true_positives + self.false_positives
        return self.true_positives / total_predicted_positives if total_predicted_positives > 0 else 0.0

    def recall(self):
        """
        Calculate recall
        :return: float
        """
        total_actual_positives = self.true_positives + self.false_negatives
        return self.true_positives / total_actual_positives if total_actual_positives > 0 else 0.0

    def f1_score(self):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :return: float
        """
        precision_val = self.precision()
        recall_val = self.recall()
        return 2 * (precision_val * recall_val) / (precision_val + recall_val) if (precision_val + recall_val) > 0 else 0.0

    def accuracy(self):
        """
        Calculate accuracy
        :return: float
        """
        total_samples = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        return (self.true_positives + self.true_negatives) / total_samples if total_samples > 0 else 0.0