import docker

class FactorioClient:
    def __init__(self):
        self.client = docker.from_env()

    def run(self):
        self.client.containers.run(
            image='factoriotools/factorio',
            detach=True,
            ports={'34197/udp':34197, '27015/tcp':27015},
            name='factorio',
            restart_policy={'Name':'always'},
            volumes={'/opt/factorio':{'bind':'/factorio', 'mode':'rw'}}
        )

    def start(self):
        self.client.containers.get('factorio').start()

    def stop(self):
        self.client.containers.get('factorio').stop()

    def remove(self):
        self.client.containers.get('factorio').remove()

    def update(self):
        self.client.images.pull('factoriotools/factorio', 'latest')

