from app import create_app

# Creamos la instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)