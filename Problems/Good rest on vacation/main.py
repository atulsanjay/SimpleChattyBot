# put your python code here
dur = int(input())
food_per_day = int(input())
flight = int(input())
hotel_per_day = int(input())

total = food_per_day * dur + (flight*2) + hotel_per_day * (dur-1)
print(total)