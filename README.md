# 🏥 AI Medical Report System

An AI-powered medical image analysis and report generation system designed to assist in analyzing medical scans such as MRI, CT, and ultrasound images.

## 📌 Project Overview

The **AI Medical Report System** uses deep learning and image processing techniques to analyze medical images and generate automated medical reports. The system provides a simple web-based interface where users can upload medical scan images, view AI-generated predictions, access previous analysis history, and download reports.

## ✨ Key Features

- **MRI Image Analysis:** AI-based analysis of MRI scan images.
- **CT Scan Analysis:** Deep learning-based CT image classification.
- **Ultrasound Analysis:** AI-assisted ultrasound image analysis.
- **Automated Report Generation:** Generates downloadable medical reports in DOCX format.
- **Prediction Results:** Displays analysis results through a web interface.
- **History Management:** Stores and displays previous analysis records.
- **Dashboard:** Provides an overview of system activities.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask |
| Deep Learning | TensorFlow, Keras |
| Image Processing | OpenCV |
| Data Processing | NumPy, Pandas |
| Machine Learning | Scikit-learn |
| Report Generation | python-docx |
| Deployment | Render |
| Version Control | Git, GitHub |

## 🏗️ System Architecture

1. **Image Upload:** The user uploads an MRI, CT, or ultrasound image.
2. **Image Preprocessing:** OpenCV and NumPy are used for image preprocessing.
3. **AI Model Prediction:** The trained deep learning models analyze the uploaded image.
4. **Result Display:** The prediction result is displayed on the web application.
5. **Report Generation:** A medical report is generated for download.
6. **History Tracking:** Previous analysis records can be viewed through the history section.

## 📂 Project Structure

```text
AI-MEDICAL-SYSTEM/
│
├── app.py
├── requirements.txt
├── render.yaml
├── .python-version
│
├── services/
│   ├── predict_service.py
│   └── report_service.py
│
├── models/
│   └── cnn/
│       ├── mri_model.h5
│       ├── ct_model.h5
│       └── uv_model.h5
│
├── backend/
│
├── templates/
├── static/
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ChSivamowny15/ai-medical-system.git
```

### 2. Navigate to the Project Directory

```bash
cd ai-medical-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

## 🚀 Deployment

The application is configured for deployment using **Render**.

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Python Version: `3.11.9`

## 🎯 Project Objective

The main objective of this project is to develop an AI-based medical image analysis platform that assists in scan classification and automated report generation through deep learning techniques.

## 👩‍💻 Author

**CH. Siva Mowny**

B.Tech – Computer Science and Engineering (AI & ML)  
Kalasalingam Academy of Research and Education

## ⚠️ Disclaimer

This project is developed for educational and research purposes. AI-generated predictions are not a substitute for professional medical diagnosis. All results must be reviewed by qualified healthcare professionals.

## ⭐ Acknowledgement

This project demonstrates the application of Artificial Intelligence, Deep Learning, and Web Development in the healthcare domain.
