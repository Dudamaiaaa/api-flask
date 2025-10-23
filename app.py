from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return '''
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                color: #4CAF50;
                text-align: center;
                padding-top: 50px;
                background-color: #f4f4f4;
            }
            h1 {
                color: #2E7D32;
            }
            p {
                font-size: 18px;
                color: #333;
            }
            a {
                color: #4CAF50;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>✅ API Flask criada com sucesso!</h1>
        <p>Bem-vindo ao meu primeiro servidor local com Flask 🚀</p>
        <p>Você pode editar este código e ver as mudanças em tempo real!</p>
        <a href="https://flask.palletsprojects.com/" target="_blank">Saiba mais sobre Flask</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
