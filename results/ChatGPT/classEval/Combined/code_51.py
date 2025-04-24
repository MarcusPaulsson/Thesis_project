import numpy as np

class KappaCalculator:
    """
    This class calculates Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(confusion_matrix):
        """
        Calculate Cohen's kappa value from a confusion matrix.
        
        :param confusion_matrix: A square matrix representing the confusion matrix.
        :return: float, the Cohen's kappa value.
        """
        total = np.sum(confusion_matrix)
        observed_agreement = np.sum(np.diag(confusion_matrix)) / total
        expected_agreement = np.sum(np.sum(confusion_matrix, axis=0) ** 2) / (total ** 2)
        
        if expected_agreement == 1:
            return 1.0  # Perfect agreement
        if expected_agreement == 0:
            return 0.0  # No agreement
        
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(data_matrix, num_samples, num_categories, num_raters):
        """
        Calculate Fleiss' kappa value from a data matrix.
        
        :param data_matrix: Input data matrix, shape (num_samples, num_categories).
        :param num_samples: int, Number of samples.
        :param num_categories: int, Number of categories.
        :param num_raters: int, Number of raters.
        :return: float, Fleiss' kappa value.
        """
        p = np.sum(data_matrix, axis=0) / (num_samples * num_raters)
        P_e = np.sum(p ** 2)
        
        P_o = np.sum(np.sum(data_matrix ** 2, axis=1) - num_raters) / (num_samples * num_raters * (num_raters - 1))
        
        if P_e == 1:
            return 1.0  # Perfect agreement
        if P_e == 0:
            return 0.0  # No agreement
        
        fleiss_kappa_value = (P_o - P_e) / (1 - P_e)
        return fleiss_kappa_value