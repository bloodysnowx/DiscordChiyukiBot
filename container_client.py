import docker


class ContainerClient:
    def __init__(self):
        self.client = docker.from_env()
        self.container_name = ''
        self.image_name = ''
        self.ports={}
        self.volumes={}
        self.environment={}

    def exists(self):
        return len(list(filter(lambda container: container.name == self.container_name, self.client.containers.list()))) > 0

    def is_running(self):
        return self.client.containers.get(self.container_name).status == 'running'
    
    def run(self):
        self.client.containers.run(
            image=self.image_name,
            detach=True,
            ports=self.ports,
            name=self.container_name,
            restart_policy={'Name':'always'},
            volumes=self.volumes,
            environment=self.environment
        )

    def start(self):
        self.client.containers.get(self.container_name).start()

    def stop(self):
        self.client.containers.get(self.container_name).stop()

    def remove(self):
        self.client.containers.get(self.container_name).remove()

    def update(self):
        self.client.images.pull(self.image_name, 'latest')