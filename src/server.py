from flask import (Flask)
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config.from_pyfile('config.py')

jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!',200

@app.route('/user', methods=['GET'])
@jwt_required
def user():
    current_user = get_jwt_identity()
    return f"Hello {current_user}",200

if __name__ == "__main__":
    app.run()
