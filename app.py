from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/info')
def info():
    return jsonify({
        "project": "GPT Lab 02",
        "description": "AI Engineering Lab with Cloud Development Focus",
        "technologies": ["Python", "Flask", "JavaScript", "TensorFlow"],
        "developer": "AI Engineering Student"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "message": "Application is running smoothly"})

if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
