# put your python code here
walk_hr_input = int(input())
walk_min_input = int(input())
walk_sec_input = int(input())

rain_hr_input = int(input())
rain_min_input = int(input())
rain_sec_input = int(input())

walk = walk_hr_input * 3600 + walk_min_input * 60 + walk_sec_input
rain = rain_hr_input * 3600 + rain_min_input * 60 + rain_sec_input

print(rain - walk)