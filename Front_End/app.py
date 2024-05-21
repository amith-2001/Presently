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

# def render_template_1():
#     st.title("Dynamic Content Updater")
#
#     # Sidebar inputs for title and color customization
#     user_title = st.sidebar.text_input("Enter Title", "Default Title")
#     color_input_title = st.sidebar.text_input("Enter Hex Color Code title ", "#FF6347")
#     input_type = st.sidebar.radio("Choose Content Type:", ('Image', 'Text', 'Graph'))
#
#     # Displaying the title in a custom color block
#     st.markdown(f"""
#     <div style='background-color: {color_input_title}; padding: 10px; color: white; text-align: center;'>
#         <h1>{user_title}</h1>
#     </div>
#     """, unsafe_allow_html=True)
#
#     # Handle content based on input type
#     if input_type == 'Image':
#         uploaded_file = st.sidebar.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
#         if uploaded_file is not None:
#             # Convert the file to an image
#             image = Image.open(uploaded_file)
#             img_base64 = get_image_base64(image)
#
#             # Display the image using HTML
#             st.markdown(f"""
#             <img src="{img_base64}" alt="Uploaded Image" style="width:100%">
#             """, unsafe_allow_html=True)
#         else:
#             # Placeholder for no image
#             st.markdown("""
#             <div style='background-color: #808080; height: 300px; display: flex; justify-content: center; align-items: center; color: white;'>
#                 <h4>No Image Uploaded</h4>
#             </div>
#             """, unsafe_allow_html=True)
#
#     elif input_type == 'Text':
#         color_input = st.sidebar.text_input("Enter Hex Color Code Body", "#FF6347")
#         user_text = st.sidebar.text_area("Enter Text", "Default Text")
#         # Display the text in a colored block, using the user-specified hex color
#         st.markdown(f"""
#         <div style='background-color: {color_input}; padding: 10px; color: black; text-align: center;'>
#             <p>{user_text}</p>
#         </div>
#         """, unsafe_allow_html=True)
#
#     elif input_type == 'Graph':
#         # st.set_page_config(layout="wide")
#         # Placeholder text for graph functionality
#         st.session_state['page'] = 'graph_page'
#         st.experimental_rerun()
def graph_plotter_with_chat(user_graph_text):
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
                data: [5, 20, 36, 10, 10, 20]
            }}]
        }};
        myChart.setOption(option);
    </script>
    """
    st.components.v1.html(echarts_html, height=400)

    # Sidebar Chat interface
    user_message = st.sidebar.text_input("Say something...", key="chat")
    if user_message:
        st.sidebar.write("AI: Hi")

def render_template_1():
    # st.title("Dynamic Content Updater")

    # Sidebar inputs for title and color customization
    # Use session state to store and retrieve user inputs
    user_title = st.sidebar.text_input("Enter Title", st.session_state.get('user_title', "Default Title"))
    color_input_title = st.sidebar.text_input("Enter Hex Color Code title", st.session_state.get('color_input_title', "#FF6347"))
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
        user_graph_text = st.sidebar.text_input("Enter Graph Title", "Default Graph Title")
        graph_plotter_with_chat(user_graph_text)

    if 'graph_ready' in st.session_state and st.session_state['graph_ready']:
        # Call the graph plotting function or embed the graph directly
        st.write("Displaying graph based on the latest data:")
        grapg_plotter()  # This function should handle plotting based on session state data
def handle_image_upload():
    uploaded_file = st.sidebar.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_base64 = get_image_base64(image)
        st.markdown(f"<img src='{img_base64}' alt='Uploaded Image' style='width:100%'>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background-color: #808080; height: 300px; display: flex; justify-content: center; align-items: center; color: white;'><h4>No Image Uploaded</h4></div>", unsafe_allow_html=True)

def handle_text_content():
    color_input = st.sidebar.text_input("Enter Hex Color Code Body", st.session_state.get('color_input_body', "#FF6347"))
    user_text = st.sidebar.text_area("Enter Text", st.session_state.get('user_text', "Default Text"))
    st.session_state['color_input_body'] = color_input
    st.session_state['user_text'] = user_text
    st.markdown(f"<div style='background-color: {color_input}; padding: 10px; color: black; text-align: center;'><p>{user_text}</p></div>", unsafe_allow_html=True)


def graph_plotter_1(user_graph_text):
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
                data: [5, 20, 36, 10, 10, 20]
            }}]
        }};
        myChart.setOption(option);
    </script>
    """
    st.components.v1.html(echarts_html, height=400)




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
    st.text_input("Enter project ID")
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



def grapg_plotter():
    echarts_html = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ECharts Example</title>
    <!-- Import ECharts library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.0/echarts.min.js"></script>
</head>
<body>
    <!-- Container for your chart -->
    <div id="main" style="width: 600px; height: 400px;"></div>

    <script>
        // Your ECharts configuration
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom);
        var option;

        const data = [
          [
            [28604, 77, 17096869, 'Australia', 1990],
            [31163, 77.4, 27662440, 'Canada', 1990],
            [1516, 68, 1154605773, 'China', 1990],
            [13670, 74.7, 10582082, 'Cuba', 1990],
            [28599, 75, 4986705, 'Finland', 1990],
            [29476, 77.1, 56943299, 'France', 1990],
            [31476, 75.4, 78958237, 'Germany', 1990],
            [28666, 78.1, 254830, 'Iceland', 1990],
            [1777, 57.7, 870601776, 'India', 1990],
            [29550, 79.1, 122249285, 'Japan', 1990],
            [2076, 67.9, 20194354, 'North Korea', 1990],
            [12087, 72, 42972254, 'South Korea', 1990],
            [24021, 75.4, 3397534, 'New Zealand', 1990],
            [43296, 76.8, 4240375, 'Norway', 1990],
            [10088, 70.8, 38195258, 'Poland', 1990],
            [19349, 69.6, 147568552, 'Russia', 1990],
            [10670, 67.3, 53994605, 'Turkey', 1990],
            [26424, 75.7, 57110117, 'United Kingdom', 1990],
            [37062, 75.4, 252847810, 'United States', 1990]
          ],
          [
            [44056, 81.8, 23968973, 'Australia', 2015],
            [43294, 81.7, 35939927, 'Canada', 2015],
            [13334, 76.9, 1376048943, 'China', 2015],
            [21291, 78.5, 11389562, 'Cuba', 2015],
            [38923, 80.8, 5503457, 'Finland', 2015],
            [37599, 81.9, 64395345, 'France', 2015],
            [44053, 81.1, 80688545, 'Germany', 2015],
            [42182, 82.8, 329425, 'Iceland', 2015],
            [5903, 66.8, 1311050527, 'India', 2015],
            [36162, 83.5, 126573481, 'Japan', 2015],
            [1390, 71.4, 25155317, 'North Korea', 2015],
            [34644, 80.7, 50293439, 'South Korea', 2015],
            [34186, 80.6, 4528526, 'New Zealand', 2015],
            [64304, 81.6, 5210967, 'Norway', 2015],
            [24787, 77.3, 38611794, 'Poland', 2015],
            [23038, 73.13, 143456918, 'Russia', 2015],
            [19360, 76.5, 78665830, 'Turkey', 2015],
            [38225, 81.4, 64715810, 'United Kingdom', 2015],
            [53354, 79.1, 321773631, 'United States', 2015]
          ]
        ];

        option = {
          backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [
            {
              offset: 0,
              color: '#0000'
            },
            {
              offset: 1,
              color: '#0000'
            }
          ]),
          title: {
            text: 'Life Expectancy and GDP by Country',
            left: '5%',
            top: '3%'
          },
          legend: {
            right: '10%',
            top: '3%',
            data: ['1990', '2015']
          },
          grid: {
            left: '8%',
            top: '10%'
          },
          xAxis: {
            splitLine: {
              lineStyle: {
                type: 'dashed'
              }
            }
          },
          yAxis: {
            splitLine: {
              lineStyle: {
                type: 'dashed'
              }
            },
            scale: true
          },
          series: [
            {
              name: '1990',
              data: data[0],
              type: 'scatter',
              symbolSize: function (data) {
                return Math.sqrt(data[2]) / 5e2;
              },
              emphasis: {
                focus: 'series',
                label: {
                  show: true,
                  formatter: function (param) {
                    return param.data[3];
                  },
                  position: 'top'
                }
              },
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(120, 36, 50, 0.5)',
                shadowOffsetY: 5,
                color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
                  {
                    offset: 0,
                    color: 'rgb(251, 118, 123)'
                  },
                  {
                    offset: 1,
                    color: 'rgb(204, 46, 72)'
                  }
                ])
              }
            },
            {
              name: '2015',
              data: data[1],
              type: 'scatter',
              symbolSize: function (data) {
                return Math.sqrt(data[2]) / 5e2;
              },
              emphasis: {
                focus: 'series',
                label: {
                  show: true,
                  formatter: function (param) {
                    return param.data[3];
                  },
                  position: 'top'
                }
              },
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(25, 100, 150, 0.5)',
                shadowOffsetY: 5,
                color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
                  {
                    offset: 0,
                    color: 'rgb(129, 227, 238)'
                  },
                  {
                    offset: 1,
                    color: 'rgb(25, 183, 207)'
                  }
                ])
              }
            }
          ]
        };

        option && myChart.setOption(option);
    </script>
</body>
</html>
    """
    # Use st.components to display the chart
    st.components.v1.html(echarts_html, height=400)


def graph_page():
    # Create a sidebar for CSV file upload
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        # Optionally process data or prepare it for plotting here

        # Store the data in session state or mark that the graph is ready to be plotted
        st.session_state['graph_data'] = data  # You could store actual data or just a flag

    if st.button("Apply Changes"):
        st.session_state['graph_ready'] = True
        st.session_state['page'] = 'template_1'  # Navigate back to template_1 page
        st.experimental_rerun()

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


    if st.session_state.page == "graph_page":
        # st.set_page_config(layout="wide")
        st.write('this is graph page')
        graph_page()
        if st.button("back"):

            st.session_state['page'] = 'template_1'
        pass

    if st.session_state['page'] == 'home':
        st.title(
            "Welcome! Let's generate Interactive Viz from your data! 🚀")
        lottie_animation_path = "Animation - 1716175109588.json"
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, height=250, width=600, key="example")
        live_typing_effect("Hello, I'm your AI Flowchart Generator! 🚀 Just send over your code or GitHub repository, and I'll transform it into a sleek, easy-to-understand flow diagram. Let's streamline your work and make your projects visually engaging!", speed=25)
        col1, col2 = st.columns(2)

        with col1:
            if st.button('Load existing Project'):
                st.session_state['page'] = 'load_existing'
                st.experimental_rerun()

        with col2:
            if st.button('Create New Project'):
                st.session_state['page'] = 'temp_page'
                st.experimental_rerun()

