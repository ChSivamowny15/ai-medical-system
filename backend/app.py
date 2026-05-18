from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

import os
import json

from datetime import datetime

from services.predict_service import predict_image
from services.report_service import generate_report

app = Flask(__name__)

CORS(app)

# =====================================
# PATHS
# =====================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

HISTORY_FILE = os.path.join(
    BASE_DIR,
    "history",
    "history.json"
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

os.makedirs(
    os.path.dirname(HISTORY_FILE),
    exist_ok=True
)

# =====================================
# HOME
# =====================================

@app.route("/")
def home():

    return "AI Multimodal Medical System Running"


# =====================================
# 🔍 PREDICT
# =====================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        file = request.files.get("file")

        if not file:

            return jsonify({
                "error": "No file uploaded"
            })

        # =====================================
        # SAVE IMAGE
        # =====================================

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(file_path)

        # =====================================
        # GET FORM DETAILS
        # =====================================

        scan_type = request.form.get(
            "scan_type"
        )

        patient_name = request.form.get(
            "patient_name"
        )

        patient_age = request.form.get(
            "patient_age"
        )

        patient_gender = request.form.get(
            "patient_gender"
        )

        patient_symptoms = request.form.get(
            "patient_symptoms"
        )

        # =====================================
        # AI PREDICTION
        # =====================================

        result = predict_image(
            file_path,
            scan_type
        )

        if "error" in result:

            return jsonify(result)

        # =====================================
        # ADD EXTRA RESULT DATA
        # =====================================

        result["scan_type"] = scan_type.upper()

        result["patient_name"] = patient_name

        result["patient_age"] = patient_age

        result["patient_gender"] = patient_gender

        result["patient_symptoms"] = patient_symptoms

        result["image_path"] = file_path

        # =====================================
        # CREATE SMS MESSAGE
        # =====================================

        if result["prediction"] == "yes":

            sms_message = f"""
Dear {patient_name},

Your AI {scan_type.upper()} scan analysis is completed.

⚠ Abnormality detected
📊 Confidence: {result['confidence']}%

Please visit the hospital and collect your medical reports for further consultation.

Thank you.
AI Medical Center
"""

        else:

            sms_message = f"""
Dear {patient_name},

Your AI {scan_type.upper()} scan analysis is completed.

✅ Scan looks normal
📊 Confidence: {result['confidence']}%

Please visit the hospital and collect your medical reports.

Thank you.
AI Medical Center
"""

        # =====================================
        # PRINT SMS IN TERMINAL
        # =====================================

        print("\n================ SMS MESSAGE ================\n")

        print(sms_message)

        print("=============================================\n")

        # =====================================
        # LOAD HISTORY
        # =====================================

        try:

            with open(HISTORY_FILE, "r") as f:

                history = json.load(f)

        except:

            history = []

        # =====================================
        # SAVE HISTORY
        # =====================================

        history.append({

            "patient_name": patient_name,

            "patient_age": patient_age,

            "patient_gender": patient_gender,

            "patient_symptoms": patient_symptoms,

            "scan_type": scan_type.upper(),

            "prediction": result["prediction"],

            "confidence": result["confidence"],

            "time": str(datetime.now())
        })

        with open(HISTORY_FILE, "w") as f:

            json.dump(
                history,
                f,
                indent=4
            )

        # =====================================
        # RETURN RESULT
        # =====================================

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


# =====================================
# 📜 HISTORY
# =====================================

@app.route("/history", methods=["GET"])
def history():

    try:

        with open(HISTORY_FILE, "r") as f:

            return jsonify(json.load(f))

    except:

        return jsonify([])


# =====================================
# 📊 DASHBOARD
# =====================================

@app.route("/dashboard", methods=["GET"])
def dashboard():

    try:

        with open(HISTORY_FILE, "r") as f:

            data = json.load(f)

    except:

        data = []

    total = len(data)

    mri = len([
        x for x in data
        if x["scan_type"] == "MRI"
    ])

    ct = len([
        x for x in data
        if x["scan_type"] == "CT"
    ])

    uv = len([
        x for x in data
        if x["scan_type"] == "UV"
    ])

    abnormal = len([
        x for x in data
        if x["prediction"] == "yes"
    ])

    normal = total - abnormal

    latest = data[-1] if total > 0 else None

    return jsonify({

        "total_scans": total,

        "mri_scans": mri,

        "ct_scans": ct,

        "uv_scans": uv,

        "abnormal": abnormal,

        "normal": normal,

        "latest": latest
    })


# =====================================
# 📄 DOWNLOAD REPORT
# =====================================

@app.route("/download-report", methods=["POST"])
def download():

    try:

        data = request.json

        path = generate_report(

            prediction=data["prediction"],

            confidence=data["confidence"],

            scan_type=data["scan_type"],

            patient_name=data["patient_name"],

            patient_age=data["patient_age"],

            patient_gender=data["patient_gender"],

            patient_symptoms=data["patient_symptoms"],

            image_path=data["image_path"]
        )

        return send_file(

            path,

            as_attachment=True,

            download_name="AI_Report.docx"
        )

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


# =====================================
# 🚀 RUN APP
# =====================================

if __name__ == "__main__":

    app.run(
        debug=True
    )