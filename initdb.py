from pet_pals.app import db, app

# # db.drop_all()
# with app.app_context():
#   db.create_all()
app.app_context().push()
db.create_all()