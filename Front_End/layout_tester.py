import streamlit as st
import streamlit.components.v1
# ECharts JavaScript code embedded within HTML
echarts_html = """
<!DOCTYPE html>
<html style="width: 100%; height: 100%;">
<head>
    <meta charset="UTF-8">
</head>
<body style="width: 100%; height: 100%; margin: 0;">
    <div id="main" style="width: 100%; height: 100%;"></div>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"></script>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'), 'light');

        // Specify the configuration items and data for the chart
        var option = {
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: [820, 932, 901, 934, 1290, 1330, 1320],
                type: 'line'
            }]
        };

        // Use the specified configuration items and data to show the chart
        myChart.setOption(option);
    </script>
</body>
</html>
"""

# Use st.components to display the chart
st.components.v1.html(echarts_html, height=400)
