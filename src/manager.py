# Get Logger
from utilities import log_helper
log = log_helper.get_logger()


def deploy_container(game_type):
    print(f"Deploying {game_type}")
