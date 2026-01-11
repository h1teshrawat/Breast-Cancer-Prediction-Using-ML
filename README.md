# Breast Cancer Prediction Using Machine Learning

This project is a web-based application that predicts whether breast cancer is cancerous or not based on input features using a machine learning model. It uses a Logistic Regression model trained on the Breast Cancer Wisconsin (Diagnostic) dataset.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)

## Features
- Predict breast cancer diagnosis (Cancerous or Not Cancerous) based on 31 numerical features.
- Web interface built with Flask and Bootstrap for easy interaction.
- Displays prediction results with visual cards and images.
- Error handling for invalid inputs.

## Requirements
### Software
- Python 3.8 or higher
- A web browser (e.g., Chrome, Firefox) to access the web app

### Libraries
The project uses the following Python libraries (automatically installed via pip):
- `flask` - For building the web application
- `numpy` - For numerical computations
- `pandas` - For data manipulation (used in training, not in the app)
- `scikit-learn` - For machine learning model and preprocessing

## Installation
1. **Clone or Download the Repository**:
   - Download the project folder to your local machine.

2. **Set Up a Virtual Environment** (Recommended):
   - Open a terminal/command prompt in the project directory.
   - Create a virtual environment:
     ```
     python -m venv .venv
     ```
   - Activate it:
     - On Windows: `.venv\Scripts\activate`
     - On macOS/Linux: `source .venv/bin/activate`

3. **Install Dependencies**:
   - Run:
     ```
     pip install flask numpy pandas scikit-learn
     ```
   - This installs all required libraries.

4. **Prepare Files**:
   - Ensure `model/model.pkl` (trained model) and `model/scaler.pkl` (data scaler) are in the `model/` folder.
   - Place images (`img.jpg`, `okay.jpg`, `alert.jpg`) in the `static/` folder for the web interface.

## Usage
1. **Run the Application**:
   - In the terminal (with virtual environment activated), navigate to the project root and run:
     ```
     python app.py
     ```
   - The app will start on `http://127.0.0.1:5000/`.

2. **Access the Web App**:
   - Open a web browser and go to `http://127.0.0.1:5000/`.
   - Enter 31 comma-separated numerical features (e.g., from the dataset) in the input field.
   - Click "Predict" to get the result.

3. **Example Input**:
   - Use this sample input (from the dataset, predicts "Not Cancerous"):
     ```
     -0.23711093,-0.4976419,0.61365274,-0.49813131,-0.53102815,-0.57694824,-0.17494424,-0.36215622,-0.284859,0.43345165,0.17818232,-0.36844966,0.55310406,-0.31671104,-0.40524636,0.04025752,-0.03795529,-0.18043065,0.16478901,-0.12170969,0.23079329,-0.50044002,0.81940367,-0.46922838,-0.53308833,-0.04910117,-0.04160193,-0.14913653,0.09681787,0.10617647,0.49035329
     ```

4. **Stop the App**:
   - Press `Ctrl+C` in the terminal.

## How It Works
### Overall Workflow
1. **Data Collection**: The model is trained on the Breast Cancer Wisconsin dataset.
2. **Preprocessing**: Features are scaled using StandardScaler.
3. **Model Training**: Logistic Regression predicts cancer diagnosis.
4. **Web App**: Users input features via a form; the app processes them and displays the prediction.

### Code Breakdown
- **`Breast_Cancer_predictiob.ipynb`** (Jupyter Notebook):
  - Loads and explores the dataset (`data.csv`).
  - Preprocesses data (removes unnecessary columns, encodes labels, scales features).
  - Trains a Logistic Regression model.
  - Saves the model (`model.pkl`) and scaler (`scaler.pkl`).
  - Includes a test prediction example.

- **`app.py`** (Flask Application):
  - Loads the trained model and scaler.
  - Defines routes: `/` for the home page, `/predict` for handling form submissions.
  - In `/predict`:
    - Parses input (comma-separated string to array).
    - Scales the input using the loaded scaler.
    - Makes a prediction (0 = Not Cancerous, 1 = Cancerous).
    - Renders the result on the page with error handling.

- **`templates/index.html`** (HTML Template):
  - Displays the web interface with a form for input.
  - Shows prediction results in cards with images.
  - Uses Jinja2 templating for dynamic content.

- **`static/` Folder**:
  - Contains images used in the web app (e.g., `img.jpg` for the header, `okay.jpg` for non-cancerous, `alert.jpg` for cancerous).

### Key Concepts
- **Machine Learning**: Supervised learning with Logistic Regression for binary classification.
- **Web Development**: Flask handles backend logic; HTML/CSS (via Bootstrap) for frontend.
- **Data Scaling**: Ensures features are on the same scale for accurate predictions.

## Dataset
- **Source**: Breast Cancer Wisconsin (Diagnostic) Dataset from UCI Machine Learning Repository.
- **Description**: Contains 569 samples with 31 features (e.g., radius, texture, area) and a diagnosis label (M = Malignant/Cancerous, B = Benign/Not Cancerous).
- **File**: `breast cancer report and dataset/data.csv`

## Model Training
- **Algorithm**: Logistic Regression (simple, interpretable for binary classification).
- **Accuracy**: ~95% on test data (based on the notebook).
- **Preprocessing**: Standard scaling to normalize features.
- **Files**: Model and scaler are saved as pickle files for the web app.

## Web Application
- **Framework**: Flask (lightweight Python web framework).
- **Frontend**: Bootstrap for responsive design.
- **Functionality**: Single-page app with form input and result display.

## Contributing
- Fork the repository.
- Make changes and test thoroughly.
- Submit a pull request with a description of your changes.

## License
This project is for educational purposes. Feel free to use and modify it.

For questions or issues, check the code comments or reach out!