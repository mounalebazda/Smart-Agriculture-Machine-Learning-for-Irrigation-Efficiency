import pymongo
import pandas as pd
import os

# MongoDB connection settings
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["agriculture_db"]  

# Function to insert data into MongoDB collection
def insert_data(collection_name, data):
    collection = db[collection_name]
    collection.insert_many(data)
    print(f"Inserted {len(data)} documents into '{collection_name}' collection")

def main():
    # File path
    file_path = os.path.join('data', 'Project_datasheet_2023-2024.csv')

    # Read CSV file into pandas DataFrame
    crop_data = pd.read_csv(file_path)

    # Convert DataFrame to list of dictionaries
    data_to_insert = crop_data.to_dict(orient='records')

    # Insert data into MongoDB collection
    collection_name = 'crop_data' 
    insert_data(collection_name, data_to_insert)

if __name__ == "__main__":
    main()
