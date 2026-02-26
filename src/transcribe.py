import io
from faster_whisper import WhisperModel

# モデルの初期化（CPU使用をデフォルトとするが、性能向上のためint8量子化を使用）
# コンテナ環境に合わせてデバイスや計算タイプを調整可能
model_size = "base"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def transcribe_audio(audio_data: bytes):
    """
    音声バイナリを受け取り、文字起こし結果をテキストで返す
    """
    # バイナリデータをファイルライクオブジェクトに変換
    audio_file = io.BytesIO(audio_data)
    
    segments, info = model.transcribe(audio_file, beam_size=5)
    
    # セグメントを結合して一つのテキストにする
    full_text = ""
    for segment in segments:
        full_text += segment.text
        
    return full_text.strip()
