from pymongo import MongoClient
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['agriculture_db']  
collection_name = 'crop_data'  

# Function to extract data from MongoDB
def extract_data_for_ml(collection_name):
    collection = db[collection_name]
    cursor = collection.find({}, {'_id': 0, 'CropType': 1, 'CropDays': 1,
                                  'Soil Moisture': 1, 'Soil Temperature': 1,
                                  'Temperature': 1, 'Humidity': 1, 'Irrigation(Y/N)': 1})

    X = []
    y = []

    for doc in cursor:
        features = [
            doc['CropType'], 
            doc['CropDays'], 
            doc['Soil Moisture'], 
            doc['Soil Temperature'], 
            doc['Temperature'], 
            doc['Humidity']
        ]
        target = doc['Irrigation(Y/N)']

        X.append(features)
        y.append(target)

    return X, y

# Split data into training and evaluation sets
def split_data(X, y):
    X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_eval, y_train, y_eval


# Train and evaluate machine learning model
def train_and_evaluate_model(X_train, X_eval, y_train, y_eval):
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_eval)
    accuracy = accuracy_score(y_eval, y_pred)
    print(f"Accuracy of the model: {accuracy}")
    return model  # Return the trained model object

# Function to predict using trained model
def predict_with_model(model, input_features):
    # Convert input features to numpy array
    input_features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_features)[0]
    if prediction == 1:
        return "Irrigation is needed."
    else:
        return "No irrigation is needed."

# Main function to orchestrate the workflow
def main():
    # Extract data from MongoDB
    X, y = extract_data_for_ml(collection_name)

    # Split data into training and evaluation sets
    X_train, X_eval, y_train, y_eval = split_data(X, y)

    # Train and evaluate machine learning model
    trained_model = train_and_evaluate_model(X_train, X_eval, y_train, y_eval)

    # Example of making predictions
    print("\nExample predictions:")
    example_input = [2, 93, 425, 20, 23, 58]  
    prediction = predict_with_model(trained_model, example_input)
    print("Input:", example_input)
    print("Prediction:", prediction)

    # Interactive prediction loop
    while True:
        print("\nEnter new data to predict (enter 'exit' to quit):")
        try:
            crop_type = input("Crop Type: ")
            if crop_type.lower() == 'exit':
                break
            crop_type = int(crop_type)  # Convert to integer
            crop_days = int(input("Crop Days: "))
            soil_moisture = int(input("Soil Moisture: "))
            soil_temperature = int(input("Soil Temperature: "))
            temperature = int(input("Temperature: "))
            humidity = int(input("Humidity: "))

            input_data = [crop_type, crop_days, soil_moisture, soil_temperature, temperature, humidity]
            prediction = predict_with_model(trained_model, input_data)
            print("Prediction:", prediction)

        except ValueError:
            user_input = input("Invalid input. Enter 'exit' to quit or press any key to continue: ")
            if user_input.lower() == 'exit':
                break

# Entry point of the script
if __name__ == "__main__":
    main()
