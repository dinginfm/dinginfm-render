from flask import Flask, Response
import requests

app = Flask(__name__)

# 🎧 Mixxx'in Icecast yayını adresi
# Mixxx’te Host olarak dinginfm.onrender.com, Port olarak 10000 kullanılacak
SOURCE_URL = "http://localhost:8000/live"

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
          paddi
