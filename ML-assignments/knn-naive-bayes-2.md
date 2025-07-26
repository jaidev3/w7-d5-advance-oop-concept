Theory
1. What is the intuition behind the KNN algorithm? How does it make a prediction for a new data point?
The intuition behind KNN is that similar data points tend to be close to each other in the feature space. It is a lazy learning algorithm that doesn't build a model during training but instead memorizes the training data. To make a prediction for a new data point, KNN identifies the k closest training examples (neighbors) based on a distance metric, then assigns the class label by majority vote among those neighbors.

2. Discuss how Euclidean, Manhattan, and Minkowski distances differ and their implications in KNN.
Euclidean distance: Measures the straight-line distance between two points, calculated as √(∑(x_i - y_i)²). It is sensitive to large differences in individual features and works well when features are on similar scales.
Manhattan distance: Measures the sum of absolute differences, calculated as ∑|x_i - y_i|. It is useful in grid-like spaces or high-dimensional data where paths are along axes, and it's less sensitive to outliers than Euclidean.
Minkowski distance: A generalization, calculated as (∑|x_i - y_i|^p)^(1/p), where p=2 is Euclidean and p=1 is Manhattan. The choice of p affects sensitivity to feature scales and dimensionality; lower p is better for sparse data, while higher p emphasizes larger differences.
In KNN, the choice of distance affects how neighbors are selected. Euclidean is common for continuous data, Manhattan for categorical or sparse, and Minkowski allows tuning for optimal performance.

3. Mention three advantages and three drawbacks of using KNN in practical settings.
Advantages:

Simple to implement and understand, with no assumptions about data distribution.
Naturally handles multi-class classification and adapts to local data structure.
No training phase, making it fast to "train" on new data.
Drawbacks:

Computationally intensive during prediction, especially with large datasets, as it requires calculating distances to all training points.
Sensitive to irrelevant or noisy features and requires feature scaling.
Suffers from the curse of dimensionality in high-dimensional spaces, where distances become less meaningful.
4. What is conditional probability, and how is it related to the working of Naive Bayes classifiers?
Conditional probability is the probability of an event A occurring given that event B has occurred, denoted as P(A|B) = P(A and B) / P(B).

In Naive Bayes classifiers, it is used via Bayes' theorem to compute the posterior probability P(class|features) = [P(features|class) * P(class)] / P(features). The algorithm estimates these probabilities from training data to predict the most likely class for new instances.

5. Why is the assumption of independence critical in Naive Bayes? What are the consequences if this assumption fails?
The independence assumption simplifies the computation by allowing P(features|class) = ∏ P(feature_i|class), reducing complexity from exponential to linear in the number of features.

If the assumption fails (features are correlated), the probability estimates can be inaccurate, leading to biased predictions. However, Naive Bayes often performs well in practice even with violated assumptions, especially in high-dimensional data like text classification.

6. Differentiate between the types of Naive Bayes classifiers and their suitability for different data types.
Gaussian Naive Bayes: Assumes features follow a normal distribution; suitable for continuous or real-valued data (e.g., measurements in the Wine dataset).
Multinomial Naive Bayes: Assumes features are multinomially distributed (e.g., word counts); ideal for discrete count data like text documents vectorized by term frequency.
Bernoulli Naive Bayes: Assumes binary features (presence/absence); suitable for binary data, such as word occurrence in short texts or document classification where feature count is ignored.
7. List and explain at least two significant conceptual differences between KNN and Naive Bayes models.
Learning Approach: KNN is a lazy, non-parametric learner that stores data and computes at prediction time without building a model. Naive Bayes is an eager, parametric learner that builds a probabilistic model during training based on feature distributions.
Basis for Prediction: KNN uses similarity via distance metrics to find neighbors, making it instance-based. Naive Bayes uses probability theory and Bayes' theorem, assuming feature independence, making it probability-based and faster for prediction.