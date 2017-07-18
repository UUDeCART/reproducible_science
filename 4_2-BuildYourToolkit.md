# A Brief Introduction to Using Docker

Docker is an open source platform for distributing software through **containers**. Containers are a light-weight mechanism for creating isolated computing environments within an operating system. You can read Docker's own description of what Docker is [here](https://www.docker.com/what-docker) or, alternatively, this [ZDNet Article, "What is Docker and why is it so darn popular?"](http://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)

Without getting bogged down in the technical details, Docker is popular for two primary reasons:

1. Docker makes it very easy for you to use somebody else's software, particularly if that software is complex to install and configure.

1. Docker makes it very easy for you to share your software with somebody else, thus increasing the potential for your impact in your particular scientific, engineering, or business community.

In thinking about reproducible science, Docker provides another value:

### Docker can facilitate reproducible science by creating a **version controlled** way of specifying "precisely" the computational environment in which your experiment performed.

I put precisely in quotes, because of the complexity of computing environments and the challenges of precisely describing them. We will touch on this later.

![It's turtles all the way down](https://imgs.xkcd.com/comics/pixels.png)

## Docker Images and containers

A Docker image is a binary file that contains all the dependencies necessary to run your software.

### Docker Images are Like Onions

A new image is defined by layering more dependencies onto a more primitive image.

### Containers are the individual compute environments created from an image.


## Running Software with Docker

### Hello, World

In your terminal, run the following command

```Bash
docker run hello-world
```

You should see something similar to the following:

```Bash
powderkeg:reproducible_science brian$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b04784fba78d: Pull complete
Digest: sha256:f3b3b28a45160805bb16542c9531888519430e9e6d6ffc09d72261b0d26ff74f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

powderkeg:reproducible_science brian$
```

#### What happened?

* ``docker run``

This tells docker to **run** a container.

Alternative commands include

1. ``docker build``
1. ``docker pull``

* ``docker run hello-world``

Since we told Docker we want to run a container, we have to tell it which **image** to build the container with.

Here are are telling Docker to create the container from the **``hello-world``** image.

* Since we didn't specify a **tag**, Docker assumes we want to use the *latest* Docker image with this name. (This does not always behave as you would expect.)

The ``hello-world`` image has a default command to execute, which prints out the message we see.

### More Complex examples

The ``docker run SOMEIMAGE`` syntax can be extended by the following syntax:

```bash
docker run SOMEIMAGE SOME_COMMAND
```

#### Hello world with ubuntu

We'll run a container that executes a basic Unix command.

Run the following command in the terminal:

```bash
docker run ubuntu:16.04 echo "hello, world"
```

#### Hello world with python

```bash
docker run python:3.5 python -c "print('hello, world')"
```
#### Hello world with Alpine Python

## Interactive Docker

We can create an interactive computing environment:

* ``-i``: Interactive
* ``-t``: Start a terminal connection
* ``-it``: This combines the two

```bash
docker run -it python:3.5-alpine python
```
## Viewing our Images

To view the images that now exist on your computer, execute the following command:

```bash
docker images
```

You should see a list similar but smaller to the following:

```bash
powderkeg:reproducible_science brian$ docker images
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
chapmanbe/resonant_ct_segmentation   latest              73c2be1fb1ff        3 days ago          1.31 GB
test_build                           latest              31e05604d93e        5 days ago          1.31 GB
<none>                               <none>              baa5b055a881        5 days ago          188 MB
<none>                               <none>              add0514dbb95        5 days ago          1.62 GB
girder/girder                        latest              ba5be9427023        6 days ago          1.46 GB
python                               3.5                 0a5c3ea81b62        9 days ago          684 MB
python                               3.4.6               ada45a0b8d42        9 days ago          680 MB
docker                               latest              192e3edb771f        2 weeks ago         97 MB
python                               3.5-alpine          235019b3e981        2 weeks ago         88.6 MB
postgres                             latest              f8d91fbcfa35        2 weeks ago         269 MB
2017_notebook                        latest              9f5b1e1b585d        3 weeks ago         8.75 GB
2017_myssh                           latest              ce515af29135        3 weeks ago         12.2 MB
2017_sshserver                       latest              ce515af29135        3 weeks ago         12.2 MB
2017_mynginx                         latest              3a38db471fcc        3 weeks ago         21.6 MB
2017_remotedata                      latest              3a38db471fcc        3 weeks ago         21.6 MB
mysql                                latest              44a8e1a5c0b2        3 weeks ago         407 MB
toolshed/requirements                latest              9f184f96efab        3 weeks ago         609 MB
ubuntu                               16.04               d355ed3537e9        3 weeks ago         119 MB
ubuntu                               14.04               4a2820e686c4        3 weeks ago         188 MB
orientdb                             latest              5da77630a9bf        4 weeks ago         149 MB
nginx                                alpine              33aa78cbda15        4 weeks ago         15.5 MB
hello-world                          latest              1815c82652c0        4 weeks ago         1.84 kB
solr                                 latest              99cb7b2a536b        5 weeks ago         518 MB
sickp/alpine-sshd                    latest              37d47e7dd0ef        6 weeks ago         7.79 MB
jupyter/datascience-notebook         11be019e4079        1c9be5e6bb85        7 weeks ago         6.84 GB
atmoz/sftp                           latest              b00345b201f6        7 weeks ago         144 MB
mongo                                latest              0dffc7177b06        6 months ago        402 MB
quay.io/bgruening/galaxy             compose             22e4ba7ca94c        12 months ago       1.55 GB
motiz88/corenlp                      latest              3d3d6ec54eb2        16 months ago       918 MB
```

#### What stands out to you?

* Docker has traditionally built Images around Debian/Ubuntu Linux.
* Alpine Linux creates much smaller containers.

## Defining our own images

We define our own images with a []**Dockerfile.**](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)

Dockerfiles have a lot of options and we will touch on only very simple Dockerfiles.

### Edge Detector

In the repository is a python script ``edge_detector.py`` and a ``Dockerfile``.

``edge_detector.py`` uses [scikit-image]() to create an edge image with a [Sobel filter]().

You can run this against the included image ``chest.jpg``. to find out how to run it, you can type:

```bash
python edge_detector.py --help
```

You might have gotten an error, since scikit-image might not be installed.

If needed, you can install scikit-image with the following command:

```bash
pip install scikit-image
```

**Note:** pip should know the dependencies that scikit-image has and install those also.

Our Dockerfile is very simple. We start with a python:3.5 image, install scikit-image, and then add our script.

We can build an image from the Dockerfile with the following command:

```bash
docker build -t chapmanbe/edger .
```

substituting for "chapmanbe" some string that identifies you.

This command tells docker to build an image that will be tagged with the name "chapmanbe/edger" and to build it with the Dockerfile contained in the current (``.``) directory.

We can now run a container with this image:

```bash

docker run -it chapmanbe/edger  bash
```

The program complains that we haven't provided required arguments.

#### Explore what happens if you change ``ENTRYPOINT`` TO ``CMD``

There are no images in the container for us to process. We can **map/mount** a directory on our host computer to a directory in the container with the ``-v`` option:

```bash
docker run -v DIRECTORY_ON_HOST:DIRECTORY_IN_CONTAINER
```
```bash
docker run -it -v $PWD:/data chapmanbe/edger bash
```

This will connect you to the container with a bash shell. Look at what is in ``/data``.

#### Change ``CMD`` back to ``ENTRYPOINT`` and Rebuild

We can now process an image with our container:

```bash
docker run -it -v $PWD:/data chapmanbe/edger --input /data/chest.jpg --output /data/chest_edge.jpg
```
### Clean up

* List all the containers we've created

```bash
docker ps -a  
```

* Remove containers

```bash
docker rm ContainersID_OR_CONTAINER_NAME
```

* Use the ``--rm`` option when running
