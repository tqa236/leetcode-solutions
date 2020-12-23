class RecentCounter(object):
    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        cut_off = 0
        request_len = len(self.requests)
        for index, request in enumerate(self.requests):
            if t - request <= 3000:
                cut_off = index
                break
        self.requests = self.requests[cut_off:]
        return request_len - cut_off