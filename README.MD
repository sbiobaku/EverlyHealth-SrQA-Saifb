# Set up desktop environment 
https://docs.python.org/3/library/venv.html 

# Pull pytest image
docker pull saifb/docker_pytest

# Clone Testcase from Github


# Copy Testcase to Docker Volume directory
~/pytest

# Run Testcases
docker run -v ~/pytest:/etc/workdir -t Image_ID


