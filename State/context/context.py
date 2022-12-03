from state.docker_state import DockerState

class Context():
    def __init__(self,state):
        self.state = state

    def setState(self,obj):
        self.state = obj
    
    def handle(self):
        self.state.handle(self)

    def getState(self):
        return self.state.getDockerState()