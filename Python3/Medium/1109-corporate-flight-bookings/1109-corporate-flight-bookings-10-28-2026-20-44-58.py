class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer = [0]*(n)
        der = [0]*(n+1)
        for first,last,seats in bookings:
            der[first-1]+=seats
            der[last]-=seats

        print(der)
        ch = 0
        for i,c in enumerate(der):
            if not i == n:
                ch+=c
                answer[i]+=ch

        return answer
