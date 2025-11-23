from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import firestore
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import math

# --------------------
# CONFIGURATION
# --------------------

client = genai.Client(
    vertexai=True,
    project="safepath-ai-479104",
    location="us-central1"
)

db = firestore.Client(project="safepath-ai-479104")

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# MODELS
# --------------------
class RiskRequest(BaseModel):
    disasterType: str
    pincode: str
    city: str = "Unknown"
    latitude: float
    longitude: float

# --------------------
# HELPERS
# --------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in KM
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)

    a = math.sin(dLat/2)**2 + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon/2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# --------------------
# TEST ENDPOINT
# --------------------
@app.get("/")
def home():
    return {"status": "SafePath AI backend is running ✅"}

# --------------------
# SOS ENDPOINT
# --------------------
@app.post("/sos")
def sos(data: RiskRequest):
    db.collection("sos_alerts").add({
        "city": data.city,
        "pincode": data.pincode,
        "disasterType": data.disasterType,
        "latitude": data.latitude,
        "longitude": data.longitude
    })
    return {"status": "🚨 SOS Alert Sent to Authorities"}

# --------------------
# RISK CHECK ENDPOINT
# --------------------
@app.post("/risk-check")
def risk_check(data: RiskRequest):

    # ✅ USE REAL GPS (from frontend)
    user_lat = data.latitude
    user_lng = data.longitude

    # 1. Get risk zone info (extra context)
    risk_doc = db.collection("risk_zones").document(data.pincode).get()

    if risk_doc.exists:
        zone_data = risk_doc.to_dict()
        risk_level = zone_data.get("riskLevel", "unknown")
        notes = zone_data.get("notes", "")
    else:
        risk_level = "unknown"
        notes = "No specific government risk data for this area."

    # 2. Find closest safe place
    safe_places = db.collection("safe_places").stream()

    closest_place = None
    shortest_distance = float("inf")

    for place in safe_places:
        place_data = place.to_dict()
        place_lat = place_data.get("lat")
        place_lng = place_data.get("lng")

        if place_lat is not None and place_lng is not None:
            distance = calculate_distance(
                user_lat,
                user_lng,
                place_lat,
                place_lng
            )

            if distance < shortest_distance:
                shortest_distance = distance
                closest_place = place_data

    if closest_place is None:
        return {"error": "No safe places found in database."}

    # 3. Ask Gemini for instructions
    prompt = f"""
    A person is in {data.city} (pincode: {data.pincode}).
    Disaster type: {data.disasterType}
    Risk level: {risk_level}
    Area notes: {notes}

    Nearest Safe Location: {closest_place["name"]} ({closest_place["type"]})
    Distance: {round(shortest_distance, 2)} km

    Give 5 simple safety steps.
    Use easy language.
    End with: "Contact local authorities for official instructions."
    """

    response = client.models.generate_content(
        model="publishers/google/models/gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text

    # 4. Save full check history
    db.collection("checks").add({
        "pincode": data.pincode,
        "city": data.city,
        "disasterType": data.disasterType,
        "riskLevel": risk_level,
        "notes": notes,
        "userLocation": {
            "lat": user_lat,
            "lng": user_lng
        },
        "nearestPlace": closest_place,
        "distance_km": round(shortest_distance, 2),
        "aiResponse": ai_text
    })

    # 5. Send result to frontend
    return {
        "pincode": data.pincode,
        "city": data.city,
        "disasterType": data.disasterType, 
        "riskLevel": risk_level,
        "notes": notes,
        "aiResponse": ai_text,
        "safeLocation": {
            "name": closest_place["name"],
            "type": closest_place["type"],
            "lat": closest_place["lat"],
            "lng": closest_place["lng"]
        },
        "distance_km": round(shortest_distance, 2)
    }
