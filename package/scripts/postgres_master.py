from resource_management import *
from anaconda_base import AnacondaBase
from resource_management.core.exceptions import ExecutionFailed

class PostgresServer(AnacondaBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)
        print("Installing Ancaonda")

    def configure(self, env):
        import params
        env.set_params(params)
        self.config_pg(env)
        reload_cmd = format("service postgresql-13 reload")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting postgres")
        self.config_pg(env)
        start_cmd = format("service postgresql-13 start")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping postgres")
        stop_cmd = format("service postgresql-13 stop")
        Execute(stop_cmd)

    def restart(self, env):
        print("Restartarting postgres")
        self.config_pg(env)
        Execute('service postgresql-13 restart')

    def status(self, env):
        print("Checking postgres status...")
        Execute('service postgresql-13 status')

if __name__ == "__main__":
    PostgresServer().execute()
