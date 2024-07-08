MACHINE LEARNING

OPEN ENDED LAB

BY

MIRZA TAHA HASSAN (CS-21018)
SHAYAN ZAHID (CS-21026)
IBRAHIM NAZIR (CS-21037)
MUHAMMAD ABDURRAHMAN (CS-21107)


SUBMITTED TO:
MS. MAHNOOR MALIK



DEPARTMENT OF COMPUTER & INFORMATION SYSTEMS ENGINEERING

Detecting Credit Card Transaction Fraud Using Machine Learning Algorithms

Introduction

Credit card fraud is a significant issue in the financial industry, leading to substantial financial losses. Detecting fraudulent transactions is challenging due to the imbalanced nature of the data, with legitimate transactions vastly outnumbering fraudulent ones. In this project, we implemented and compared four machine learning algorithms to detect credit card transaction fraud: Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, and Random Forest.

Data Preprocessing

Before applying machine learning algorithms, the following preprocessing steps were undertaken:

1. Data Cleaning: Handling missing values and erroneous data.
2. Feature Scaling: Normalizing the data using StandardScaler.
3. Train-Test Split: Splitting the data into training (80%) and testing (20%) sets.
4. Handling Imbalance using undersampling technique.

 Machine Learning Algorithms

 1. Logistic Regression
Logistic Regression is a statistical method for analyzing a dataset in which there are one or more independent variables that determine an outcome. 
In this project, we used Logistic Regression to predict the probability of a transaction being fraudulent.
Working Principle:

●	The model uses a logistic function to model a binary dependent variable.

●	It predicts the probability of an instance belonging to a class (fraudulent or non-fraudulent) using the logistic function.

●	The threshold is typically set at 0.5, but this can be adjusted to manage precision and recall trade-offs.

 3. K-Nearest Neighbors (KNN)
KNN is a simple, instance-based learning algorithm where the classification of a sample is based on the majority class among its k-nearest neighbors.
Working Principle:

●	It calculates the distance (typically Euclidean) between the test data point and all training data points.

●	Selects the 'k' nearest neighbors (where k is a user-defined constant).

●	Assigns the class based on the majority vote of the nearest neighbors.

 5. Decision Tree
A Decision Tree is a flowchart-like tree structure where an internal node represents a feature (or attribute), the branch represents a decision rule, and each leaf node represents the outcome. It is a non-parametric supervised learning method used for classification and regression.
Working Principle:

●	Starts at the root node and splits the data based on the feature that results in the highest information gain (or lowest Gini impurity).

●	Recursively splits the subsets into smaller subsets.

●	Continues until all data points are classified or a stopping criterion (such as maximum depth) is reached.

 7. Random Forest

Random Forest is an ensemble learning method that operates by constructing multiple decision trees during training and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.
Working Principle:

●	Creates multiple decision trees using bootstrapped subsets of the data.

●	Each tree is constructed with a random subset of features.

●	Predictions are made by averaging the predictions of all individual trees (for regression) or by majority vote (for classification).


 Results

Algorithm	Accuracy	Precision 	Recall	F1 Score

Decision Tree	0.9911	0.99	0.99	0.99

K-Nearest Neighbors	0.9881	0.99      	0.99      	0.99      

Logistic Regression	0.8962	0.90      	0.90      	0.90      

Random Forest	0.9923	0.99      	0.99      	0.99      

Discussion

In our machine learning project, we evaluated the performance of four different models: K-Nearest Neighbors (KNN), Logistic Regression, Decision Tree, and Random Forest. We considered various metrics such as accuracy, precision, F1 score, and computational efficiency to compare these models.

●	Decision Tree: The Decision Tree model demonstrated a strong balance across multiple metrics, including accuracy, precision, and F1 score. Importantly, it also excelled in terms of computational efficiency. Given its relatively fast training and prediction times, the Decision Tree is considered favorable choice when time efficiency is a critical factor.

●	Random Forest: The Random Forest model achieved higher precision and F1 scores compared to the other models. However, it is computationally intensive and has significantly longer training and prediction times. If time efficiency is not a primary concern, Random Forest stands out as the best-performing model due to its superior accuracy and robust performance across different metrics.

●	K-Nearest Neighbors (KNN): The KNN model, characterized as a lazy learner, provided good accuracy. However, its need to learn the dataset each time it makes a prediction leads to longer prediction times. Given these time constraints, KNN is less favorable compared to the Decision Tree for this dataset.

●	Logistic Regression: The Logistic Regression model exhibited slightly lower accuracy relative to the other models. While it is computationally efficient, its performance metrics do not match those of the Decision Tree or Random Forest, making it a less suitable choice for this particular dataset.
Limitations

Our evaluation was subject to several limitations:

●	Computational Resources: We faced constraints in terms of available computational power and RAM. This significantly impacted our ability to handle the large dataset efficiently.

●	Time Constraints: Training models on the entire dataset required substantial time, which was not feasible given our limitations.

To address these challenges, we opted to undersample our dataset. This approach reduced the time and computational resources required for training, making it more manageable within our constraints. However, undersampling may have affected the overall performance and generalizability of the models.

Suggestions for Improvement

●	Increase Computational Resources: Utilizing more powerful hardware or cloud-based solutions could allow for training on the full dataset, potentially improving model performance.

●	Optimize Model Parameters: Further tuning of hyperparameters for each model could yield better results, especially for complex models like Random Forest.

●	Advanced Sampling Techniques: Instead of undersampling, employing techniques like SMOTE (Synthetic Minority Over-sampling Technique) could help in maintaining a balanced dataset without losing valuable information.

●	Efficient Code Writing: Improving the efficiency of our code can significantly reduce training times. Writing clean, optimized code that minimizes computational overhead will enhance performance and make better use of available resources. As compared to sci-learn libraries, our code takes a little more time so efficient programming would take less time

By addressing these limitations and implementing the suggested improvements, we can further enhance the performance and reliability of our machine learning models.

Conclusion

Considering all factors, the Decision Tree model is the most balanced and efficient choice, particularly when time is a significant constraint. For scenarios where computational time is less critical, the Random Forest model would be preferred due to its higher precision and F1 scores. KNN and Logistic Regression, while competent, do not offer the same level of overall performance and efficiency for this dataset.
Future work could include exploring more advanced techniques such as deep learning, tuning hyperparameters more extensively, and utilizing real-time data to enhance the detection system's robustness.



