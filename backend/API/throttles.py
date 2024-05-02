from rest_framework.throttling import  UserRateThrottle
class TierBasedRateThrottle(UserRateThrottle):
    def allow_request(self, request, view):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser:
                self.rate = '10/day'  # Rate limit for tier 1 users
            else:
                self.rate = '5/day'  # Rate limit for tier 2 users
            self.num_requests, self.duration = self.parse_rate(self.rate)  # Add this

        return super().allow_request(request, view)
