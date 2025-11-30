from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "API is running!"}

@app.route("/search", methods=["POST"])
def search_image():
    try:
        data = request.json
        image_base64 = data.get("image")

        if not image_base64:
            return jsonify({"error": "image is required"}), 400

        demo_results = [
            {"title": "Benzer Görsel 1", "url": "https://example.com/img1.jpg"},
            {"title": "Benzer Görsel 2", "url": "https://example.com/img2.jpg"}
        ]

        return jsonify({"results": demo_results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
