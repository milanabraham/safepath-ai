# 🌍 SafePath AI – Intelligent Crisis Response & Evacuation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

SafePath AI is an AI-powered disaster response and evacuation guidance system built using **Google Cloud**, **FastAPI**, **Firestore**, **Gemini AI**, and **Google Maps**. It helps people during emergencies by detecting risk levels, identifying the nearest safe location, and providing real-time safety instructions.

**Developed for BNB Marathon 2025 Hackathon** 🚀

---

## 🚨 Problem Statement

During natural disasters (floods, earthquakes, fire, cyclones), people often:

- ❌ Don't know how risky their location is
- ❌ Don't know where the nearest safe place is
- ❌ Panic due to lack of guidance
- ❌ Have no direct way to send SOS to authorities

**This confusion leads to loss of lives.**

---

## ✅ Our Solution

SafePath AI is a web-based AI system that:

- 📍 Detects user's real-time GPS location
- 🏥 Calculates the nearest safe location (shelters / hospitals / relief camps)
- 📏 Calculates distance using geo coordinates
- 🤖 Provides AI-generated emergency safety steps
- 🗺️ Shows safe route using Google Maps
- 🆘 Allows users to send SOS alerts to authorities

---

## 🧠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Backend API service |
| **Google Firestore** | Real-time database |
| **Google Vertex AI (Gemini 2.5 Flash)** | AI-generated instructions |
| **Google Maps JavaScript API** | Route visualization & navigation |
| **Python** | Backend logic |
| **JavaScript + HTML/CSS** | Frontend interface |
| **Docker** | Containerization & deployment |
| **GitHub** | Version control |

---

## ✨ Features

✅ Real-time GPS tracking  
✅ AI-generated safety steps  
✅ Nearest safe place detection  
✅ Distance calculation (Haversine formula)  
✅ Google Map + navigation route  
✅ SOS emergency alerts  
✅ Clean, responsive UI  
✅ Firestore integration  
✅ Large-scale ready  

---

## 🖥️ Project Structure

```
safepath-backend/
│
├── main.py                 # FastAPI server
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container setup
├── safepath-frontend.html  # Frontend UI
├── list_models.py          # Gemini models list
├── .gitignore
└── README.md               # Documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/safepath-ai.git
cd safepath-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Authenticate with Google Cloud (OAuth)

```bash
gcloud auth application-default login
```

**Make sure the following services are enabled:**
- ✅ Firestore
- ✅ Vertex AI
- ✅ Google Maps JavaScript API

### 4. Set Up Environment Variables (Optional)

Create a `.env` file:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_MAPS_API_KEY=your-maps-api-key
```

---

## ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

This will show the **interactive API documentation** (Swagger UI).

---

## 🌐 Run Frontend

Simply **double-click** on:

```
safepath-frontend.html
```

**Allow Location Access** when prompted by your browser.

---

## 🧪 How It Works

1. **User enters:**
   - City
   - Pincode
   - Disaster type

2. **GPS is accessed** via browser

3. **Backend calculates** nearest safe location

4. **AI generates** safety instructions

5. **Google Maps draws** the safest route

---

## 🚨 SOS Feature

Clicking **SEND SOS**:

- 📡 Sends your coordinates to Firestore
- 💾 Saves:
  - City
  - Pincode
  - Disaster type
  - Latitude
  - Longitude

**Authorities can monitor all alerts directly in Firestore.**

---

## 🗺️ Firestore Collections

### `risk_zones`

```
pincode
  ├── riskLevel
  ├── notes
```

### `safe_places`

```
name
type (hospital/shelter/camp)
lat
lng
```

### `sos_alerts`

```
city
pincode
disasterType
latitude
longitude
timestamp
```

---

## 🎥 Demo Flow

1. User selects disaster type
2. Enters city & pincode
3. Clicks **"Find Safe Route"**
4. System shows:
   - ⚠️ Risk level
   - 🏥 Nearest safe place
   - 📏 Distance in KM
   - 🗺️ Live route on map
   - 🤖 AI safety steps

---

## 🏆 Hackathon Value

| Criteria | Score |
|----------|-------|
| Real World Impact | ⭐⭐⭐⭐⭐ |
| AI Usage | ⭐⭐⭐⭐⭐ |
| Cloud Usage | ⭐⭐⭐⭐⭐ |
| Innovation | ⭐⭐⭐⭐ |
| Scalability | ⭐⭐⭐⭐ |

---

## 🚀 Future Improvements

- 🌐 Real-time disaster data from government APIs
- 🌍 Multiple language support
- 📱 SMS + WhatsApp alert system
- 📴 Offline mode via PWA
- 🎙️ AI voice assistant
- 👨‍💼 Admin dashboard for authorities
- 📊 Analytics & heatmap visualization
- 🔔 Push notifications for nearby disasters

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t safepath-ai .
```

### Run Container

```bash
docker run -p 8000:8000 safepath-ai
```

---

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/get-route` | Get safe route & AI instructions |
| `POST` | `/send-sos` | Send SOS alert |
| `GET` | `/risk-zones` | Get all risk zones |
| `GET` | `/safe-places` | Get all safe places |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Name:** Milan Abraham  
**Project:** SafePath AI  
**Hackathon:** BNB Marathon 2025  
**Country:** India 🇮🇳  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

For queries or collaboration:

- 📧 Email: your.email@example.com
- 🐙 GitHub: [@your-username](https://github.com/your-username)
- 💼 LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

---

## ❤️ Final Note

SafePath AI is built with the vision to **save lives**, guide people during emergencies, and support disaster management with **AI + Cloud**.

> **"Technology should not just be smart — it must be life-saving."**

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

**Made with ❤️ for humanity** 🌍
