class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the count of true positives, false positives, false negatives, and true negatives to 0.
        """
        self.reset()

    def reset(self):
        """Reset the metrics counters to zero."""
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts of true positives, false positives, false negatives, and true negatives based on the predictions and true labels.
        
        :param predicted_labels: list of predicted results
        :param true_labels: list of true labels
        :return: None
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("Length of predicted_labels and true_labels must be the same.")

        self.reset()  # Reset counts before updating
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            elif predicted == 0 and true == 0:
                self.true_negatives += 1

    def precision(self):
        """
        Calculate precision.
        
        :return: float
        """
        total_positive_predictions = self.true_positives + self.false_positives
        return self.true_positives / total_positive_predictions if total_positive_predictions > 0 else 0.0

    def recall(self):
        """
        Calculate recall.
        
        :return: float
        """
        total_actual_positives = self.true_positives + self.false_negatives
        return self.true_positives / total_actual_positives if total_actual_positives > 0 else 0.0

    def f1_score(self):
        """
        Calculate F1 score, which is the harmonic mean of precision and recall.
        
        :return: float
        """
        p = self.precision()
        r = self.recall()
        return 2 * (p * r) / (p + r) if (p + r) > 0 else 0.0

    def accuracy(self):
        """
        Calculate accuracy.
        
        :return: float
        """
        total = self.true_positives + self.true_negatives + self.false_positives + self.false_negatives
        return (self.true_positives + self.true_negatives) / total if total > 0 else 0.0