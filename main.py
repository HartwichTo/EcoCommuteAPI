from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit_email', methods=['POST'])
def submit_email():
    try:
        data = request.get_json()
        email = data['email']

        # Hier können Sie mit der E-Mail-Adresse 'email' arbeiten, z.B. sie speichern oder verarbeiten.

        response = {
            'message': 'E-Mail wurde erfolgreich empfangen',
            'email': email
        }

        return jsonify(response), 200
    except Exception as e:
        error_response = {
            'error': 'Fehler bei der Verarbeitung des Requests',
            'message': str(e)
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(debug=True)
