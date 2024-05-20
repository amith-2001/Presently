import streamlit as st
import streamlit.components.v1 as components
import json

def render_echarts(option: dict):
    # Convert the Python dictionary to JSON
    option_json = json.dumps(option)

    # HTML and JavaScript with ECharts setup
    html_template = f"""
    <html>
    <head>
         <script src="https://cdn.jsdelivr.net/npm/echarts@5.0.0/dist/echarts.min.js"></script>
    </head>
    <body style="height: 100%; margin: 0">
        <div id="main" style="height: 500px; width: 100%;"></div>
        <script type="text/javascript">
            var myChart = echarts.init(document.getElementById('main'));

            var option = {option_json};

            myChart.setOption(option);
        </script>
    </body>
    </html>
    """
    # Render the HTML in the Streamlit app
    components.html(html_template, width=700, height=500)

# Example ECharts options dictionary
option = {
    "title": {"text": "ECharts entry example"},
    "tooltip": {},
    "legend": {"data": ['Sales']},
    "xAxis": {"data": ["shirt", "cardigan", "chiffon shirt", "pants", "heels", "socks"]},
    "yAxis": {},
    "series": [{
        "name": 'Sales',
        "type": 'bar',
        "data": [5, 20, 36, 10, 10, 20]
    }]
}

# Call the function with the options
render_echarts(option)
