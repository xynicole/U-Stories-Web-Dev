from google.cloud import datastore


def get_client():
    return datastore.Client()


def get_password_by_username(username):
    client = get_client()
    query = client.query(kind="users")
    query.add_filter("username", "=", username)
    if len(query.fetch()) < 1:
        return False
    else:
        password = query.fetch()[0]['password']
        return password
