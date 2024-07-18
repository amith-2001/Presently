# Presently

Presently is a cutting-edge prototype designed to redefine the creation and delivery of presentations. It integrates Snowflake Arctic to recommend the most effective graphs based on uploaded data and OpenAI's GPT-4 to generate E-charts code for accurate and beautifully rendered visualizations. The frontend utilizes Streamlit for a user-friendly experience.

## Features

- **Data Upload**: Upload your data files easily.
- **Graph Recommendations**: Get recommendations for the most effective graphs based on your data using Snowflake Arctic.
- **E-charts Generation**: Automatically generate E-charts code with the help of OpenAI's GPT-4.
- **Interactive Frontend**: A user-friendly interface built with Streamlit.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/HarshithDR/Presently.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Presently
    ```

3. **Set up a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set up Snowflake Arctic**: Follow the [Snowflake Arctic documentation](https://docs.snowflake.com/arctic) to configure Snowflake Arctic and obtain necessary credentials.

2. **Set up OpenAI GPT-4**: Obtain an API key from [OpenAI](https://beta.openai.com/signup/) and configure it in your environment.

3. **Update configuration files**: Update the configuration files with your Snowflake Arctic and OpenAI credentials.

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Access the app**: Open your browser and go to `http://localhost:8501` to use the Presently application.

## Contributing

We welcome contributions to improve Presently. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


## Acknowledgements

- **Snowflake Arctic**: For providing effective graph recommendations.
- **OpenAI GPT-4**: For generating E-charts code.
- **Streamlit**: For the interactive frontend framework.

## Contact

For any questions or feedback, please reach out to [HarshithDR](harshithdr10@gmail.com).

