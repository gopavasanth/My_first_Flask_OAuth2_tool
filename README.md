# Flask app with Wikimedia OAuth2

This is a simple Flask application that integrates with Wikimedia's OAuth2 service. It allows users to log in via Wikimedia, access their profile information, and display it on the homepage.

## Features:

- User login via Wikimedia OAuth2.
- Access to user profile data after successful authentication.
- Store OAuth token and user profile in the session.

## Prerequisites:

- Python 3.7+.
- Flask.
- Authlib for OAuth2 integration.
- A `.env` file containing your OAuth client ID and client secret.

## Installation:

Follow these steps to set up the app locally:

### 1. Clone the repository:

```bash
git clone https://github.com/gopavasanth/My_first_Flask_OAuth2_tool
cd My_first_Flask_OAuth2_tool
```

### 2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:

Create a .env file in the root of the project directory with the following content:

```bash
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
SECRET_KEY=your-secret-key
```

### 5. Run the app

```bash
python app.py
```
