# Indicate what base image we want to build on top of
FROM python:3.5

# Install the extra python libraries we'll be using
RUN pip install scikit-image 

# Copy our algorithm script into the image
COPY edge_detection.py /edge_detection.py

# Make our script the executable that will be run via "docker run"
ENTRYPOINT ["python", "/edge_detection.py"]
