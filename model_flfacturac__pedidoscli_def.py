
# @class_declaration pedidos_cliente #
class pedidos_cliente(flfacturac):

    def pedidos_cliente_getDesc(self):
        desc = "nombrecliente"
        return desc

    def pedidos_cliente_initValidation(self, name, data=None):
        response = True
        return response

    def pedidos_cliente_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.pedidos_cliente_getDesc()

    def initValidation(self, name, data=None):
        return self.ctx.pedidos_cliente_initValidation(name, data)

    def getFilters(self, model, name, template=None):
        return self.ctx.pedidos_cliente_getFilters(model, name, template)

