from TREINAMENTO import app, db

if __name__ == '__name__':
    with app.app_context():
        db.create_all()
    
    app.run(host='localhost', port=5000)