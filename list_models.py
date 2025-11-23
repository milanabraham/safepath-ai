from google import genai

client = genai.Client(
    vertexai=True,
    project="safepath-ai-479104",
    location="us-central1",
)

print("Available models in us-central1:")
for m in client.models.list():
    print("-", m.name)
