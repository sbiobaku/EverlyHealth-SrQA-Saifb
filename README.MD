### Set up desktop environment 
https://docs.python.org/3/library/venv.html 

https://docs.docker.com/desktop/

### Pull pytest image
docker pull saifb/docker_pytest

### Clone Testcase from Github
https://github.com/sbiobaku/EverlyHealth-SrQA-Saifb

### Copy Testcase to Docker Volume directory
~/pytest

### Run Testcases
docker run -v ~/pytest:/etc/workdir -t Image_ID


