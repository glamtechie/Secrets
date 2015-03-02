if [ "$#" -ne 1 ]; then
	echo -e  "Usage: ./test.sh <root_url>"
	exit -1
fi

ROOT_URL="$1"

echo -e  "Creating new user..."
curl -X POST "$ROOT_URL/new" --data "user=poojanaik&pwd1=tarrega&pwd2=tarrega"  && echo -e  "\n"

echo -e  "Logging in..."
curl -X POST --header "Authorization: Basic poojanaik:tarrega" "$ROOT_URL/login" && echo -e "\n"

echo -e "Deleting all secrets of test user..."
curl -X DELETE "$ROOT_URL/secrets/" && echo -e  "\n"

echo -e  "Posting a secret..."
curl -X POST "$ROOT_URL/secrets/" --data "Very secretive here..." && echo -e "\n"

echo -e  "Posting another secret..."
POST2=`curl -X POST "$ROOT_URL/secrets/" --data "Very secretive here...Part 2"`
echo -e "\n"
POST2_ID=`echo $POST2 | awk -F: '{print $3}' | awk -F'}' '{print $1}'`

echo -e  "Posting yet another secret..."
POST3=`curl -X POST "$ROOT_URL/secrets/" --data "Very secretive here...Part 3"` 
echo -e "\n"
POST3_ID=`echo $POST3 | awk -F: '{print $3}' | awk -F'}' '{print $1}'`

echo -e  "Getting all secrets..."
curl -X GET "$ROOT_URL/secrets/" && echo -e "\n"

echo -e  "Deleting secret with ID=$POST3_ID..."
curl -X DELETE "$ROOT_URL/secrets/$POST3_ID" && echo -e  "\n"

echo -e  "Patching and updating secret with ID=$POST2_ID..."
curl -X PATCH "$ROOT_URL/secrets/$POST2_ID" --data "New Secret!" && echo -e  "\n"

echo -e  "Getting all secrets..."
curl -X GET "$ROOT_URL/secrets/" && echo -e  "\n"
