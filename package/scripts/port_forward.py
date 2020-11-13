from resource_management import *
from port_forward_base import PortForwardBase
from resource_management.core.exceptions import ExecutionFailed
import subprocess

class JupyterServer(PortForwardBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)
        print("Installing Jupyter Port forwarding")

    def configure(self, env):
        import params
        env.set_params(params)
        self.configure_ac(env)
        reload_cmd = format("service jupyter_portforward reload")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting portforward")
        start_cmd = format("service jupyter_portforward start")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping portforward")
        stop_cmd = format("service jupyter_portforward stop")
        Execute(stop_cmd)

    def restart(self, env):
        self.configure_ac(env)
        print("Restartarting port forwarding")
        Execute('service jupyter_portforward restart')

    def status(self, env):
        print("Checking portforward status...")
        Execute('service jupyter_portforward status')

if __name__ == "__main__":
    JupyterServer().execute()
