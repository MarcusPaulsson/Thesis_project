class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of true positives, false positives, false negatives, and true negatives to 0.
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts of true positives, false positives, false negatives, and true negatives
        based on the predicted and true labels.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :raises ValueError: if predicted_labels and true_labels have different lengths.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("predicted_labels and true_labels must have the same length")

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

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, precision score. Returns 0.0 if no positive predictions are made.
        """
        tp = 0
        fp = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 1 and true == 0:
                fp += 1

        if tp + fp == 0:
            return 0.0
        return tp / (tp + fp)

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, recall score. Returns 0.0 if no actual positives are present.
        """
        tp = 0
        fn = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                tp += 1
            elif predicted == 0 and true == 1:
                fn += 1

        if tp + fn == 0:
            return 0.0
        return tp / (tp + fn)

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate F1 score, the harmonic mean of precision and recall.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, F1 score. Returns 0.0 if both precision and recall are 0.
        """
        precision_value = self.precision(predicted_labels, true_labels)
        recall_value = self.recall(predicted_labels, true_labels)

        if precision_value + recall_value == 0:
            return 0.0

        return 2 * (precision_value * recall_value) / (precision_value + recall_value)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, accuracy score. Returns 0.0 if the input lists are empty.
        """
        correct = 0
        total = len(predicted_labels)
        if total == 0:
            return 0.0

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                correct += 1

        return correct / total