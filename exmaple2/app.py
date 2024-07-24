# fichier: app.py

def get_user_by_id(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    return user

def send_email_to_user(user, email_content):
    # Logique pour envoyer un email
    pass

def process_user_data(db, user_id, email_content):
    user = get_user_by_id(db, user_id)
    if user:
        send_email_to_user(user, email_content)
    return user
