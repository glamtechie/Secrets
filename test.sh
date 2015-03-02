 curl -X POST --header "Authorization: Basic vikesh:vikeshkhanna" "http://0.0.0.0:8080/login" -v
 curl -X POST "http://0.0.0.0:8080/new" --data "user=vikesh&pwd1=vikeshkhanna&pwd2=vikeshkhanna" -v
 curl -X POST "http://0.0.0.0:8080/secrets/" --data "My name and password are the same" -v
 curl -X DELETE "http://0.0.0.0:8080/secrets/2" -v
 curl -X PATCH "http://0.0.0.0:8080/secrets/1" -v
