# Extraction of Text from PDFs

## Setup
Follow the instructions [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#uninstall-old-versions) to set up Docker for Ubuntu, [here](https://docs.docker.com/docker-for-mac/install/) to set up Docker for Mac OS X, or [here](https://docs.docker.com/docker-for-windows/install/) to set up Docker for Windows.

Use the script `install.sh` to set up `pipenv` and pull the latest Docker image for `grobid`.

Alternately, you can also set up `pipenv` manually.

Note: you have to have python3.6 in order to run this program
```
# Mac OS
brew install pipenv

# Pip Installation
pip3 install --user pipenv # install pipenv in the local directory

pip3 install  pipenv # needs sudoer permission
```

The Grobid Docker container can be set up using the commands

```
docker pull lfoppiano/grobid:0.5.1
```

## Run Grobid

Use the script `grobid.sh` to start or stop the grobid service as a Docker container. The script is very simple right now and only takes in a positional argument of `start` or `stop`.

Alternately, you can also start grobid from the command line as

```
docker run -t --rm --init --name grobid -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.5.1
```

This will host the service on `localhost:8080`.

## Run extraction

Run the `full_text_extract.py` to extract out the text from PDF. This can be done by:

```
pipenv run python full_text_extract.py -h
```
