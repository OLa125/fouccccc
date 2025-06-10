from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from inference import analyze_focus
import shutil
import os

app = FastAPI()

# 🔁 إضافة CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # أو حط الدومين بتاع الفرونت هنا
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    with open("temp_video.mp4", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    score = analyze_focus("temp_video.mp4")
    os.remove("temp_video.mp4")

    return {"focus_score": score}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=10000)
