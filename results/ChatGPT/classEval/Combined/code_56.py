class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the counts for true positives, false positives, false negatives, and true negatives to 0.
        """
        self.reset()

    def reset(self):
        """Reset the metrics counts to 0."""
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts for true positives, false positives, false negatives, and true negatives.
        
        :param predicted_labels: list of predicted results
        :param true_labels: list of true labels
        :return: None
        """
        self.reset()  # Reset previous counts
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
        Calculate precision based on the current counts.
        
        :return: float
        """
        total_predicted_positive = self.true_positives + self.false_positives
        return self.true_positives / total_predicted_positive if total_predicted_positive > 0 else 0.0

    def recall(self):
        """
        Calculate recall based on the current counts.
        
        :return: float
        """
        total_actual_positive = self.true_positives + self.false_negatives
        return self.true_positives / total_actual_positive if total_actual_positive > 0 else 0.0

    def f1_score(self):
        """
        Calculate F1 score, which is the harmonic mean of precision and recall.
        
        :return: float
        """
        prec = self.precision()
        rec = self.recall()
        return (2 * prec * rec / (prec + rec)) if (prec + rec) > 0 else 0.0

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy based on predicted and true labels.
        
        :param predicted_labels: list of predicted results
        :param true_labels: list of true labels
        :return: float
        """
        if not predicted_labels:
            return 0.0
        correct_predictions = sum(p == t for p, t in zip(predicted_labels, true_labels))
        return correct_predictions / len(predicted_labels)