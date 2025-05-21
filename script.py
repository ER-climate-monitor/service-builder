import docker
import os
import sys

DOCKER_TAG_FORMAT: str = "europe-west8-docker.pkg.dev/er-climate-monitor/quickstart-docker-repo/%s"


def find_dockerfile(path: str) -> str | None:
    elements: list[str] = os.listdir(path)
    for element in elements:
        if element == "Dockerfile":
            return os.path.join(path, element)
    return None


def build_image(service_folder: str) -> None:
    dockerfile_path: str = find_dockerfile(service_folder)
    return


def main():
    input_arguments: list[str] = sys.argv[1:]


if __name__ == "__main__":
    main()
