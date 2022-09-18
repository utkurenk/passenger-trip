# passenger-trip restapi

## installation

to deploy the application run following commands

```
docker pull holyhumerus/passenger-trip

docker run -p 127.0.0.1:8000:8000 holyhumerus/passenger-trip
```

## installation by building docker image

to build the docker image and run the docker container, run the following commands

```
git clone https://github.com/utkurenk/trip-logs.git

docker build . -t passenger-trip

docker run -p 127.0.0.1:8000:8000 passenger-trip
```