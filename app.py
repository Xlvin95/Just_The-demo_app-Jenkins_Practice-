from flask import Flask
import os

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # We grab the version from an environment variable (typically injected by Jenkins)
    # This proves the pipeline successfully built and deployed the correct version.
    app_version = os.environ.get('APP_VERSION', '1.0.0')

    # Simple HTML response
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CI/CD Demo App</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding: 50px;">
        <div style="background-color: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h1 style="color: #2c3e50;">Hello from Jenkins CI/CD Pipeline!</h1>
            <p style="color: #34495e; font-size: 1.2em;">
                This simple app is ready for deployment practice.
            </p>
            <hr style="border-top: 1px solid #bdc3c7; margin: 20px 0;">
            <p style="font-weight: bold; color: #e74c3c;">
                Application Version: {app_version}
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # When running locally, it uses port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
