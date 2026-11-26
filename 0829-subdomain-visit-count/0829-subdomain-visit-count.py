class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        hashmap = dict()
        for cpdomain in cpdomains:
            visit, domain = cpdomain.split(" ")
            visit = int(visit)
            while True:
                print(domain)
                hashmap[domain] = visit + hashmap.get(domain, 0)
                domain = domain.split(".", 1)
                if len(domain) > 1:
                    domain = domain[1]
                else:
                    break
        return [f"{v} {k}" for k, v in hashmap.items()]
          

        