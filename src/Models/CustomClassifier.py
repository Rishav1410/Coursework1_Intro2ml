import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature       # Feature index for the split
        self.threshold = threshold   # Threshold value for the split
        self.left = left             # Left child node
        self.right = right           # Right child node
        self.value = value           # Leaf node value (class label)
        
    def is_leaf(self):
        return self.value is not None

class DecisionTree:
    def __init__(self):
        self.root = None

    def fit(self, dataset):
        self.root, depth= self.decision_tree_learning(dataset)
        return self.root, depth

    def entropy(self, y):
        if len(y) == 0 :
            return 0
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return -np.sum([probability * np.log2(probability) for probability in probabilities if probability > 0])  # Avoid log(0)

    def information_gain(self, y, y_left, y_right):
        return self.entropy(y) - (len(y_left) / len(y) * self.entropy(y_left) + len(y_right) / len(y) * self.entropy(y_right))

    def find_split(self, dataset):
        X, y = dataset[:, :-1], dataset[:, -1]  # Split dataset into features and labels
        n_examples, n_features = X.shape
        best_gain = -1
        best_feature, best_threshold = None, None
        

        for feature in range(n_features):
            # Sort the dataset by the current feature
            sorted_indices = np.argsort(X[:, feature])
            sorted_X = X[sorted_indices]
            sorted_y = y[sorted_indices]

            for i in range(1, n_examples):
                # Calculate the threshold as the midpoint between two consecutive points
                if sorted_X[i, feature] != sorted_X[i - 1, feature]:
                    threshold = (sorted_X[i, feature] + sorted_X[i - 1, feature]) / 2
                    left_indices = sorted_y[:i]
                    right_indices = sorted_y[i:]
                        
                    gain = self.information_gain(sorted_y, left_indices, right_indices)

                    if gain > best_gain:
                        best_gain = gain
                        best_feature = feature
                        best_threshold = threshold

        return best_feature, best_threshold

    def split_dataset(self, dataset, feature, threshold):
        left_indices = dataset[:, feature] < threshold
        right_indices = dataset[:, feature] >= threshold
        return dataset[left_indices], dataset[right_indices]
    
    def traverse_tree(self, X, node : Node):
        if node.is_leaf():
            return node.value
        
        if X[node.feature] < node.threshold:
            return self.traverse_tree(X, node.left)
        else:
            return self.traverse_tree(X, node.right)
        

    def decision_tree_learning(self, dataset, depth=0):
        y = dataset[:, -1]  # Extract labels from the last column
        
        if  len(np.unique(y)) == 1 or len(set(y)) == 1:
            return Node(value=y[0]), depth  # Leaf node

        split = self.find_split(dataset)
        
        node = Node(feature= split[0], threshold= split[1])
        
        l_dataset, r_dataset = self.split_dataset(dataset, split[0], split[1])
        
        l_branch, l_depth = self.decision_tree_learning(l_dataset, depth + 1)
        r_branch, r_depth = self.decision_tree_learning(r_dataset, depth + 1)
        
        node.left, node.right = l_branch, r_branch

        return node, max(l_depth, r_depth)

    def predict(self, X):
        return np.array(self.traverse_tree(X, self.root))
        
    
    def find_depth(self, node : Node): # An utility method to calculate the current depth
        if node.is_leaf():
            return 0
        return 1 + max(self.find_depth(node.left), self.find_depth(node.right))

    def prune(self, node, validation_dataset):     
        #Check an edge case 
        if node is None:
            return None

        
        if node.is_leaf():
            return node  # It's already a leaf, no need to prune !!

        # Prune the left and right subtrees
        if node.left is not None:
            node.left = self.prune(node.left, validation_dataset)
        if node.right is not None:
            node.right = self.prune(node.right, validation_dataset)

        
        # Calculate accuracy before pruning (the current node is non-leaf)
        before_prune_accuracy = self.accuracy(validation_dataset)

        # Convert current node to a leaf node with the majority class
        class_counts = {}
        for sample in validation_dataset:
            label = sample[-1]
            if label in class_counts:
                class_counts[label] += 1
            else:
                class_counts[label] = 1
        majority_class = max(class_counts, key=class_counts.get) # Get the label with majority 
        
        node.value = majority_class  # Replace with majority class

        # Calculate accuracy after pruning
        after_prune_accuracy = self.accuracy(validation_dataset)

        # If accuracy improved, we keep the leaf; otherwise, revert back to the previous state
        if after_prune_accuracy < before_prune_accuracy:
            node.value = None  # Revert to non-leaf node
            

        return node

    def accuracy(self, dataset):
        predictions = np.array([self.predict(sample[:-1]) for sample in dataset])
        return np.mean(predictions == dataset[:, -1])
    
    