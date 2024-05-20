import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json

# Sample DataFrame
data = {
    "product": ["shirt", "cardigan", "chiffon shirt", "pants", "heels", "socks"],
    "sales": [5, 20, 36, 10, 10, 20]
}
df = pd.DataFrame(data)

def render_echarts(option: dict):
    option_json = json.dumps(option)

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
    components.html(html_template, width=700, height=500)

# Prepare ECharts options using DataFrame
option = {
    "title": {"text": "ECharts Sales Example"},
    "tooltip": {},
    "legend": {"data": ["Sales"]},
    "xAxis": {"data": df["product"].tolist()},
    "yAxis": {},
    "series": [{
        "name": "Sales",
        "type": "bar",
        "data": df["sales"].tolist()
    }]
}

# Call the function with the options
render_echarts(option)
