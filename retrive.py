import streamlit as st
import json
import base64
from PIL import Image
from io import BytesIO
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb+srv://maxwelljohn123123:nRJWqRQxvjH4bnYu@stremlit-snowflake-hack.ul6jfec.mongodb.net/?retryWrites=true&w=majority&appName=Stremlit-Snowflake-hackathon')
db = client['ga']
collection = db['ma']
slides_data = []

def retrieve_data_from_mongo(title):
    st.title(f"Data for Title: {title}")

    # Retrieve all slide data with the specified title from MongoDB
    slides_data_mongo = list(collection.find({},{"title": title}))
    for i in slides_data_mongo:
        slides_data.append(collection.find_one(i.get('id')))
    # slides_data = [for i in slides_data i.collection.find_one({i['id']})]
    # print(slides_data[0].get('Slide 2').keys())
    

    if not slides_data:
        st.write("No data found for the given title.")
        return

    for s in slides_data:
        slide_data = s.get('Slide 2')
        slide_title = slide_data.get('title', 'Untitled')
        st.header(slide_title)

        # Display left content
        left_content_type = slide_data.get('left_content_type', 'text')
        st.subheader("Left Content")
        if left_content_type == 'text':
            left_content = slide_data.get('left_content', '')
            st.write(left_content)
        elif left_content_type == 'image':
            left_image_base64 = slide_data.get('left_image_base64', '')
            if left_image_base64:
                left_image = base64.b64decode(left_image_base64)
                image = Image.open(BytesIO(left_image))
                st.image(image, caption='Left Image', use_column_width=True)

        # Display right content
        right_content_type = slide_data.get('right_content_type', 'text')
        st.subheader("Right Content")
        if right_content_type == 'text':
            right_content = slide_data.get('right_content', '')
            st.write(right_content)
        elif right_content_type == 'image':
            right_image_base64 = slide_data.get('right_image_base64', '')
            if right_image_base64:
                right_image = base64.b64decode(right_image_base64)
                image = Image.open(BytesIO(right_image))
                st.image(image, caption='Right Image', use_column_width=True)

        st.markdown("---")

# Main function to run Streamlit app
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "Retrieve Data"])

    if app_mode == "Home":
        st.title("Welcome to MongoDB Presentation App")
        st.write("Use the sidebar to navigate.")

        # Debugging: List all titles in the collection
        st.write("Existing titles in the collection:")
        titles = collection.distinct("title")
        st.write(titles)

    elif app_mode == "Retrieve Data":
        title = st.text_input("Enter Title to Retrieve Data")
        if st.button("Retrieve Data"):
            retrieve_data_from_mongo(title)

if __name__ == "__main__":
    main()
