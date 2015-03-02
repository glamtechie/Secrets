# Secrets
Secrets is a simple web.py app for storing personal secrets.

Files:
1. schema.sql - Describes tables used for this api
2. auth_model.py - Describes the model used for this api
3. authentication.py - Describes server methods and runs server
4. test.sh - Can be used to test the methods of the api

Required downloads to run this api:
1. Curl (you may choose to send the requests using any other too , but you will have to write your own test commands)

Currently, the api is deployed on: https://poojanaik.webfactional.com/secrets_app/

Required downloads to host your own server:
1. MySQL
2. Python 2.7 (and associated libraries)

API Requests:

POST /new:
    Create new user with username and password. Enter password twice.
    Suggested usage: curl -k -X POST "$ROOT_URL/new" --data "user=poojanaik&pwd1=tarrega&pwd2=tarrega"
    Returns: Badrequest if username exists, passwords don't match or either parameters not specified and displays error message on the server. Otherwise returns success with a message on the server.

POST /login:
    Login user with username and password.
    Suggested usage: curl -k -X POST --header "Authorization: Basic poojanaik:tarrega" "$ROOT_URL/login"
    Returns: Success with a message on the server if successful. Badrequest or unauthorized with error message displayed on the server.

/secrets:

    GET /secrets/(.*):
        Get all or specific secrets of user (Note: User has to be logged in)
        Suggested usage: curl -k -X GET "$ROOT_URL/secrets/" for all secrets
                                                             for secret with a specific ID
        Returns: Json object with secrets and their ids if sucessful. Unauthorized if not logged in.

    POST /secrets:
        Add a secret (Note: User has to be logged in)
        Suggested usage: curl -k -X POST "$ROOT_URL/secrets/" --data "Very secretive here..."
        Returns: Json object with posted secret or unauthorized if not logged in.

    PATCH /secrets/(.*):
        Modify a secret by specifying an id (Note: User has to be logged in)
        Suggested usage: curl -k -X PATCH "$ROOT_URL/secrets/$POST_ID"
        Returns: Json object with modified secret. Badrequest if invalid id, unauthorized if not logged in.

    DELETE /secrets/(.*):
        Delete specific or all secrets of user(Note: User has to be logged in)
        Suggested usage: curl -k -X DELETE "$ROOT_URL/secrets/$POST_ID" for a specific id
                         curl -k -X DELETE "$ROOT_URL/secrets/" for all secrets
        Returns: Success if successful and badrequest or unauthorized if ID is invalid or not logged in

Suggested extensions:
1. Sharing secrets
2. Public secrets
3. Organizing secrets





