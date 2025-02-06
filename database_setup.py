from web import app, db, Movie 


mov1 = Movie(title='The Godfather', release_year=1972, director='Francis Ford Coppola', runtime=175)
mov2 = Movie(title='The Dark Knight', release_year=2008, director='Christopher Nolan', runtime=152)
mov3 = Movie(title='Pulp Fiction', release_year=1994, director='Quentin Tarantino', runtime=154)
mov4 = Movie(title='The Shawshank Redemption', release_year=1994, director='Frank Darabont', runtime=142)

with app.app_context():
    db.create_all()

with app.app_context():
    db.session.add(mov1)
    db.session.add(mov2)
    db.session.add(mov3)
    db.session.add(mov4)
    db.session.commit()