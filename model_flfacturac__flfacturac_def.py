
# @class_declaration pedidos_cliente #
from YBUTILS.viewREST import cacheController


class pedidos_cliente(flfacturac):

    def pedidos_cliente_bufferCommited_lineaspedidoscli(self, curLinea=None):
        # _i = self.iface
        curPedido = qsatype.FLSqlCursor(u"pedidoscli")
        curPedido.select(ustr(u"idpedido = ", curLinea.valueBuffer(u"idpedido")))
        if not curPedido.first():
            return False
        curPedido.setModeAccess(curPedido.Edit)
        curPedido.refreshBuffer()
        if not qsatype.FactoriaModulos.get('formRecordpedidoscli').iface.calcularTotalesCursor(curPedido):
            return False
        if not curPedido.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def bufferCommited_lineaspedidoscli(self, curLinea=None):
        return self.ctx.pedidos_cliente_bufferCommited_lineaspedidoscli(curLinea)

