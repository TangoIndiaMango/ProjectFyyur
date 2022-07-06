# from app import db

# class Venue(db.Model):
#     __tablename__ = 'Venue'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     address = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     image_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(120))

#     # Completed: implement any missing fields, as a database migration using Flask-Migrate
#     genres = db.Column(db.ARRAY(db.String()))
#     website = db.Column(db.String(120))
#     seeking_talent = db.Column(db.Boolean)
#     seeking_description = db.Column(db.String)
#     shows = db.relationship('Show', cascade="all, delete", backref = 'venue', lazy=True)

#     def __repr__(self):
#       return f'<Venue {self.id} {self.name}>'

# class Artist(db.Model):
#     __tablename__ = 'Artist'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     genres = db.Column(db.String(120))
#     image_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(120))

#     # completed: implement any missing fields, as a database migration using Flask-Migrate
#     website = db.Column(db.String(120))
#     seeking_venue = db.Column(db.Boolean)
#     seeking_description = db.Column(db.String)
#     shows = db.relationship('Show', cascade="all, delete", backref = 'artist', lazy=True)

#     def __repr__(self):
#       return f'<Artist {self.id}{self.name}>'


# # Completed: Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# class Show(db.Model):
#     __tablename__='Show'

#     id = db.Column(db.Integer, primary_key=True)
#     venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False) #venue to show is one-to-many
#     artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False) #artist to show is one-to-many
#     start_time = db.Column(db.DateTime, nullable=False)

#     def __repr__(self):
#       return f'<Show {self.id}>'