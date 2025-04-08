class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initializes the counts for true positives, false positives, false negatives, and true negatives.
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Updates the counts of true positives, false positives, false negatives, and true negatives
        based on the provided predicted and true labels.

        :param predicted_labels: A list of predicted labels (1 for positive, 0 for negative).
        :param true_labels: A list of true labels (1 for positive, 0 for negative).
        :raises ValueError: If the lengths of predicted_labels and true_labels are not equal.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("predicted_labels and true_labels must have the same length.")

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
        Calculates precision based on the predicted and true labels.

        :param predicted_labels: A list of predicted labels (1 for positive, 0 for negative).
        :param true_labels: A list of true labels (1 for positive, 0 for negative).
        :return: The precision score (float). Returns 0.0 if no positive predictions are made.
        :raises ValueError: If the lengths of predicted_labels and true_labels are not equal.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("predicted_labels and true_labels must have the same length.")

        true_positives = 0
        false_positives = 0

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 1 and true == 0:
                false_positives += 1

        if true_positives + false_positives == 0:
            return 0.0  # Avoid division by zero

        return true_positives / (true_positives + false_positives)

    def recall(self, predicted_labels, true_labels):
        """
        Calculates recall based on the predicted and true labels.

        :param predicted_labels: A list of predicted labels (1 for positive, 0 for negative).
        :param true_labels: A list of true labels (1 for positive, 0 for negative).
        :return: The recall score (float). Returns 0.0 if no actual positive cases are present.
        :raises ValueError: If the lengths of predicted_labels and true_labels are not equal.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("predicted_labels and true_labels must have the same length.")

        true_positives = 0
        false_negatives = 0

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 0 and true == 1:
                false_negatives += 1

        if true_positives + false_negatives == 0:
            return 0.0  # Avoid division by zero

        return true_positives / (true_positives + false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculates the F1 score based on the predicted and true labels.

        :param predicted_labels: A list of predicted labels (1 for positive, 0 for negative).
        :param true_labels: A list of true labels (1 for positive, 0 for negative).
        :return: The F1 score (float). Returns 0.0 if either precision or recall is 0.0.
        :raises ValueError: If the lengths of predicted_labels and true_labels are not equal.
        """
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)

        if precision + recall == 0:
            return 0.0  # Avoid division by zero

        return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculates accuracy based on the predicted and true labels.

        :param predicted_labels: A list of predicted labels (1 for positive, 0 for negative).
        :param true_labels: A list of true labels (1 for positive, 0 for negative).
        :return: The accuracy score (float). Returns 0.0 if the input lists are empty.
        :raises ValueError: If the lengths of predicted_labels and true_labels are not equal.
        """
        if len(predicted_labels) != len(true_labels):
            raise ValueError("predicted_labels and true_labels must have the same length.")

        correct_predictions = 0
        total_predictions = len(predicted_labels)

        if total_predictions == 0:
            return 0.0

        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                correct_predictions += 1

        return correct_predictions / total_predictions