from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from math import gcd

class MDCService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def calcular_mdc(ctx, x, y):
        return gcd(x, y)

application = Application([MDCService], 'imagem.digital',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))
    server.serve_forever()
