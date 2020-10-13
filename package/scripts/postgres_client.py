from resource_management import *
from anaconda_base import AnacondaBase


class AnacondaClient(AnacondaBase):
    postgres_packages = ['postgresql-13']

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)


if __name__ == "__main__":
    AnacondaClient().execute()
