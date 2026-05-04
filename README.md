# Mentor-Mentee Form

A web app to fill the Mohan Babu University Mentor-Mentee form and download a filled Excel sheet.

## Stack
- **Backend**: FastAPI + openpyxl (Python)
- **Frontend**: Static HTML/CSS/JS

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/KotalaKishanReddy/mentor-mentee-form.git
cd mentor-mentee-form
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Place the Excel template
Copy `Consolidated-Mentor-Mentee-form.xlsx` to:
```
backend/templates/Consolidated-Mentor-Mentee-form.xlsx
```

### 4. Run the backend
```bash
cd backend
uvicorn main:app --reload
```

### 5. Open the frontend
Open `frontend/index.html` in your browser, or serve it:
```bash
cd frontend
python -m http.server 8080
```
Then go to `http://localhost:8080`

## Deployment
- **Frontend**: Deploy `frontend/` folder to Vercel
- **Backend**: Deploy `backend/` to Render, Railway, or Fly.io
- Update `API_URL` in `frontend/script.js` to your backend URL
