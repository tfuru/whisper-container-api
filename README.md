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
curl http://localhost:8030/health
```

### transcription

```bash
cd tmp/
curl -X POST http://localhost:8030/transcribe -F "file=@test.wav"
```

## API仕様

### health check

サーバーが正常に動作しているか確認します。

- **URL**: `/health`
- **Method**: `GET`
- **Response**:
    ```json
    {
      "status": "ok"
    }
    ```

### transcription

音声ファイルをアップロードして文字起こしを実行します。

- **URL**: `/transcribe`
- **Method**: `POST`
- **Request (Multipart Form Data)**:
    - `file`: 音声ファイル（wav, mp3, m4a）
- **Response**:
    ```json
    {
      "filename": "test.wav",
      "transcription": "こんにちは、今日はいい天気ですね。"
    }
    ```
