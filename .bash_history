sudo apt update && sudo apt upgrade -y
echo -e "[boot]\nsystemd=true" | sudo tee /etc/wsl.conf
mkdir -p ~/projects/cloud-vault-devops/app
cd ~/projects/cloud-vault-devops/app
nano main.py
nano requirements.txt
nano Dockerfile
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
exit
