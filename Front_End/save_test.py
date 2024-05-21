import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

def get_image_base64(image):
    if image is not None:
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return f"data:image/jpeg;base64,{img_str}"
    return None

def graph_plotter_with_chat(user_graph_text, data):
    # Saving the current graph state to session state
    st.session_state.graph_title = user_graph_text
    st.session_state.graph_data = data.to_json()  # Save data as JSON for simplicity

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
    # Interaction for changing the color, which could also be saved
    user_message = st.sidebar.text_input("Say something (e.g., 'Change color to red')...", key="chat")
    if user_message:
        if "change color to " in user_message.lower():
            new_color = user_message.lower().split("change color to ")[1].strip()
            st.session_state.graph_color = new_color
            st.sidebar.write(f"AI: Changing color to {new_color}")

def save_graph_state():
    if 'graph_title' in st.session_state:
        st.write("Graph Title:", st.session_state.graph_title)
    if 'graph_color' in st.session_state:
        st.write("Graph Color:", st.session_state.graph_color)
    if 'graph_data' in st.session_state:
        st.write("Graph Data (JSON):", st.session_state.graph_data)

def load_graph_state():
    if 'graph_title' in st.session_state:
        st.write("Saved Graph Title:", st.session_state.graph_title)
    if 'graph_color' in st.session_state:
        st.write("Saved Graph Color:", st.session_state.graph_color)
    if 'graph_data' in st.session_state:
        data = pd.read_json(st.session_state.graph_data)
        st.write("Saved Data:", data.head())

def main():
    # Assume this is part of your main app logic
    if st.button('Save Current Graph State'):
        save_graph_state()
    if st.button('Load Saved Graph State'):
        load_graph_state()

if __name__ == '__main__':
    st.title("Interactive Viz from your data!")
    main()
