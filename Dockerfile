FROM python:3.12-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストールに必要なシステムパッケージ
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 依存関係のコピーとインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードのコピー
COPY src/ ./src/

# ポートの公開
EXPOSE 8000

# サーバーの起動
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
