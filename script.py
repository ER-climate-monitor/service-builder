import os
import sys
from python_on_whales import docker, Image


DOCKER_TAG_FORMAT: str = "europe-west8-docker.pkg.dev/er-climate-monitor/quickstart-docker-repo/{}"


def find_dockerfile(path: str) -> str | None:
    elements: list[str] = os.listdir(path)
    for element in elements:
        if element == "Dockerfile":
            return os.path.join(path, element)
    return None


def build_image(service_folder: str, service_name: str) -> None:
    dockerfile_path: str = find_dockerfile(service_folder)
    if dockerfile_path:
        builded_image: Image = docker.build(
            context_path=service_folder, file=dockerfile_path, tags=[DOCKER_TAG_FORMAT.format(service_name)], push=True, platforms=["linux/amd64"])
    return


def main():
    input_arguments: list[str] = sys.argv[1:]
    if len(input_arguments) > 1:
        build_image(input_arguments[0], input_arguments[1])


if __name__ == "__main__":
    main()
