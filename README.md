# property_violations_platform
<img width="1434" alt="Screenshot 2024-09-07 at 23 47 59" src="https://github.com/user-attachments/assets/7d46d69f-1850-4045-93b7-6612d6a5c3fb">


Project Aim
The primary goal of this project is to demonstrate how AI-based predictions can be practically integrated into existing applications to improve efficiency and decision-making processes. The AI model leverages historical violation data to predict future violations, allowing users to preemptively address potential issues. The project serves as an example of how AI can enhance data-driven processes in various industries without requiring complex or costly infrastructure.

Features
Predicts violation categories based on user inputs.
Real-time insights with instant prediction results.
Seamless integration of AI and machine learning into an existing web application.

Tech Stack

React (TypeScript): For building an interactive and dynamic user interface.

Flask: A lightweight web framework for building REST APIs.

TensorFlow: For building and training the machine learning model that powers the prediction engine.
Pandas and Scikit-learn: For data preprocessing, feature scaling, and model evaluation.
Flask-CORS: To handle cross-origin requests from the frontend.
Deployment:


Historical property violation data from NYC Open Data: https://data.cityofnewyork.us

Data Preprocessing Notes
<img width="810" alt="Screenshot 2024-09-07 at 23 53 27" src="https://github.com/user-attachments/assets/0054a9c8-b541-413f-be23-812677ad55d7">
Scaling the Features:

The features are scaled using StandardScaler to ensure they have a mean of 0 and a standard deviation of 1, which helps in improving model performance:
Standard deviation of all scaled features is 1, ensuring that all features are on the same scale for better model performance.
