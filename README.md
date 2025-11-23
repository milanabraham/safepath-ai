🌍 SafePath AI – Intelligent Crisis Response & Evacuation System

SafePath AI is an AI-powered disaster response and evacuation guidance system built using Google Cloud, FastAPI, Firestore, Gemini AI, and Google Maps. It helps people during emergencies by detecting risk levels, identifying the nearest safe location, and providing real-time safety instructions.

Developed for BNB Marathon 2025 Hackathon 🚀

🚨 Problem Statement

During natural disasters (floods, earthquakes, fire, cyclones), people often:

Don’t know how risky their location is

Don’t know where the nearest safe place is

Panic due to lack of guidance

Have no direct way to send SOS to authorities

This confusion leads to loss of lives.

✅ Our Solution

SafePath AI is a web-based AI system that:

Detects user’s real-time GPS location

Calculates the nearest safe location (shelters / hospitals / relief camps)

Calculates distance using geo coordinates

Provides AI-generated emergency safety steps

Shows safe route using Google Maps

Allows users to send SOS alerts to authorities

🧠 Technologies Used

FastAPI – Backend API service

Google Firestore – Database

Google Vertex AI (Gemini 2.5 Flash) – AI instructions

Google Maps JavaScript API – Route & map

Python + JavaScript + HTML/CSS

Docker – Deployment ready

GitHub – Version control

✨ Features

✅ Real-time GPS tracking
✅ AI-generated safety steps
✅ Nearest safe place detection
✅ Distance calculation (Haversine formula)
✅ Google Map + navigation route
✅ SOS emergency alerts
✅ Clean UI
✅ Firestore integration
✅ Large scale ready

🖥️ Project Structure
safepath-backend/
│
├── main.py                # FastAPI server
├── requirements.txt        # Dependencies
├── Dockerfile              # Container setup
├── safepath-frontend.html  # UI
├── list_models.py          # Gemini models list
├── .gitignore
└── README.md

🛠️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/safepath-ai.git
cd safepath-ai

2. Install Dependencies
pip install -r requirements.txt

3. Authenticate with Google Cloud (OAuth)
gcloud auth application-default login


Make sure:

Firestore is enabled

Vertex AI is enabled

Google Maps API is enabled

▶️ Run Backend
uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000/docs

🌐 Run Frontend

Simply double click on:

safepath-frontend.html


Allow Location Access when prompted.

🧪 How It Works

User enters:

City

Pincode

Disaster type

GPS is accessed via browser

Backend calculates nearest safe location

AI gives safety instructions

Google Maps draws route

🚨 SOS Feature

Clicking SEND SOS:

Sends your coordinates to Firestore

Saves:

City

Pincode

Disaster

Latitude

Longitude

Authorities can monitor all alerts directly in Firestore.

🗺️ Firestore Collections

risk_zones

pincode
  ├── riskLevel
  ├── notes


safe_places

name
type (hospital/shelter/camp)
lat
lng


sos_alerts

city
pincode
disasterType
latitude
longitude

🎥 Demo Flow

User selects disaster

Enters city & pincode

Clicks "Find Safe Route"

System shows:

Risk level

Nearest safe place

Distance in KM

Live route on map

AI safety steps

🏆 Hackathon Value
Criteria	Value
Real World Impact	✅✅✅✅✅
AI Usage	✅✅✅✅✅
Cloud Usage	✅✅✅✅✅
Innovation	✅✅✅✅
Scalability	✅✅✅✅
🚀 Future Improvements

Real-time disaster data from government APIs

Multiple language support

SMS + WhatsApp alert system

Offline mode via PWA

AI voice assistant

Admin dashboard for authorities

👨‍💻 Developer

Name: Milan Abraham
Project: SafePath AI
Hackathon: BNB Marathon 2025
Country: India 🇮🇳

❤️ Final Note

SafePath AI is built with the vision to save lives, guide people during emergencies and support disaster management with AI + Cloud.

"Technology should not just be smart — it must be life-saving."
