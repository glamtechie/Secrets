# Secrets
Secrets is a simple web.py app for storing personal secrets.

Files:
1. schema.sql - Describes tables used for this api
2. auth_model.py - Describes the model used for this api
3. authentication.py - Describes server methods and runs server
4. test.sh - Can be used to test the methods of the api

Required downloads to run this api:
1. Curl (you may choose to send the requests using any other tool)
2. awk (to run test.sh)

To test this api using test.sh, type './test.sh https://poojanaik.webfactional.com/secrets_app' on your terminal.

Currently, the api is deployed on: https://poojanaik.webfactional.com/secrets_app/

Required downloads to host your own server:
1. MySQL
2. Python 2.7 (and associated libraries)

API:

    POST /user:
        Create new user with username and password. Enter password twice. User is also logged in.
        Suggested usage: curl -k -X POST "https://poojanaik.webfactional.com/secrets_app/user" --data "user=poojanaik&pwd1=tarrega&pwd2=tarrega"
        Returns: Badrequest if username exists, passwords don't match or either parameters not specified. Otherwise returns success.

    Note: -k is required with curl because webfaction's ssl certificates fail to get verified by the client. Webfaction documents this issue but ensures that the channel is encrypted.

    DELETE /user:
	   Delete the currently logged-in user.
        Suggested usage: curl -k -X DELETE "https://poojanaik.webfactional.com/secrets_app/user"
        Returns: Returns internal error if user could not be deleted (after logging on the server side), otherwise Success.

    POST /login:
        Login user with username and password.
        Suggested usage: curl -k -X POST --header "Authorization: Basic poojanaik:tarrega" "https://poojanaik.webfactional.com/secrets_app/login"
        Returns: Success if successful. Badrequest or unauthorized otherwise.

    GET /logout:
        Logs out user.
        Suggested usage: curl -k -X GET "https://poojanaik.webfactional.com/secrets_app/secrets/logout"
        Returns: Success

/secrets:

    GET /secrets/(.*):
        Get all or specific secrets of user (Note: User has to be logged in)
        Suggested usage:
                        for all secrets:
                            curl -k -X GET "https://poojanaik.webfactional.com/secrets_app/secrets/"
                        for secret with a specific ID:
                            curl -k -X GET "https://poojanaik.webfactional.com/secrets_app/secrets/POST_ID"
        Returns: Json object with secrets and their ids if sucessful. Unauthorized if not logged in.

    POST /secrets:
        Add a secret (Note: User has to be logged in)
        Suggested usage: curl -k -X POST "https://poojanaik.webfactional.com/secrets_app/secrets/" --data "Very secretive here..."
        Returns: Json object with posted secret or unauthorized if not logged in.

    PATCH /secrets/(.*):
        Modify a secret by specifying an id (Note: User has to be logged in)
        Suggested usage: curl -k -X PATCH "https://poojanaik.webfactional.com/secrets_app/secrets/POST_ID"
        Returns: Json object with modified secret. Badrequest if invalid id, unauthorized if not logged in.

    DELETE /secrets/(.*):
        Delete specific or all secrets of user(Note: User has to be logged in)
        Suggested usage: curl -k -X DELETE "https://poojanaik.webfactional.com/secrets_app/secrets/POST_ID" for a specific id
                         curl -k -X DELETE "https://poojanaik.webfactional.com/secrets_app/secrets/" for all secrets
        Returns: Success if successful and badrequest or unauthorized if ID is invalid or not logged in

Suggested extensions:
1. Sharing secrets
2. Public secrets
3. Organizing secrets





