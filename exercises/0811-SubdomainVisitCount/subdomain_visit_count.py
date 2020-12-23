from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cpdomain in cpdomains:
            visit = int(cpdomain.split()[0])
            rest = cpdomain.split()[1]
            counter[rest] = counter.get(rest, 0) + visit
            for i, char in enumerate(rest):
                if char == ".":
                    counter[rest[i + 1 :]] = counter.get(rest[i + 1 :], 0) + visit
        return [str(count) + " " + subdomain for subdomain, count in counter.items()]
