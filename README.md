# spam_classification

## docker command to pull the image

docker pull teenajain193/spam

## docker command to run
docker run -p 8000:8000 teenajain193/spam

## curl to access the api
curl --location 'http://localhost:8000/detect_spam' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Your email text here."
}'

## Deployment 

kubectl apply -f deployment.yaml

kubectl get pods(to check whether the pod is running)

#### port-forward to test api on local

kubectl port-forward pod_name 8000:8000

#### Then you can use above curl to access the api.




