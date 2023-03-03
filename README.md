## Throttle Responder
This mini web-server should receive requests containing a delay value (int) and a identificator (sha1).
It returns a response delayed accordingly, containing the identificator.

# Build the container
docker build -t throttle-responder .

# Start the container
docker run -p 5000:5000 throttle-responder

# Example usage
curl --location --request POST 'http://localhost:5000/throttle' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ms": 1000,
    "sha1": "sample_sha1",
    "integer": 10
}'
