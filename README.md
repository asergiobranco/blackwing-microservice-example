## Blackwing Microservice Example

This example creates a docker for a microservice running in one-shot-mode, and streaming.

The one-shot-mode means that if it receives a single connection, the microservice will promptly close the socket after parsing and handling the request.

On the streaming mode the 

## Running

To run both docker just:

`sh run.sh`

The one-shot microservice will run in port 5002 while the streaming will run on port 5001.