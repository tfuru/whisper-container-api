from fastapi import FastAPI, UploadFile, File, HTTPException
from .transcribe import transcribe_audio

app = FastAPI(title="Whisper Container API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # ファイル形式のチェック（簡易的）
    if not file.filename.endswith((".wav", ".mp3", ".m4a")):
        raise HTTPException(status_code=400, detail="Unsupported file format. Please upload wav, mp3 or m4a.")
    
    try:
        # ファイル内容を読み込む
        audio_content = await file.read()
        
        # 文字起こし実行
        text = transcribe_audio(audio_content)
        
        return {
            "filename": file.filename,
            "transcription": text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
