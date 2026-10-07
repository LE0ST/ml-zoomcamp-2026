# Module 2: Machine Learning for Regression

This module covers linear regression from scratch using the Normal Equation, validation frameworks, evaluation with Root Mean Squared Error (RMSE), feature engineering, and regularization (Ridge regression).

---

## 📚 Module Topics

1. **Linear Regression:**
   - Vector form of linear regression: $g(x) = w_0 + x_1 w_1 + \dots + x_n w_n = X w$.
   - Normal Equation: $w = (X^T X)^{-1} X^T y$.
2. **Validation Framework:**
   - Splitting data into Training (60%), Validation (20%), and Test (20%) sets.
   - Shuffling indices reproducibly with `np.random.seed` and `np.random.shuffle`.
3. **Model Evaluation:**
   - Root Mean Squared Error (RMSE): $\text{RMSE} = \sqrt{\frac{1}{m} \sum (g(x_i) - y_i)^2}$.
4. **Missing Values & Imputation:**
   - Handling missing features with constant fill (`0`) vs statistical fill (`mean`).
   - Computing imputation parameters strictly on the training set to prevent data leakage.
5. **Regularization (Ridge Regression):**
   - Preventing singular Gram matrices and large weights: $(X^T X + r I)^{-1} X^T y$.
   - Tuning the hyperparameter $r$ using the validation set.

---

## 📝 Deliverable

- **Homework 2:** [`homework.ipynb`](homework.ipynb)
