from .connections import SessionMaker

def get_db():
    session = SessionMaker()

    try:
        yield session
    finally:
        session.close()
