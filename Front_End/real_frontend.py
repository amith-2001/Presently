import streamlit as st
import json
from typing_live import live_typing_effect
from streamlit_lottie import st_lottie
import os
# from test import get_image_base64 , render_template_1
from PIL import Image
import base64
from io import BytesIO
import pandas as pd
import streamlit.components.v1


# CSS to hide scrollbars in Chrome and other browsers


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


# def graph_plotter_with_chat(user_graph_text):
#     echarts_html = f"""
#     <div id="main" style="width: 600px;height:400px;"></div>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.0/echarts.min.js"></script>
#     <script>
#         var myChart = echarts.init(document.getElementById('main'));
#         var option = {{
#             title: {{
#                 text: '{user_graph_text}',
#                 left: 'center'
#             }},
#             tooltip: {{}},
#             legend: {{
#                 data:['Sales']
#             }},
#             xAxis: {{
#                 data: ["shirt","cardigan","chiffon shirt","pants","heels","socks"]
#             }},
#             yAxis: {{}},
#             series: [{{
#                 name: 'Sales',
#                 type: 'bar',
#                 data: [5, 20, 36, 10, 10, 20]
#             }}]
#         }};
#         myChart.setOption(option);
#     </script>
#     """
#     st.components.v1.html(echarts_html, height=400)
#
#     # Sidebar Chat interface
#     user_message = st.sidebar.text_input("Say something...", key="chat")
#     if user_message:
#         st.sidebar.write("AI: Hi")
def graph_plotter_with_chat(user_graph_text):
    # Check if a color has been set in the session state
    if 'color' not in st.session_state:
        st.session_state.color = 'blue'  # Default color

    # Generate the HTML for the ECharts graph
    echarts_html = f"""
    <div id="main" style="width: 600px;height:400px;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.0/echarts.min.js"></script>
    <script>
        var myChart = echarts.init(document.getElementById('main'));
        var option = {{
            title: {{
                text: '{user_graph_text}',
                left: 'center'
            }},
            tooltip: {{}},
            legend: {{
                data:['Sales']
            }},
            xAxis: {{
                data: ["shirt","cardigan","chiffon shirt","pants","heels","socks"]
            }},
            yAxis: {{}},
            series: [{{
                name: 'Sales',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20],
                itemStyle: {{
                    color: '{st.session_state.color}'
                }}
            }}]
        }};
        myChart.setOption(option);
    </script>
    """
    st.components.v1.html(echarts_html, height=400)

    # Sidebar Chat interface for color input
    user_message = st.sidebar.text_input("Say something (e.g., 'Change color to red')...", key="chat")
    if user_message:
        # Simple check for a color change command
        if "change color to " in user_message.lower():
            new_color = user_message.lower().split("change color to ")[1].strip()
            st.session_state.color = new_color  # Update the color in session state
            st.sidebar.write(f"AI: Changing color to {new_color}")

        else:
            st.sidebar.write("AI: Hi, you can ask me to change the graph color by saying 'Change color to [color]'")


def arctic_recommender():
    st.sidebar.text_area("Recommended Graphs by Snowflake Arctic",
                         """Bar Chart""",
                         height=5)


def render_template_1():
    # st.title("Dynamic Content Updater")

    # Sidebar inputs for title and color customization
    # Use session state to store and retrieve user inputs
    st.sidebar.write("Reference agraphs : https://echarts.apache.org/examples/en/index.html")
    user_title = st.sidebar.text_input("Enter Title", st.session_state.get('user_title', "Default Title"))
    color_input_title = st.sidebar.text_input("Enter Hex Color Code title",
                                              st.session_state.get('color_input_title', "#FF6347"))
    input_type = st.sidebar.radio("Choose Content Type:", ('Image', 'Text', 'Graph'))

    # Save inputs to session state to persist data across reruns
    st.session_state['user_title'] = user_title
    st.session_state['color_input_title'] = color_input_title
    st.session_state['input_type'] = input_type

    # Displaying the title in a custom color block
    st.markdown(f"""
    <div style='background-color: {color_input_title}; padding: 10px; color: white; text-align: center;'>
        <h1>{user_title}</h1>
    </div>
    """, unsafe_allow_html=True)

    if input_type == 'Image':
        handle_image_upload()

    elif input_type == 'Text':
        handle_text_content()

    elif input_type == 'Graph':
        # user_graph_text = st.sidebar.text_input("Enter Graph Title", "Default Graph Title")
        user_graph_text = ""
        if data_upload():
            arctic_recommender()
            graph_plotter_with_chat(user_graph_text)
            if st.button("Home"):
                st.session_state['page'] = 'home'




def handle_image_upload():
    uploaded_file = st.sidebar.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_base64 = get_image_base64(image)
        st.markdown(f"<img src='{img_base64}' alt='Uploaded Image' style='width:100%'>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<div style='background-color: #808080; height: 300px; display: flex; justify-content: center; align-items: center; color: white;'><h4>No Image Uploaded</h4></div>",
            unsafe_allow_html=True)


def handle_text_content():
    color_input = st.sidebar.text_input("Enter Hex Color Code Body",
                                        st.session_state.get('color_input_body', "#FF6347"))
    user_text = st.sidebar.text_area("Enter Text", st.session_state.get('user_text', "Default Text"))
    st.session_state['color_input_body'] = color_input
    st.session_state['user_text'] = user_text
    st.markdown(
        f"<div style='background-color: {color_input}; padding: 10px; color: black; text-align: center;'><p>{user_text}</p></div>",
        unsafe_allow_html=True)


def graph_plotter_1(user_graph_text):
    pass


# hide_scrollbars = """
# <style>
# /* Hide scrollbar for Chrome, Safari and Opera */
# body, .element-container, .stBlock, .stMarkdown, .stDataFrame, .main, .block-container {
#     ::-webkit-scrollbar {
#         display: none;
#     }
# }
#
# /* Hide scrollbar for IE, Edge and Firefox */
# body, .element-container, .stBlock, .stMarkdown, .stDataFrame, .main, .block-container {
#     -ms-overflow-style: none;  /* IE and Edge */
#     scrollbar-width: none;  /* Firefox */
#     overflow: hidden; /* Generally hide overflow */
# }
# </style>
# """
#
# st.markdown(hide_scrollbars, unsafe_allow_html=True)


def load_lottiefile(filepath: str):
    """ Load a Lottie animation from a JSON file located at filepath """
    with open(filepath, 'r') as file:
        return json.load(file)


def load_existing_project():
    x = st.text_input("Enter project Title")
    if x == "my project":
        echarts_html = f"""
        <div id="main" style="width: 600px;height:400px;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.0/echarts.min.js"></script>
        <script>
            var myChart = echarts.init(document.getElementById('main'));
            var option = {{
                title: {{
                    text: '{''}',
                    left: 'center'
                }},
                tooltip: {{}},
                legend: {{
                    data:['Sales']
                }},
                xAxis: {{
                    data: ["shirt","cardigan","chiffon shirt","pants","heels","socks"]
                }},
                yAxis: {{}},
                series: [{{
                    name: 'Sales',
                    type: 'bar',
                    data: [5, 20, 36, 10, 10, 20],
                    itemStyle: {{
                        color: '{st.session_state.color}'
                    }}
                }}]
            }};
            myChart.setOption(option);
        </script>
        """
        st.components.v1.html(echarts_html, height=400)



    if st.button("Back"):
        st.session_state['page'] = 'home'  # Set the session state to redirect to the home page
        st.experimental_rerun()  # Rerun the app to reflect the change


def experimental_graph():
    pass


def template_selection():
    st.title("Choose Your PowerPoint Template")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Template 1")
        template1_path = "template1.png"
        if os.path.exists(template1_path):
            st.image(template1_path, caption="Template 1 Example")
        else:
            st.error("Error: Template 1 image not found!")
        if st.button("Choose Template 1", key="btn1"):
            st.session_state.current_page = 'selected_template1'
            st.success("You have selected Template 1!")
            st.session_state['page'] = 'template_1'
            st.experimental_rerun()

    with col2:
        st.header("Template 2")
        template2_path = "template2.png"
        if os.path.exists(template2_path):
            st.image(template2_path, caption="Template 2 Example")
        else:
            st.error("Error: Template 2 image not found!")
        if st.button("Choose Template 2", key="btn2"):
            st.session_state.current_page = 'selected_template2'
            st.success("You have selected Template 2!")
            st.experimental_rerun()
    print('tempelate pafe')
    pass



def data_upload():
    # Create a sidebar for CSV file upload
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # Optionally process data or prepare it for plotting here

        # Store the data in session state or mark that the graph is ready to be plotted
        st.session_state['graph_data'] = data  # You could store actual data or just a flag
        return True


if __name__ == '__main__':
    # Initialize the session state for page navigation if not already set
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == "temp_page":
        template_selection()

    if st.session_state['page'] == "load_existing":
        # st.set_page_config(layout="wide")
        load_existing_project()
        pass

    if st.session_state['page'] == "template_1":
        # st.set_page_config(layout="wide")
        render_template_1()
        pass



    if st.session_state['page'] == 'home':
        st.title(
            "Welcome! Let's generate Interactive Viz from your data! 🚀")
        lottie_animation_path = "/Animation - 1716175109588.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=250, width=600, key="example")
        live_typing_effect(
            "Hello, I'm your AI Flowchart Generator! 🚀 Just send over your code or GitHub repository, and I'll transform it into a sleek, easy-to-understand flow diagram. Let's streamline your work and make your projects visually engaging!",
            speed=25)
        col1, col2 = st.columns(2)

        with col1:
            if st.button('Load existing Project'):
                st.session_state['page'] = 'load_existing'
                st.experimental_rerun()

        with col2:
            if st.button('Create New Project'):
                st.session_state['page'] = 'temp_page'
                st.experimental_rerun()

