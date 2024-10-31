import numpy as np

def evaluate(test_dataset, decision_tree, num_classes):
    # Initialize confusion matrix
    confusion = np.zeros((num_classes, num_classes), dtype=int)
    # Populate confusion matrix using true and predicted labels from test dataset
    y_gold = test_dataset[:,-1]
    x_test = test_dataset[:,:-1]
    y_prediction= np.array([decision_tree.predict(x) for x in x_test])
    for true_label, predicted_label in zip(y_gold,y_prediction):
        true_label = int(true_label -1)
        predicted_label = int(predicted_label -1)
        confusion[true_label][ predicted_label] += 1
    # Calculate True Positives, False Positives, False Negatives
    tp = np.diag(confusion)
    fp = np.sum(confusion, axis=0) - tp
    fn = np.sum(confusion, axis=1) - tp
    # Calculate Accuracy, Precision, Recall, and F1 Score for each class
    accuracy = np.trace(confusion) / np.sum(confusion) if np.sum(confusion) > 0 else 0
    precision = tp / (tp + fp) if (tp.any() + fp.any()) > 0 else 0  
    recall = tp / (tp + fn) if (tp.any() + fn.any()) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if(precision.any() + recall.any()) > 0 else 0
    return confusion, precision, recall, accuracy, f1_score