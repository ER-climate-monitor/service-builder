import os
import sys
from python_on_whales import docker, Image
import subprocess

DOCKER_TAG_FORMAT: str = "europe-west8-docker.pkg.dev/er-climate-monitor/quickstart-docker-repo/{}"
GCP_URL = "https://run.googleapis.com/v2/projects/e-climate-monitor/locations/europe-west8/services?serviceId={}"


def find_dockerfile(path: str) -> str | None:
    elements: list[str] = os.listdir(path)
    for element in elements:
        if element == "Dockerfile":
            return os.path.join(path, element)
    return None


def build_image(service_folder: str, service_name: str) -> None:
    dockerfile_path: str = find_dockerfile(service_folder)
    if dockerfile_path:
        formatted_tag: str = DOCKER_TAG_FORMAT.format(service_name)
        docker.build(
            context_path=service_folder, file=dockerfile_path, tags=[formatted_tag], push=True, platforms=["linux/amd64"])
        deploy_service(formatted_tag, service_name)

    return


def deploy_service(docker_tag: str, service_name: str) -> None:
    # deploy
    deploy_command: str = "gcloud run deploy {} --image {} --project er-climate-monitor --region europe-west8 --allow-unauthenticated".format(
        service_name, docker_tag)
    subprocess.run(deploy_command.split(' '))


def main():
    input_arguments: list[str] = sys.argv[1:]
    if len(input_arguments) > 1:
        build_image(input_arguments[0], input_arguments[1])


if __name__ == "__main__":
    main()
