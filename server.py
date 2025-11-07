from flask import Flask, Response
import requests

app = Flask(__name__)

# 🎧 Mixxx’in yayın kaynağı adresi
# Mixxx ayarlarında:
# Tür: Shoutcast
# Host: dinginfm.onrender.com
# Port: 10000
# Mount: /live
# Giriş: (boş)
# Şifre: (boş)
SOURCE_URL = "http://dinginfm.onrender.com/live"

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Dingin FM — Sessizliğin Sesi Burada</title>
      <style>
        body {
          margin: 0;
          background: #001626;
          color: #e6edf3;
          font-family: 'Segoe UI', sans-serif;
          text-align: center;
        }
        .logo {
          position: fixed;
          top: 0;
          left: 0;
          width: 100vw;
          height: 100vh;
          object-fit: cover;
          opacity: 0.08;
          z-index: 0;
          pointer-events: none;
        }
        header {
          background: rgba(0, 39, 67, 0.85);
          padding: 20px 10px;
          box-shadow: 0 3px 10px rgba(0, 0, 0, .5);
          position: sticky;
          top: 0;
          z-index: 10;
        }
        h1 {
          color: #ffd43b;
          font-size: 30px;
          margin-bottom: 0;
        }
        h2 {
          color: #9fbdd3;
          margin-top: 5px;
          font-weight: normal;
          font-size: 14px;
        }
        audio {
          width: 90%;
          max-width: 400px;
          margin-top: 40px;
          border-radius: 10px;
          outline: none;
        }
        footer {
          margin-top: 60px;
          padding: 10px;
          font-size: 13px;
          color: #9fbdd3;
        }
      </style>
    </head>
    <body>
      <img src="https://dinginfm.com.tr/assets/logo.png" alt="DinginFM Logo" class="logo">
      <header>
        <h1>DINGIN FM</h1>
        <h2>Sessizliğin Sesi Burada ☕</h2>
      </header>

      <main>
        <audio controls autoplay>
          <source src="/live.mp3" type="audio/mpeg">
          Tarayıcınız ses oynatmayı desteklemiyor.
        </audio>
        <p>📻 DJ Aylak yayında... kahveni al, frekansı yakala.</p>
      </main>

      <footer>© 2025 Dingin FM — Tüm Hakları Saklıdır</footer>
    </body>
    </html>
    """
    return html


@app.route('/live.mp3')
def stream():
    def generate():
        try:
            with requests.get(SOURCE_URL, stream=True, timeout=10) as r:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        yield chunk
        except Exception as e:
            print("Bağlantı hatası:", e)
            yield b""
    return Response(generate(), mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
