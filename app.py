from flask import Flask, jsonify

# Create the Flask app
app = Flask(__name__)

# Define a route for the GET request
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message="Hello, welcome to my APII!")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
