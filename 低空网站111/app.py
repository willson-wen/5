from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

@app.route('/api/test')
def test():
    return jsonify({'message': 'API is working!'})

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Vercel 需要这个
application = app

if __name__ == '__main__':
    app.run(debug=True) 