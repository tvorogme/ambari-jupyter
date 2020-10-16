from resource_management import Execute, Script
from resource_management.core.exceptions import ExecutionFailed


class AnacondaBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)

        Execute("cd /tmp")

        Execute("curl -O https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")

        try:
            Execute("bash Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/anaconda")
        except ExecutionFailed as ef:
            print("Error, maybe installed {0}".format(ef))

#         filestr = """[Unit]
# Description=Jupyter-Notebook service
# After=network.target
# StartLimitIntervalSec=0
# [Service]
# Type=simple
# Restart=always
# RestartSec=1
# User=root
# ExecStart=/opt/anaconda3/bin/jupyter-notebook
#
# [Install]
# WantedBy=multi-user.target"""
#         Execute(f'echo "{filestr}" > /etc/systemd/system/jupyter.service')

    def install(self, env):
        self.install_ac(self, env)
