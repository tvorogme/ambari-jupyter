from resource_management import Execute, Script, File, Template, Directory
from resource_management.core.exceptions import ExecutionFailed
import os


class PortForwardBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)


    def configure_ac(self, env):
        pass

    def install(self, env):
        self.install_ac(self, env)
