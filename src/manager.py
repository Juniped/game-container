import docker

# Get Logger
from utilities import log_helper
log = log_helper.get_logger()


class Manager:

    def __init__(self):
        self.client = docker.from_env()
        self.running_containers = {
            "Terraria": []
        }

    def deploy_container(self, game_type):
        game_name = self.parse_name(game_type)
        log.info(f"Deploying {game_name}-{len(self.running_containers[game_name])}")
        deployed_container = self.client.containers.run(
            'baseimage',
            detach=True,
            name=f"{game_name}-{len(self.running_containers[game_name])}")
        self.running_containers[game_name].append(deployed_container)

    def list_containers(self):
        for game_key in self.running_containers.keys():
            print(f"Game: {game_key}")
            for container in self.running_containers[game_key]:
                print("----------------------")
                print(f"    NAME: {container.name}")
                print(f"    STATUS: {container.status}")

    def stop_all_containers(self):
        print("Stopping and removing all containers started by this program")
        for game_key in self.running_containers.keys():
            for container in self.running_containers[game_key]:
                container.stop()
                container.remove()

    def parse_name(self, game_type):
        if game_type == 1:
            return "Terraria"
        else:
            return "undefined"
        pass


