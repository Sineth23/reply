
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import openai


app = Flask(__name__)

CORS(app, supports_credentials=True)

#app.config['CORS_HEADERS'] = 'application/json'

#openai.api_key = "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"

app = Flask(__name__)

@app.route("/api/response", methods=["POST"])
@cross_origin(supports_credentials=True)

def response():
    openai.api_key = "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"

    data = request.get_json()
    text = data.get("text")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"generate an appropriate response to this text: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    reply = response["choices"][0]["text"].strip()

    return jsonify({"response": reply})
    #return response

if __name__ == "__main__":
    app.run(debug=True)