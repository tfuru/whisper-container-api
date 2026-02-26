# whisper-container-api
Faster-Whisper をコンテナ化して API サーバーとして提供する

## 環境
- podman compose
- python 3.12

## 構成
- src/api.py: FastAPIサーバー
- src/transcribe.py: Faster-Whisperによる文字起こし
- Dockerfile: Dockerイメージ
- requirements.txt: Pythonパッケージ
- compose.yml: Podman Compose設定

## 使い方
### コンテナのビルドと起動

```bash
# ビルド
podman compose build

# 起動
podman compose up -d
```

### 動作確認（ログ）
```bash
podman compose logs -f
```

### health check

```bash
curl http://localhost:8000/health
```

### transcription

```bash
cd tmp/
curl -X POST http://localhost:8000/transcribe -F "file=@test.wav"
```

## API仕様

### health check

```
GET /health
```

### transcription
wav ファイルを POST する

```
POST /transcribe 
```
