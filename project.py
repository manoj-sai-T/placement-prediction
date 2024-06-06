import pandas as pd
from flask import Flask, request, jsonify
from flask import Flask, render_template
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings('ignore')

# Load the data
data = pd.read_csv('files/dataset.csv')

# Drop unnecessary columns
data = data.drop(['sl_no', 'salary'], axis=1)

# Map categorical variables to numerical values
data['ssc_b'] = data['ssc_b'].map({'Central': 1, 'Others': 0})
data['hsc_b'] = data['hsc_b'].map({'Central': 1, 'Others': 0})
data['gender'] = data['gender'].map({'M': 0, 'F': 1})
data['hsc_s'] = data['hsc_s'].map({'Science': 2, 'Commerce': 1, 'Arts': 0})
data['degree_t'] = data['degree_t'].map({'Sci&Tech': 2, 'Comm&Mgmt': 1, 'Others': 0})
data['specialisation'] = data['specialisation'].map({'Mkt&HR': 1, 'Mkt&Fin': 0})
data['workex'] = data['workex'].map({'Yes': 1, 'No': 0})
data['status'] = data['status'].map({'Placed': 1, 'Not Placed': 0})

# Split data into features and target
X = data.drop('status', axis=1)
y = data['status']

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize Flask app
app = Flask(__name__)

# Route for serving the HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Load the trained model
lr = LogisticRegression()
lr.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json
    
    # Convert data to DataFrame
    new_data = pd.DataFrame(data, index=[0])
    
    # Make prediction
    prediction = lr.predict(new_data)
    probability = lr.predict_proba(new_data)[0][1]
    
    # Prepare response
    response = {'placed': bool(prediction), 'probability': probability}
    
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
