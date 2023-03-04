# L2-FastAPI
Learn to use FastAPI and OpenAI


# Run app
<lib to run scrip with> <my python script>:<the app within the script to run> --<this is optional it forces the app to reload after code changes>


uvicorn tutorial:app --reload


# run tutorial post
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "string",
"price": 0,
"count": 0,
"id": 0,
"category": "tools"
}'