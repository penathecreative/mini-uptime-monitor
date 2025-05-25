# Mini Uptime Monitor ⏱️

A simple Flask-based uptime monitor that checks the status of user-submitted websites every 60 seconds.

## Features

- Add websites to be monitored via `/add`
- Check status of all sites via `/status`
- Dockerized and deployed on Azure App Service
- CI/CD with GitHub Actions

## 🧪 API Endpoints

- `POST /add` — Add a website to monitor
  - JSON body: `{ "url": "https://example.com" }`
- `GET /status` — Returns the current status of all sites

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/mini-uptime-monitor.git
cd mini-uptime-monitor
pip install -r requirements.txt
python app.py
```

Or with Docker

```bash
docker build -t uptime-monitor .
docker run -p 5050:5050 uptime-monitor


