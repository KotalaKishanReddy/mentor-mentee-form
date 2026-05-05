# Mentor-Mentee Form — Mohan Babu University

A fully serverless web app that fills the official Mentor-Mentee Excel template and returns it for download.

## Stack
| Layer | Technology |
|-------|------------|
| Frontend | Static HTML + CSS + JS (in `public/`) |
| Backend | Vercel Python Serverless Function (`api/fill-form.py`) |
| Excel | `openpyxl` — fills template, preserves all formatting |

## Project Structure
```
mentor-mentee-form/
  api/
    fill-form.py          ← Vercel Python serverless function
  public/
    index.html            ← Form UI (logo + photo + all 13 sections)
    style.css
    script.js
  backend/
    templates/
      Consolidated Mentor-Mentee form.xlsx   ← original template
  vercel.json             ← Vercel routing config
  requirements.txt        ← openpyxl
```

## Deploy to Vercel

1. Go to [vercel.com](https://vercel.com) → **Add New Project**
2. Import this GitHub repo: `KotalaKishanReddy/mentor-mentee-form`
3. Leave all settings default → click **Deploy**
4. Done — your live URL will be `https://mentor-mentee-form.vercel.app`

## Local Development

```bash
npm i -g vercel
vercel dev
```
Then open `http://localhost:3000`
