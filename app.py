from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/send-message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    messages.append({"role": "user", "content": user_message})

    try:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': 'An error occurred: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)
