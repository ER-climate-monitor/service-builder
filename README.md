# Service Builder

This repository contains a software that automatically helps deploy a dockerize application to Google Cloud Run service. This application is developed using Python3, [uv](https://docs.astral.sh/uv/) and the [Google Cloud CLI](https://cloud.google.com/cli?hl=en). So before everything install Python3 ([instructions](https://www.python.org/downloads/)), uv ([instructions](https://docs.astral.sh/uv/getting-started/installation/)) and the Google Cloud CLI [instructions](https://cloud.google.com/cli?hl=en).

After cloning this repository, you need to install all the dependencies required from this Python script. In order to achieve this goal, you follow our instructions and use:
1. uv (reccommended)
2. pip

## uv
Install all the dependencies with:

```bash
uv sync
```

After installing all the dependencies, you need to activate the Python virtual environment by running:

```bash
source .venv/bin/activate
```

By doing this operation the *set up* phase has just endend (!!this script in order to work requires also an activate GCP account on your terminal) and you can run the script with:

```bash
uv run script.py /path/to/the/folder/containing/the/dockerfile name-of-the-serice 8080
```

## Pip
Copy the following dependencies inside a *requirements.txt* file.

```txt
annotated-types==0.7.0
pydantic==2.11.4
pydantic-core==2.33.2
python-on-whales==0.76.1
typing-extensions==4.13.2
typing-inspection==0.4.0
```

After you have created the file, you have to create a virtual environment by using the command:

```bash
python3 -m venv /path/to/new/virtual/environment
```

Activate it using:

```bash
source /path/to/new/virtual/environment/bin/activate
```

Now you can install all the needed dependencies with:

```bash
pip3 install -r /path/to/requirements.txt
```

Everything is now ready to run, use the command:

```bash
python3 run script.py /path/to/the/folder/containing/the/dockerfile name-of-the-serice 8080
```
## Build and push your image
By default this script works on the *er-climate-monitor* project (on Google Cloud), so you will need to change that if you have a different name.

The deployment can require some minutes, because:
1. The script builds the Docker image;
2. The script pushes the builded docker image to the Google Cloud Artifact Registry;
3. The script deploys the *latest* image to Google Cloud Run.

After that you will see on you terminal the url where you application is deployed.