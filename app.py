from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY", "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"))

SYSTEM_PROMPT = "Sen AI Tibbiy Yoriqchi. Foydalanuvchi qaysi tilda yozsa osha tilda javob ber. Simptomlarni tingla, qaysi shifokor kerakligini ayt. Oxirida: Bu AI maslahati - shifokorga murojaat qiling."

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
        max_tokens=1000
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
