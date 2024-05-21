from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb+srv://maxwelljohn123123:nRJWqRQxvjH4bnYu@stremlit-snowflake-hack.ul6jfec.mongodb.net/?retryWrites=true&w=majority&appName=Stremlit-Snowflake-hackathon')  # Replace with your MongoDB URI if different

# Select the database and collection
db = client['Streamlit-Snowflake']
collection = db['presentation-data']

# Your JSON data
json_data = {
    "name": "Joe4rt6oe",
    "age": 33254,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postalCode": "12345"
    },
    "email": "johndoe@example.com"
}

def add_data(save_json) -> str:
# Insert the JSON data into the collection
    result = collection.insert_one(json_data)
    return result

if __name__ == '__main__': 
    print(f"Data inserted with id {add_data(json_data).inserted_id}")
