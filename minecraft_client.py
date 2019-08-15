import container_client


class MinecraftClient(container_client.ContainerClient):
    def __init__(self):
        super().__init__()
        self.container_name = 'minecraft'
        self.image_name = 'itzg/minecraft-server'
        self.ports={'25565':25565}
        self.volumes={'/opt/minecraft':{'bind':'/data', 'mode':'rw'}}
        self.environment={'EULA':'TRUE'}

