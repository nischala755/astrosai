from flask import Flask, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run the Streamlit app
    subprocess.Popen(["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"])
    return send_file("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)