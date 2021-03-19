import consul


def register(service_name, ip, port):
    c = consul.Consul()
    print(f"Start registering {service_name} services")
    # Health check ip, port, interval
    check = consul.Check.tcp(ip, port, "5s")
    c.agent.service.register(
        service_name, f"{service_name}-{ip}-{port}",
        address=ip, port=port, check=check
    )
    print(f"Register {service_name} successfully")


def unregister(service_name, ip, port):
    c = consul.Consul()
    print(f"Start removing {service_name}")
    c.agent.service.deregister(f"{service_name}-{ip}-{port}")
