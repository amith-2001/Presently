import streamlit as st
from PIL import Image
import base64
from io import BytesIO  # Add this import to handle the image file conversion to base64

title = ""
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

    # Sidebar inputs for title and color customization
    user_title = st.sidebar.text_input("Enter Title", "Default Title")
    color_input_title = st.sidebar.text_input("Enter Hex Color Code title ", "#FF6347")
    input_type = st.sidebar.radio("Choose Content Type:", ('Image', 'Text', 'Graph'))

    # Displaying the title in a custom color block
    st.markdown(f"""
    <div style='background-color: {color_input_title}; padding: 10px; color: white; text-align: center;'>
        <h1>{user_title}</h1>
    </div>
    """, unsafe_allow_html=True)

    # Handle content based on input type
    if input_type == 'Image':
        uploaded_file = st.sidebar.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
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

    elif input_type == 'Text':
        color_input = st.sidebar.text_input("Enter Hex Color Code Body", "#FF6347")
        user_text = st.sidebar.text_area("Enter Text", "Default Text")
        # Display the text in a colored block, using the user-specified hex color
        st.markdown(f"""
        <div style='background-color: {color_input}; padding: 10px; color: black; text-align: center;'>
            <p>{user_text}</p>
        </div>
        """, unsafe_allow_html=True)

    elif input_type == 'Graph':
        # st.set_page_config(layout="wide")
        # Placeholder text for graph functionality
        st.session_state['page'] = 'graph_page'
        st.experimental_rerun()


if __name__ == "__main__":
    render_template_1()
