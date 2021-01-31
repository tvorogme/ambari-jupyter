from resource_management import *
from anaconda_base import AnacondaBase
from resource_management.core.exceptions import ExecutionFailed
import subprocess


class JupyterServer(AnacondaBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)
        print("Installing Ancaonda")

    def configure(self, env):
        import params
        env.set_params(params)
        self.configure_ac(env)
        reload_cmd = format("systemctl reload jupyter")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting jupyter")
        start_cmd = format("systemctl start jupyter")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping jupyter")
        stop_cmd = format("systemctl stop jupyter")
        Execute(stop_cmd)

    def restart(self, env):
        self.configure_ac(env)
        print("Restartarting jupyter")
        Execute('systemctl restart jupyter')

    def status(self, env):
        print("Checking jupyter status...")

        try:
            Execute('systemctl status jupyter')
        except ExecutionFailed:
            return False


if __name__ == "__main__":
    JupyterServer().execute()
