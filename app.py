from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name from environment variables
    full_name = "Vijay Dappili"
    
    # Get username
    username = os.getlogin()
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Format output for web display
    html = f"""
    <html>
    <head><title>HTOP Output</title></head>
    <body>
        <h2>Name: {full_name}</h2>
        <h2>User: {username}</h2>
        <h2>Server Time (IST): {server_time}</h2>
        <h2>TOP Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
