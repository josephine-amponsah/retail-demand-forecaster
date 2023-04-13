c.NotebookApp.kernel_spec_manager_class = 'nb_conda_kernels.manager.NBCondaKernelSpecManager'

from notebook.auth import login

class CustomAuthHandler(login.LoginHandler):
    def set_default_headers(self):
        super().set_default_headers()
        self.set_header('Access-Control-Allow-Origin', 'https://8888-ladyjossy77-retaildeman-kqskuhxzv7f.ws-eu93.gitpod.io')

c.NotebookApp.allow_origin = 'https://8888-ladyjossy77-retaildeman-kqskuhxzv7f.ws-eu93.gitpod.io'
c.NotebookApp.allow_credentials = True
c.NotebookApp.webapp.settings['cookie_secret'] = 'your_secret_key'

c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors https://8888-ladyjossy77-retaildeman-kqskuhxzv7f.ws-eu93.gitpod.io",
    },
}

c.NotebookApp.login_handler_class = CustomAuthHandler
