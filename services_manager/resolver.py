from dns import resolver
from dns.exception import DNSException

consul_resolver = resolver.Resolver()
consul_resolver.port = 8600
consul_resolver.nameservers = ["127.0.0.1"]


def get_service(service_name):
    try:
        dns_answer = consul_resolver.resolve(f'{service_name}.service.consul', "A")
        dns_answer_srv = consul_resolver.resolve(f"{service_name}.service.consul", "SRV")
    except DNSException:
        return None, None
    return dns_answer[0].address, dns_answer_srv[0].port
