# SimonDockerAPI
A simple docker based installation of the SIMON API

### To run on a fresh vm try this:

sudo apt update && sudo apt-get update && sudo apt upgrade -y && sudo apt-get upgrade -y && sudo apt autoremove -y && sudo apt-get autoremove -y && sudo apt-get install nano git docker.io -y

sudo groupadd docker

sudo usermod -a -G docker ${USER}

#### Exit

git clone https://www.github.com/doclock17/SimonDockerAPI && cd SimonDockerAPI/

docker image build --tag doclock17/simon_docker_api:2.0 .

docker container run --publish 5000:5000 --name simon_docker_api doclock17/simon_docker_api:2.0

