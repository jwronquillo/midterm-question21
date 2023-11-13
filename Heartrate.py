from flask import Flask, request, jsonify

app = Flask(__name__)

heart_record = [
    {
        "heart_id": "0",
        "date": "13/11/2023",
        "heart_rate": "78bpm",
    },
    {
        "heart_id": "1",
        "date": "13/11/2023",
        "heart_rate": "72bpm",
    },
]

@app.route('/heartrate', methods=['POST'])
def insert_new_heart_record():
    new_record = request.get_json()
    heart_record.append(new_record)
    return {'heart_id': len(heart_record)}, 200

@app.route('/heartrate', methods=['GET'])
def read_a_heart():
    return jsonify(heart_record)

@app.route('/heartrate/<int:index>', methods=['GET'])
def specific_heart_id(index):
    specific = heart_record[index]
    return jsonify(specific)

@app.route('/heartrate/<int:index>', methods=['POST'])
def update_heart_id(index):
    update_record = request.get_json()
    heart_record[index] = update_record
    return {'heart_id': len(heart_record)}, 200

@app.route('/heartrate/<int:index>', methods=['DELETE'])
def delete_heart_id(index):
    heart_record.pop(index)
    return 'A record has been deleted', 200


if __name__ == "__main__":
    app.run()