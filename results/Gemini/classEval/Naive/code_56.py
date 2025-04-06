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
        Update the counts of true positives, false positives, false negatives, and true negatives.

        Args:
            predicted_labels (list): Predicted labels.
            true_labels (list): True labels.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("Predicted and true labels must have the same length.")

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            elif predicted == 0 and true == 0:
                self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision.

        Args:
            predicted_labels (list): Predicted labels.
            true_labels (list): True labels.

        Returns:
            float: Precision score. Returns 0 if no positive predictions are made.
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall.

        Args:
            predicted_labels (list): Predicted labels.
            true_labels (list): True labels.

        Returns:
            float: Recall score. Returns 0 if no actual positive samples are present.
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate F1 score, which is the harmonic mean of precision and recall.

        Args:
            predicted_labels (list): Predicted labels.
            true_labels (list): True labels.

        Returns:
            float: F1 score. Returns 0 if either precision or recall is 0.
        """
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)

        if precision + recall == 0:
            return 0.0

        return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy.

        Args:
            predicted_labels (list): Predicted labels.
            true_labels (list): True labels.

        Returns:
            float: Accuracy score.
        """
        self.update(predicted_labels, true_labels)
        total_samples = self.true_positives + self.false_positives + self.false_negatives + self.true_negatives
        if total_samples == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / total_samples