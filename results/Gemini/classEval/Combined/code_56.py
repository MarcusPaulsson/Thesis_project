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

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :raises ValueError: if predicted_labels and true_labels have different lengths
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

        Precision is the ratio of correctly predicted positive observations to the total predicted positives.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, precision score
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

        Recall is the ratio of correctly predicted positive observations to the all observations in actual class - yes.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, recall score
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
        Calculate F1 score, which is the harmonic mean of precision and recall.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, F1 score
        """
        prec = self.precision(predicted_labels, true_labels)
        rec = self.recall(predicted_labels, true_labels)

        if prec + rec == 0:
            return 0.0
        return 2 * (prec * rec) / (prec + rec)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy.

        Accuracy is the ratio of correctly predicted observations to the total observations.

        :param predicted_labels: list, predicted results (1 for positive, 0 for negative)
        :param true_labels: list, true labels (1 for positive, 0 for negative)
        :return: float, accuracy score
        """
        correct = 0
        total = len(predicted_labels)
        if total == 0:
            return 0.0

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                correct += 1

        return correct / total