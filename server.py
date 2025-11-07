from flask import Flask, Response, render_template_string
import requests

app = Flask(__name__)

# 🎙️ Dingin FM yayını Mixxx’ten Render’a gelir
# Mixxx bu adrese yayın yapacak: https://dinginfm.onrender.com/live
# Aşağıdaki şifre Mixxx ve Flask arasında eşleşmeli
SOURCE_PASSWORD = "dingin123"

@app.route('/live', methods=['SOURCE', 'POST', 'GET'])
def live():
    def generate():
        with requests.get("https://example.com", stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(generate(), mimetype="audio/mpeg")

@app.route('/')
def home():
    html = """
    <html>
      <head><title>Dingin FM — Canlı Yayın</title></head>
      <body style="background:#001626;color:#ffd43b;text-align:center;font-family:Segoe UI,sans-serif;">
        <h1>☕ Dingin FM Yayında 🎧</h1>
        <p>Sessizliğin sesi burada...</p>
        <audio controls autoplay src="/live"></audio>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
