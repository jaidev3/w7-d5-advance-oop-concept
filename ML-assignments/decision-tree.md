Q1. Explain the concept of a Decision Tree. What kind of problems is it best suited for?
A decision tree is a supervised machine learning model that represents decisions and their possible consequences in a tree-like structure. It starts with a root node, which represents the entire dataset, and splits the data into subsets based on feature values through internal nodes, leading to leaf nodes that represent the final outcome or prediction. Each branch represents a decision rule based on a feature, and the tree is built by recursively selecting the best feature to split the data to maximize separation between classes or minimize error.
Decision trees are best suited for classification and regression problems where the data has clear decision boundaries and interpretability is important. They work well with both categorical and numerical data, handle non-linear relationships, and are useful in scenarios like medical diagnosis, credit risk assessment, or customer segmentation. They are particularly effective when the relationships between features and the target can be explained by simple if-then rules.
Q2. Define the following terms with examples:

Root Node: The topmost node in a decision tree that represents the entire dataset before any splits. It is the starting point for decision-making. Example: In a decision tree for classifying animals as mammals or non-mammals, the root node might be the question "Does it have fur?" applied to all animals.
Leaf Node: The terminal nodes at the bottom of the tree where no further splits occur, representing the final prediction or class label. Example: In the animal classification tree, a leaf node might be "Mammal" if the path leads to animals with fur and warm blood.
Internal Node: Nodes between the root and leaves that represent decision points based on a feature split. They have child nodes and branches. Example: In the same tree, an internal node could be "Is it warm-blooded?" splitting from the fur question.
Branch: A path from a node to its child node, representing a specific outcome of a decision rule (e.g., yes/no or a value range). Example: From the root node "Does it have fur?", one branch might be "Yes" leading to mammals, and "No" leading to further questions.

Q3. What is Entropy? How is it used in a Decision Tree? Provide a mathematical example.
Entropy is a measure of impurity or disorder in a dataset, originating from information theory. In decision trees, it quantifies how mixed the classes are in a subset. Lower entropy means the subset is more pure (mostly one class), while higher entropy indicates more mixture.
Entropy is used as a criterion to select the best feature for splitting the data at each node. The goal is to choose the split that reduces entropy the most, leading to purer subsets.
Mathematical formula for entropy $ H(S) $ of a set $ S $ with $ c $ classes:
$ H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i) $
where $ p_i $ is the proportion of class $ i $ in $ S $.
Example: Suppose we have a dataset of 10 samples: 6 edible mushrooms (E) and 4 poisonous (P).
$ p_E = 6/10 = 0.6 $, $ p_P = 4/10 = 0.4 $
$ H(S) = - (0.6 \log_2(0.6) + 0.4 \log_2(0.4)) \approx - (0.6 \times -0.737 + 0.4 \times -1.322) \approx 0.971 $
If a split on "odor" creates two subsets: Left (all E, entropy=0), Right (all P, entropy=0), the weighted entropy after split is 0, making it a perfect split.
Q4. What is Information Gain? How does it help in building a Decision Tree? Show a small example using a feature with two values.
Information Gain (IG) measures how much entropy is reduced by splitting the dataset on a particular feature. It helps in building a decision tree by selecting the feature with the highest IG at each node, ensuring the most informative splits first.
Formula:
$ IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v) $
where $ A $ is the feature, $ S_v $ is the subset for value $ v $, $ H(S) $ is parent entropy, and the sum is weighted child entropies.
Example: Using the dataset from Q3 (10 samples: 6E, 4P, H(S)=0.971).
Feature "bruises" with two values: Yes (5 samples: 4E, 1P), No (5 samples: 2E, 3P).
Entropy Yes: $ - (4/5 \log_2(4/5) + 1/5 \log_2(1/5)) \approx 0.722 $
Entropy No: $ - (2/5 \log_2(2/5) + 3/5 \log_2(3/5)) \approx 0.971 $
Weighted entropy: (5/10)*0.722 + (5/10)*0.971 ≈ 0.8465
IG = 0.971 - 0.8465 ≈ 0.1245
If another feature has higher IG, it would be chosen instead.
Q5. Compare Gini Impurity and Entropy as criteria in Decision Trees. When would you prefer one over the other?
Gini Impurity and Entropy are both measures of node purity in decision trees, used to evaluate splits.

Gini Impurity: Measures the probability of incorrectly classifying a randomly chosen element if labeled randomly according to the class distribution. Formula: $ Gini(S) = 1 - \sum_{i=1}^{c} p_i^2 $. Ranges from 0 (pure) to 0.5 (max impurity for binary).
Entropy: Measures disorder based on information theory, as above. Ranges from 0 (pure) to 1 (max for binary).

Comparison:

Both lead to similar trees, but Gini is computationally faster (no log) and tends to isolate the most frequent class.
Entropy might produce slightly more balanced trees and is better for probabilistic interpretations.

Prefer Gini when computational efficiency is key (large datasets) or for binary classification. Prefer Entropy when you need a measure tied to information theory or when splits need to maximize information (e.g., in ensembles like Random Forests for diversity).