import injector

from bf_shop.repositories import ClientRepository, OrderRepository, ProductRepository


class LogicModule(injector.Module):
    def configure(self, binder: injector.Binder) -> None:
        from bf_shop.logic import OrderLogic

        binder.bind(OrderLogic, to=OrderLogic, scope=injector.SingletonScope)


class MemoryProvidersModule(injector.Module):
    @injector.singleton
    @injector.provider
    def provide_clients(self) -> ClientRepository:
        from bf_ram_db.client import ClientRamRepository
        from bf_api.example_data import clients

        return ClientRamRepository(static_data=clients)

    @injector.singleton
    @injector.provider
    def provide_orders(self) -> OrderRepository:
        from bf_ram_db.order import OrderRamRepository
        from bf_api.example_data import orders

        return OrderRamRepository(static_data=orders)

    @injector.singleton
    @injector.provider
    def provide_products(self) -> ProductRepository:
        from bf_ram_db.product import ProductRamRepository
        from bf_api.example_data import products

        return ProductRamRepository(static_data=products)
