# spam_classification

## docker command to pull the image

docker pull teenajain193/spam:v1

## docker command to run
docker run -p 8000:8000 teenajain193/spam:v1

## curl to access the api
curl --location 'http://localhost:8000/detect_spam' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Your email text here."
}'
