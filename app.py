from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Define a sample endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!",status="200")

if __name__ == '__main__':
    # Run the app on http://localhost:5000
    app.run(debug=True)
