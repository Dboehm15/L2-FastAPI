# L2-FastAPI
Learn to use FastAPI and OpenAI


# Run app
<http client> <my python script>:<the app within the script to run> --<this is optional it forces the app to reload after code changes>


uvicorn application:app --reload
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

# run getRecipe()
curl --location --request POST 'http://127.0.0.1:8000/recipe' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '[
{
"name": "tomato"
},
{
"name": "onion"
},
{
"name": "beer"
},
{
"name": "steak"
}
]'