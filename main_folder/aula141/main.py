# from log import LogFileMixin, LogPrintMixin


# lp = LogPrintMixin()
# lp.log_error('something')
# lp.log_success(' booom')

# lf = LogFileMixin()
# lf.log_error('something')
# lf.log_success('OK, deu tudo certo')

# Prefira Composição à Herança

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()
