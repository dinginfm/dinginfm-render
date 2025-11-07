from flask import Flask, Response
import requests

app = Flask(__name__)

# 🎙️ Dingin FM canlı yayın kaynağı adresi
# Buraya kendi Icecast veya Mixxx yayınının adresini yaz
SOURCE_URL = "http://senin-ip-adresin:8000/live"  

@app.route('/live')
def live():
    def generate():
        with requests.get(SOURCE_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(generate(), mimetype='audio/mpeg')

@app.route('/')
def home():
    return '''
    <html>
      <head><title>Dingin FM — Canlı Yayın</title></head>
      <body style="background:#001626;color:#ffd43b;text-align:center;font-family:Segoe UI, sans-serif;">
        <h1>☕ Dingin FM Yayında 🎧</h1>
        <p>Sessizliğin sesi burada...</p>
        <audio controls autoplay src="/live"></audio>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
