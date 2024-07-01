import pymongo

# MongoDB connection settings
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["agriculture_db"]  # Replace with your database name


def query_all_documents(collection_name):
    """
    Query all documents from a MongoDB collection.
    """
    collection = db[collection_name]
    print(f"Collection name: {collection_name}")  # Debug statement
    try:
        documents = collection.find()
        return list(documents)
    except pymongo.errors.PyMongoError as e:
        print(f"Error querying documents: {e}")
        return []


def query_temperature_above(collection_name, threshold):
    """
    Query documents where temperature is above a specified threshold.
    """
    collection = db[collection_name]
    print(f"Querying documents with temperature > {threshold}°C...")  # Debug statement
    try:
        query = {"Temperature": {"$gt": threshold}}
        documents = collection.find(query)
        return list(documents)
    except pymongo.errors.PyMongoError as e:
        print(f"Error querying temperature above {threshold}°C: {e}")
        return []


def update_humidity(collection_name, condition, new_value):
    """
    Update humidity field in documents matching a condition.
    """
    collection = db[collection_name]
    query = condition
    update = {"$set": {"humidity": new_value}}
    try:
        result = collection.update_many(query, update)
        return result.modified_count
    except pymongo.errors.PyMongoError as e:
        print(f"Error updating humidity: {e}")
        return 0


def delete_documents_below_rainfall(collection_name, threshold):
    """
    Delete documents where rainfall is below a specified threshold.
    """
    collection = db[collection_name]
    query = {"rainfall": {"$lt": threshold}}
    try:
        result = collection.delete_many(query)
        return result.deleted_count
    except pymongo.errors.PyMongoError as e:
        print(f"Error deleting documents below {threshold}: {e}")
        return 0


def print_menu():
    """
    Print the menu options.
    """
    print("\nMenu:")
    print("1. Query all documents")
    print("2. Query documents with temperature above a threshold")
    print("3. Update humidity in documents where temperature is above a threshold")
    print("4. Delete documents where rainfall is below a threshold")
    print("5. Exit")


if __name__ == "__main__":
    try:
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                # Example 1: Query all documents
                all_documents = query_all_documents('crop_data')
                print(f"\nNumber of documents retrieved: {len(all_documents)}")  # Debug statement
                print("\nAll documents:")
                for doc in all_documents:
                    print(doc)

            elif choice == "2":
                # Example 2: Query documents with temperature above a threshold
                try:
                    threshold = int(input("Enter the temperature threshold: "))
                    temp_above_threshold = query_temperature_above('crop_data', threshold)
                    print(f"\nDocuments with temperature > {threshold}°C:")
                    if not temp_above_threshold:
                        print("No documents found.")
                    else:
                        for doc in temp_above_threshold:
                            print(doc)
                except ValueError:
                    print("Invalid temperature threshold. Please enter a valid number.")

            elif choice == "3":
                # Example 3: Update humidity in documents where temperature is above a threshold
                try:
                    threshold = float(input("Enter the temperature threshold: "))
                    new_humidity_value = float(input("Enter the new humidity value: "))
                    condition = {"temperature": {"$gt": threshold}}
                    updated_count = update_humidity('crop_data', condition, new_humidity_value)
                    print(f"\nUpdated {updated_count} documents.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for temperature threshold and humidity.")

            elif choice == "4":
                # Example 4: Delete documents where rainfall is below a threshold
                try:
                    threshold = float(input("Enter the rainfall threshold: "))
                    deleted_count = delete_documents_below_rainfall('crop_data', threshold)
                    print(f"\nDeleted {deleted_count} documents.")
                except ValueError:
                    print("Invalid rainfall threshold. Please enter a valid number.")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()
