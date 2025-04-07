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
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == 1 and true_label == 1:
                self.true_positives += 1
            elif predicted_label == 1 and true_label == 0:
                self.false_positives += 1
            elif predicted_label == 0 and true_label == 1:
                self.false_negatives += 1
            elif predicted_label == 0 and true_label == 0:
                self.true_negatives += 1


    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        fp = 0
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == 1 and true_label == 1:
                tp += 1
            elif predicted_label == 1 and true_label == 0:
                fp += 1
        if tp + fp == 0:
            return 0.0
        return tp / (tp + fp)


    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        tp = 0
        fn = 0
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == 1 and true_label == 1:
                tp += 1
            elif predicted_label == 0 and true_label == 1:
                fn += 1
        if tp + fn == 0:
            return 0.0
        return tp / (tp + fn)


    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        prec = self.precision(predicted_labels, true_labels)
        rec = self.recall(predicted_labels, true_labels)
        if prec + rec == 0:
            return 0.0
        return 2 * (prec * rec) / (prec + rec)


    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        correct = 0
        total = len(predicted_labels)
        if total == 0 :
            return 0.0
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == true_label:
                correct += 1
        return correct / total