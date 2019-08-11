import container_client


class FactorioClient(container_client.ContainerClient):
    def __init__(self):
        self.container_name = 'factorio'
        self.image_name = 'factoriotools/factorio'
        self.ports={'34197/udp':34197, '27015/tcp':27015}
        self.volumes={'/opt/factorio':{'bind':'/factorio', 'mode':'rw'}}

