docker run -d -p 5001:5000 -v $(pwd)/msdir_streamer/:/home/bwmicroservice/msdir/ asergiobranco/blackwingmicroservice
docker run -d -p 5002:5000 -v $(pwd)/msdir_single_shot/:/home/bwmicroservice/msdir/ asergiobranco/blackwingmicroservice