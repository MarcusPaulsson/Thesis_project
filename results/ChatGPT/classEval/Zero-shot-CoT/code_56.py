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
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
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

    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        if len(predicted_labels) == 0:
            return 0.0
        correct_predictions = 0
        for pred, true in zip(predicted_labels, true_labels):
            if pred == true:
                correct_predictions += 1
        return correct_predictions / len(predicted_labels)