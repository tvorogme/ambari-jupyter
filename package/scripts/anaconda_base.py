from resource_management import Execute, Script
from resource_management.core.exceptions import ExecutionFailed
import os

class AnacondaBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)

        filestr = """[Unit]
        Description=Jupyter-Notebook service
        After=network.target
        StartLimitIntervalSec=0
        [Service]
        Type=simple
        Restart=always
        RestartSec=1
        User=root
        ExecStart=/opt/anaconda3/bin/jupyter-notebook

        [Install]
        WantedBy=multi-user.target"""

        if 'anaconda' in os.listdir("/opt"):
            print("already installed")
            return

        try:
            Execute("cd /tmp")
            Execute("curl -O https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")
            Execute("bash Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/anaconda")
            Execute('echo "{0}" > /etc/systemd/system/jupyter.service'.format(filestr))
            Execute(f'sudo systemctl daemon-reload')
        except ExecutionFailed as ef:
            print("Error {0}".format(ef))
            return

    def install(self, env):
        self.install_ac(self, env)
