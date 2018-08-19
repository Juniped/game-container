import docker

# Get Logger
from utilities import log_helper
log = log_helper.get_logger()


class Manager:

    def __init__(self):
        self.client = docker.from_env()
        self.port = 8000
        self.terraria_base_port = "7777/tcp"
        self.running_containers = {
            "Terraria": []
        }
        self.stopped_containers = []

    def deploy_container(self, game_type):
        game_name = self.parse_name(game_type)
        internal_port = self.__get_port__(game_name)
        host_port = self.port
        self.port += 1
        log.info(f"Deploying {game_name}-{len(self.running_containers[game_name])}")
        deployed_container = self.client.containers.run(
            'terraria',
            detach=True,
            name=f"{game_name}-{len(self.running_containers[game_name])}",
            ports={internal_port: host_port},
            command="/bin/bash -c ./terraria.sh")
        deployed_container.start()
        self.running_containers[game_name].append({
            'name': deployed_container.name,
            'container_object': deployed_container,
            'host_port': host_port,
            'internal_port': internal_port})

    def list_containers(self, all_containers=False):
        for game_key in self.running_containers.keys():
            # container_count = 1
            print(f"Game: {game_key}")
            for container in self.running_containers[game_key]:
                container_object = container['container_object']
                print("----------------------")
                print(f"    NAME: {container_object.name}")
        if all_containers:
            print(f"--------------------------\nSTOPPED CONTAINERS")
            for container in self.stopped_containers:
                obj = container.get('container_object')
                print(f"   NAME: {obj.name}")

    def get_container_info(self):
        cont_list = []
        for game_key in self.running_containers.keys():
            cont_list.extend(self.running_containers[game_key])
        cont_list.extend(self.stopped_containers)
        return cont_list

    def stop_all_containers(self):
        print("Stopping and removing all containers started by this program")
        for game_key in self.running_containers.keys():
            for container in self.running_containers[game_key]:
                obj = container.get('container_object')
                obj.stop()
                obj.remove()

    def parse_name(self, game_type):
        if game_type == 1:
            return "Terraria"
        else:
            return "undefined"
        pass

    def __get_port__(self, name):
        if name == "Terraria":
            return self.terraria_base_port
        return None


