from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import Predict
import os
import Firebase
from utils.keys import keys
from utils import fcm_postman_api
import warnings
import Base64_Convertor

firebase_service_key = keys['firebase_service_key']
android_emulator_token = keys['android_emulator_token']

app = Flask(__name__)

app.secret_key = 'yolo-birds-api'
app.config['ALLOWED_EXTENSIONS'] = ['.png', '.jpg', '.jpeg']
app.config['UPLOADS_FOLDER'] = 'static/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads', methods = ['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files['image']
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOADS_FOLDER'], filename)
            extension = os.path.splitext(filepath)[1].lower()

            if extension in app.config['ALLOWED_EXTENSIONS']:
                file.save(filepath)
                result, clsIdx, scores = Predict.custom_detect(filepath)

                image_url = Firebase.upload_image('static/uploads/result.png', Predict.class_names[clsIdx[0]], result)

                title = 'Bird identified'

                header = fcm_postman_api.prepare_header(firebase_service_key)
                payload = fcm_postman_api.prepare_body(image_url, android_emulator_token, result, title)

                fcm_postman_api.send_notification(header, payload)

                for idx, score in zip(clsIdx, scores):
                    print(Predict.class_names[idx], '    ', score)


                flash(result)
                return render_template('uploads.html', image='result.png')

            else:
                flash('Please upload an image file. Allowed extensions are .png, .jpg, .jpeg')
                return redirect(url_for('uploads'))

        else:
            flash('Please select a file')
            return redirect(url_for('uploads'))

    return render_template('uploads.html')

@app.route('/upload-base64', methods = ['POST', 'GET'])
def upload_base64():
    if request.method == 'POST':
        req = request.json

        print(req)
        b64_str = req['b64']

        output = 'test.png'

        Base64_Convertor.decode_image(b64_str, output)

        result, clsIdx, scores = Predict.custom_detect(output)

        image_url = Firebase.upload_image(output, Predict.class_names[clsIdx[0]], result)

        title = 'Bird identified'

        header = fcm_postman_api.prepare_header(firebase_service_key)
        payload = fcm_postman_api.prepare_body(image_url, android_emulator_token, result, title)

        fcm_postman_api.send_notification(header, payload)  
        print('Notification send....')      

        return jsonify({
            "Given" : b64_str
        })
    
    else:
        return ({
            "Respond" : "Get method called"
        })

@app.route('/display-image/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOADS_FOLDER'], filename)

if __name__ == '__main__' :
    warnings.filterwarnings('ignore')
    app.run(debug=True)