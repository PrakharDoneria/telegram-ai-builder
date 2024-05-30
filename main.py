from flask import Flask, request, jsonify, g
from bot_manager import bot_manager
import database

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def index():
    return "Running"

@app.route('/new', methods=['GET'])
def new_bot():
    token = request.args.get('bot')
    if not token:
        return jsonify({"error": "No bot token provided"}), 400

    try:
        bot_manager.start_bot(token)
        database.insert_token(token)
        return jsonify({"message": "Bot started and token stored successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/start_all', methods=['GET'])
def start_all_bots():
    try:
        tokens = database.get_all_tokens()
        for token in tokens:
            bot_manager.start_bot(token[0])
        return jsonify({"message": "All bots started successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        database.init_db()  
        start_all_bots()  
    app.run(host='0.0.0.0',port=3000, debug=True)
