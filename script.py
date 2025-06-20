import os
import sys
from python_on_whales import docker, Image
from subprocess import CompletedProcess, run

DOCKER_TAG_FORMAT: str = "europe-west8-docker.pkg.dev/er-climate-monitor/quickstart-docker-repo/{}"
GCP_URL = "https://run.googleapis.com/v2/projects/e-climate-monitor/locations/europe-west8/services?serviceId={}"


def find_dockerfile(path: str) -> str | None:
    elements: list[str] = os.listdir(path)
    for element in elements:
        if element == "Dockerfile":
            return os.path.join(path, element)
    return None


def build_image(service_folder: str, service_name: str, port: str) -> None:
    print(f"[LOGGER]: Input service folder: {service_folder}")
    dockerfile_path: str = find_dockerfile(service_folder)
    print(f"[LOGGER]: Dockerfile path: {dockerfile_path}")
    if dockerfile_path:
        formatted_tag: str = DOCKER_TAG_FORMAT.format(service_name)
        docker.build(
            context_path=service_folder, file=dockerfile_path, tags=[formatted_tag], push=True, platforms=["linux/amd64"])
        deploy_service(formatted_tag, service_name, port)

    return


def deploy_service(docker_tag: str, service_name: str, port: str) -> None:
    # deploy
    deploy_command: str = "gcloud run deploy {} --image {} --project er-climate-monitor --region europe-west8 --allow-unauthenticated --port {}".format(
        service_name, docker_tag, port)
    run(deploy_command.split(' '))
    create_env(service_name)


def create_env(service_name: str) -> None:
    url_command: str = "gcloud run services describe {} --project er-climate-monitor --region europe-west8 --format=value(status.url)" .format(
        service_name)
    output: CompletedProcess = run(url_command.split(' '), capture_output=True)
    deployed_url: str = output.stdout.decode("utf-8")
    with open('.env', 'a') as f:
        f.write("{}={}\n".format(
            service_name.upper().replace('-', '~'), deployed_url))


def main():
    input_arguments: list[str] = sys.argv[1:]
    if len(input_arguments) > 2:
        build_image(input_arguments[0], input_arguments[1], input_arguments[2])


if __name__ == "__main__":
    main()
