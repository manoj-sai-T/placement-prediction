# MBA Placement Prediction Project

This project predicts the likelihood of MBA graduates getting placed based on their academic and personal details using a machine learning model. The application includes a backend implemented in Python with Flask, and a frontend built with HTML, CSS, and JavaScript.

## Table of Contents
- [Project Structure](#project-structure)
- [Description](#description)
  - [Backend (Flask Application)](#backend-flask-application)
  - [Frontend](#frontend)
- [How to Run the Project](#how-to-run-the-project)
- [Dataset](#dataset)
- [Model](#model)
- [Conclusion](#conclusion)

## Project Structure

- **Root Directory**
  - `project.py`: Main Flask application file.
  - `templates/index.html`: HTML file for the frontend.
  - `static/script.js`: JavaScript file for handling frontend logic.
  - `static/styles.css`: CSS file for styling the frontend.
  - `files/dataset.csv`: Dataset used for training the machine learning model.

## Description

### Backend (Flask Application)
- **`project.py`**:
  - Loads and preprocesses the dataset by mapping categorical variables to numerical values.
  - Splits the data into training and testing sets and trains a logistic regression model.
  - Defines Flask app routes:
    - `/`: Serves the HTML file.
    - `/predict`: Accepts POST requests with student data, makes predictions using the trained model, and returns the result as JSON.

### Frontend
- **HTML (`index.html`)**:
  - User-friendly form for inputting MBA graduate details, including fields for gender, SSC and HSC percentages and boards, degree percentage and field, work experience, employability test percentage, MBA specialization, and MBA percentage.
- **JavaScript (`script.js`)**:
  - Collects form data, converts it to JSON, and sends it to the backend using a POST request.
  - Receives the prediction result and updates the UI to display whether the MBA graduate is placed and the probability of placement.
- **CSS (`styles.css`)**:
  - Styles the form and the prediction result for better user experience.

## How to Run the Project

1. **Set up the environment**:
   - Ensure you have Python and Flask installed.
   - Install necessary libraries: `pandas`, `scikit-learn`, and `flask`.

2. **Prepare the Dataset**:
   - Place the `dataset.csv` file in the `files` folder.

3. **Run the Flask Application**:
   ```sh
   python project.py
  - This will start the Flask server on http://127.0.0.1:5000/.

3. Access the Web Application:
   - Open a web browser and navigate to http://127.0.0.1:5000/.
   - Fill out the form and click "Predict Placement" to see the result.
  
## Dataset
The dataset contains features related to MBA graduates' academic performance and personal details. These features include gender, SSC and HSC percentages and boards, degree percentage and field, work experience, employability test percentage, MBA specialization, and MBA percentage. The target variable is whether the graduate was placed or not.


## Model
The logistic regression model is trained to predict the likelihood of an MBA graduate getting placed based on the provided features. The model is trained on 80% of the dataset, with the remaining 20% used for testing.

## Conclusion
This project demonstrates how to build a full-stack machine learning web application, integrating a trained model with a user-friendly frontend interface. The application provides MBA graduates with insights into their placement probabilities.
