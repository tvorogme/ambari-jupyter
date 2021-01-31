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
        reload_cmd = format("systemctl reload jupyter_portforward")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting portforward")
        start_cmd = format("systemctl start jupyter_portforward")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping portforward")
        stop_cmd = format("systemctl stop jupyter_portforward")
        Execute(stop_cmd)

    def restart(self, env):
        self.configure_ac(env)
        print("Restartarting port forwarding")
        Execute('systemctl restart jupyter_portforward')

    def status(self, env):
        print("Checking portforward status...")
        Execute('systemctl status jupyter_portforward')

if __name__ == "__main__":
    JupyterServer().execute()
