import sys
import time
from context.context import Context
from state.docker_state import DockerStateBooting,DockerStateDown,DockerStateReboot,DockerStateRun

def setConcreteState(operation):
    if operation == "start":
        return DockerStateBooting("booting")
    elif operation == "down":
        return DockerStateDown("exited")
    elif operation == "restart":
        return DockerStateReboot("restart")

def startMain(initial_operation, change_operation):
    obj = Context(setConcreteState(initial_operation))
    print("### Dockerを、[{0}]します".format(initial_operation))
    obj.handle()
    print("### Dockerは、[{0}]の動作状態になりました".format(obj.getState()))
    print("")

    print("... sleep 5 second")
    print("")
    time.sleep(5)

    obj.setState(setConcreteState(change_operation))
    print("### Dockerを、[{0}]します".format(change_operation))
    obj.handle()
    print("### Dockerの動作状態は、[{0}]になりました".format(obj.getState()))


if __name__ == "__main__":
    startMain(sys.argv[1], sys.argv[2])