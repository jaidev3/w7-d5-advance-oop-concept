### Q1. What is Logistic Regression? How is it different from Linear Regression?

Linear regression is utilized for regression tasks, while logistic regression helps accomplish classification tasks.


Supervised machine learning is a widely used machine learning technique that predicts future outcomes or events. It uses labeled datasets to learn and generate accurate predictions. Supervised learning is classified into two categories, namely, regression and classification.

Regression is a model that predicts continuous values (numerical), while classification mainly classifies the data. Regression is accomplished by using a linear regression algorithm, and classification is achieved through logistic regression. This article highlights the critical differences between linear and logistic regression.

### 3 Practical Differences:

1. Mathematical formula
2. Kind of prediction
3. Grapical representation curve

1. **Type of Output:**

   * **Linear Regression:** Produces a continuous output, which can take any value (e.g., house price prediction).
   * **Logistic Regression:** Produces a probability between 0 and 1, which is used to determine the class label (e.g., whether an email is spam or not).

   Example:

   * **Linear Regression:** Predicting the price of a house.
   * **Logistic Regression:** Predicting whether an email is spam (1) or not spam (0).

2. **Assumption of Relationship:**

   * **Linear Regression:** Assumes a linear relationship between input features and the target variable.
   * **Logistic Regression:** Assumes a nonlinear relationship, specifically a logistic or S-shaped curve, between the input features and the probability of the target class.

3. **Error Measurement:**

   * **Linear Regression:** Uses Mean Squared Error (MSE) or similar methods for error measurement.
   * **Logistic Regression:** Uses Log-Loss or Cross-Entropy loss to measure error.

---

### Q2. Explain the mathematical formulation of Logistic Regression. What is the role of the sigmoid function? Write the formula for the sigmoid function and explain its output behavior.

**Mathematical Formulation:**

The model predicts the probability of the positive class (class 1) using the logistic function. The formula for logistic regression is:

$$
P(y=1 | X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1X_1 + \beta_2X_2 + \dots + \beta_nX_n)}}
$$

Where:

* $P(y=1 | X)$ is the probability of the positive class given input features $X$.
* $X_1, X_2, \dots, X_n$ are the independent variables (features).
* $\beta_0, \beta_1, \dots, \beta_n$ are the coefficients (parameters) of the model.
* $e$ is Euler's number, the base of the natural logarithm.

**Role of the Sigmoid Function:**

The sigmoid function squashes the output of the linear combination of inputs (which can range from $-\infty$ to $+\infty$) into a probability between 0 and 1.

**Sigmoid Function Formula:**

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where $z = \beta_0 + \beta_1X_1 + \dots + \beta_nX_n$.

**Output Behavior:**

* When $z$ is large and positive, $\sigma(z) \to 1$ (probability near 1).
* When $z$ is large and negative, $\sigma(z) \to 0$ (probability near 0).
* When $z = 0$, $\sigma(z) = 0.5$, representing the point of indifference (equal chance of class 1 or 0).

---

### Q3. What is the decision boundary in logistic regression? How is it determined?

The **decision boundary** is the threshold that separates the predicted positive class (1) from the negative class (0). It is determined by finding the value of the feature combination $X_1, X_2, \dots, X_n$ for which the predicted probability equals 0.5.

Mathematically, this is when the sigmoid function's output equals 0.5:

$$
\sigma(\beta_0 + \beta_1X_1 + \dots + \beta_nX_n) = 0.5
$$

This leads to the equation:

$$
\beta_0 + \beta_1X_1 + \dots + \beta_nX_n = 0
$$

This equation defines the **decision boundary**, which is a hyperplane in the feature space. For two features, this is a straight line, and for higher-dimensional spaces, it becomes a hyperplane.

---

### Q4. Define the following terms with respect to classification model evaluation:

1. **Accuracy:**
   Accuracy is the proportion of correct predictions (both true positives and true negatives) out of all predictions. It is given by:

   $$
   \text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Predictions}}
   $$

2. **Precision:**
   Precision (or Positive Predictive Value) is the proportion of positive predictions that are actually correct. It is given by:

   $$
   \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
   $$

3. **Recall:**
   Recall (or Sensitivity or True Positive Rate) is the proportion of actual positives that are correctly identified by the model. It is given by:

   $$
   \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
   $$

4. **F1-Score:**
   The F1-Score is the harmonic mean of Precision and Recall. It balances both metrics, especially when there is an uneven class distribution:

   $$
   \text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
   $$

5. **Confusion Matrix:**
   A confusion matrix is a table used to evaluate the performance of a classification model. It shows the counts of true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN).

   $$
   \begin{matrix}
   & Predicted = 1 & Predicted = 0 \\
   Actual = 1 & TP & FN \\
   Actual = 0 & FP & TN \\
   \end{matrix}
   $$

6. **ROC-AUC Curve:**
   The **Receiver Operating Characteristic (ROC)** curve is a graphical representation of the true positive rate (Recall) vs. the false positive rate (FPR). The **AUC (Area Under the Curve)** measures the overall performance of the model, with a higher value indicating better model performance.

---

### Q5. What assumptions does logistic regression make? When might these assumptions be violated in real datasets?

**Assumptions of Logistic Regression:**

1. **Linearity in the log-odds:** Logistic regression assumes a linear relationship between the independent variables and the log-odds of the dependent variable.
2. **Independence of observations:** The observations should be independent of each other.
3. **No multicollinearity:** The independent variables should not be highly correlated with each other.
4. **Large sample size:** Logistic regression performs best with large datasets, especially when there are many predictors.

**When Assumptions are Violated:**

1. **Non-linearity:** If the relationship between the independent variables and the target is not linear, logistic regression might not be the best choice.
2. **Correlated Observations:** In time series data or data with clustered observations, the independence assumption is violated.
3. **Multicollinearity:** High correlations between predictors can lead to issues in estimating the model parameters.
4. **Small sample sizes:** Logistic regression may not perform well on small datasets, leading to overfitting or poor generalization.
