from resource_management import Execute, Script, File, Template, Directory
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
        ExecStart=/opt/anaconda/bin/jupyter-notebook --config {0}jupyter_notebook_config.py

        [Install]
        WantedBy=multi-user.target""".format(params.config_dir)

        if 'anaconda' in os.listdir("/opt"):
            print("already installed")
            return

        try:
            Execute("cd /tmp")
            Directory(path=params.config_dir,
                      owner=params.anaconda_user,
                      group=params.anaconda_group,
                      mode=0o0600)
            try:
                Execute("curl -O https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")
            except:
                Execute("cp /var/lib/ambari-agent/Anaconda3-2020.07-Linux-x86_64.sh /tmp")
            Execute("bash Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/anaconda")
            Execute('echo "{0}" > /etc/systemd/system/jupyter.service'.format(filestr))
            Execute('sudo systemctl daemon-reload')
            self.configure_ac(env)
        except ExecutionFailed as ef:
            print("Error {0}".format(ef))
            return

    def configure_ac(self, env):
        import params
        env.set_params(params)

        conf = dict()
        for key in params.config['configurations']['jupyter-env']:
            conf[key] = params.config['configurations']['jupyter-env'][key]

        conf['jupyter_password'] = params.hashText(conf['jupyter_password'])

        print("----------------------------\n", conf, "\n------------------------------------------------")

        File("{0}jupyter_notebook_config.py".format(params.config_dir),
             content=Template("jupyter_notebook_config.py.j2",
                              configurations=conf),
             owner=params.anaconda_user,
             group=params.anaconda_group,
             mode=0o0600
             )

    def install(self, env):
        self.install_ac(self, env)
