''' Ask the user how many videos they watched in a day 
and how many minutes each video was on average. 
Then calculate and display the total time they spent watching videos in hours and minutes.'''

vid = int(input("How many videos you watched in a day :"))
avg_min_per_vid = int(input("How many minutes each video was on average :"))
total_time = vid * avg_min_per_vid
hours = total_time // 60
minutes = total_time % 60

print(f"You have watched videos for {hours} hours & {minutes} minutes")