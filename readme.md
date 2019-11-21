## running the app
if you want to run the app in your terminal of choice, clone this repository down and cd into group-project2

the command ./jenkins-setup.sh will start the docker container

access the website by navigating to http://<your ip>/80

## aws
the infrastructure of the project is as follows:

the entire project is contained withing a vpc

an SQL RDS has its own security group which has open rds access. it also is in a private subnet that does not allow internet access from outside the vpc

2 ec2 instances use amazon linux 2 and are in a public subnet. the main ec2 instance is in a security group allowing access from all ips on ports 80, 5000, 8080, and 3306.

an auto-scaling group and a load balancer are configured with the main EC2. they are in the same security group as this.

## jenkins

the other instance, named 'jenkins', has a jenkins instance running and is in a security group allowing all inbound access on ports 8080 and 22. importantly, the SSH plugin has been installed. this instance has two jobs - group-project and group-project-pipeline. group-project pipeline is connected with a webhook to this github repository. this repository is also set as its source code.

the pipeline job calls the freestyle job, which uses the build step 'execute shell script on remote host using ssh'. the ssh site is ec2-user@<elastic ip of main ec2> and the command it runs is: ./group-project2/jenkins-setup.sh

this means that pushing an update to git automatically rebuilds and deploys the new application.

