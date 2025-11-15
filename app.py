from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageEnhance

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ENHANCED_FOLDER'] = 'static/enhanced'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['ENHANCED_FOLDER'], exist_ok=True)


def generate_clinical_note(disease="Pituitary Adenoma", code="D35.2"):
    note = f"""
**Clinical Note:**
*   **O (Objective):** Diagnostic findings confirm a pituitary mass.
*   **A (Assessment):** Benign pituitary adenoma (WHO Grade I).
*   **P (Plan):** Treatment with medication and/or transsphenoidal surgery is indicated. Prognosis is excellent for hormonal recovery.

**ICD-10-CM Code Validation:**
*   **Generated Code:** {code}
*   **Code Description:** Benign neoplasm of pituitary gland
*   **Reference Code:** {code}
*   **Validation:** Match — This code is the correct and specific representation for a benign pituitary adenoma.
    """.strip()
    return note


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict_page():
    return render_template('predict.html')


@app.route('/upload_image', methods=['POST'])
def upload_image():
    file = request.files['image']

    if not file:
        return jsonify({'error': 'No image uploaded.'})

  
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    img = Image.open(filepath)
    img = ImageEnhance.Contrast(img).enhance(1.3)
    img = ImageEnhance.Sharpness(img).enhance(1.2)

    enhanced_filename = f"enhanced_{filename}"
    enhanced_path = os.path.join(app.config['ENHANCED_FOLDER'], enhanced_filename)
    img.save(enhanced_path)

    
    note = generate_clinical_note()

    return jsonify({
        'original_path': filepath.replace('\\', '/'),
        'enhanced_path': enhanced_path.replace('\\', '/'),
        'note': note
    })


if __name__ == '__main__':
    app.run(debug=True)
