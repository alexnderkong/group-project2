docker rm -f $(docker ps -a)
docker rmi -f $(docker images -a -q)
docker pull alexkong14/group-project:latest
sudo docker run -d -p 80:5000 --name group alexkong14/group-project
