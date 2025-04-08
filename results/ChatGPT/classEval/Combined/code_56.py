class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of true positives, false positives, false negatives, and true negatives to 0.
        """
        self.reset_metrics()

    def reset_metrics(self):
        """Reset all metrics to zero."""
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts of true positives, false positives, false negatives, and true negatives.
        
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, updates the counts
        """
        self.reset_metrics()
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
        Calculate precision.
        
        :return: float
        """
        total_predicted_positive = self.true_positives + self.false_positives
        return self.true_positives / total_predicted_positive if total_predicted_positive else 0.0

    def recall(self):
        """
        Calculate recall.
        
        :return: float
        """
        total_actual_positive = self.true_positives + self.false_negatives
        return self.true_positives / total_actual_positive if total_actual_positive else 0.0

    def f1_score(self):
        """
        Calculate F1 score, which is the harmonic mean of precision and recall.
        
        :return: float
        """
        precision_value = self.precision()
        recall_value = self.recall()
        if precision_value + recall_value == 0:
            return 0.0
        return 2 * (precision_value * recall_value) / (precision_value + recall_value)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy.
        
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        if not predicted_labels or len(predicted_labels) != len(true_labels):
            return 0.0
        correct_predictions = sum(pred == true for pred, true in zip(predicted_labels, true_labels))
        return correct_predictions / len(true_labels)