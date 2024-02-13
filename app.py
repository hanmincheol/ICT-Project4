from flask import Flask
from flask_restful import Api
from api.mask_detection import MaskDetection


#플라스크 앱 생성
app = Flask(__name__)

api = Api(app)

api.add_resource(MaskDetection,'/mask')
if __name__ == '__main__':
    app.run(debug=True)