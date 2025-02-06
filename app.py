from app import create_app, db


app = create_app()


with app.app_context():
    db.create_all()  # Cria as tabelas do banco de dados


if __name__ == "__main__":
    app.run(debug=True)
