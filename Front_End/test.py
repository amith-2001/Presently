import streamlit as st
from PIL import Image
import base64
from io import BytesIO  # Add this import to handle the image file conversion to base64

# Function to create a base64 image URL from a PIL image object
def get_image_base64(image):
    if image is not None:
        # Convert RGBA to RGB
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        buffered = BytesIO()
        image.save(buffered, format="JPEG")  # You can also change this to PNG if you prefer
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/jpeg;base64,{img_str}"
    else:
        return None

def render_template_1():
    st.title("Dynamic Content Updater")

    # Sidebar inputs
    user_title = st.sidebar.text_input("Enter Title", "Default Title")
    uploaded_file = st.sidebar.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

    # Displaying the title in a color block
    st.markdown(f"""
    <div style='background-color: #FF6347; padding: 10px; color: white; text-align: center;'>
        <h1>{user_title}</h1>
    </div>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:
        # Convert the file to an image
        image = Image.open(uploaded_file)
        img_base64 = get_image_base64(image)

        # Display the image using HTML
        st.markdown(f"""
        <img src="{img_base64}" alt="Uploaded Image" style="width:100%">
        """, unsafe_allow_html=True)
    else:
        # Placeholder for no image
        st.markdown("""
        <div style='background-color: #808080; height: 300px; display: flex; justify-content: center; align-items: center; color: white;'>
            <h4>No Image Uploaded</h4>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_template_1()
