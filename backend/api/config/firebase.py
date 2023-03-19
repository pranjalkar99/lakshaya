from firebase_admin import auth

async def firebase():
    default_app = firebase_admin.initialize_app()
    print(default_app.name)  # "[DEFAULT]"