from state.state import State

# 具体的な個々の状態を表現するクラス
class DockerState(State):
    def __init__(self, state):
        self.state = state

    def getDockerState(self):
        return self.state

class DockerStateBooting(DockerState):
    def __init__(self, state):
        super().__init__(state)

    # 起動中からRUNに移行する
    def handle(self, context):
        print("*** コンテナを起動中です。")
        context.setState(DockerStateRun("running"))

class DockerStateRun(DockerState):
    def __init__(self, state):
        super().__init__(state)
    
    def handle(self, context):
        print("*** コンテナは動作中です。")

class DockerStateDown(DockerState):
    def __init__(self, state):
        super().__init__(state)

    def handle(self,context):
        print("*** コンテナは停止中です。")

class DockerStateReboot(DockerState):
    def __init__(self, state):
        super().__init__(state)
    
    def handle(self, context):
        print("*** コンテナを再起動します。")
        context.setState(DockerStateBooting("booting"))
        context.handle()

        
