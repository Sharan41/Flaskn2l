# app.py

from flask import Flask, request, jsonify
from nl2query import MongoQuery

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def generate_mongo_query():
    data = request.json
    schema = data['schema']
    text_query = data['text']

    queryfier = MongoQuery('Phi2')
    
    try:
        result = queryfier.generate_query(schema, text_query, max_length=1024)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
