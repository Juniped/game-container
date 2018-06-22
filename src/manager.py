import docker

# Get Logger
from utilities import log_helper
log = log_helper.get_logger()


class Manager:

    def __init__(self):
        self.client = docker.from_env()
        self.running_containers = []

    def deploy_container(self, game_type):
        print(f"Deploying {game_type}")
        deployed_container = self.client.containers.run('baseimage', detach=True)
        self.running_containers.append(deployed_container)

    def list_containers(self):
        print(self.running_containers)


