import time
with open("banlist.txt", "r") as file:
	print("*Generated `" + time.ctime() + " (" + time.tzname[1] + ")`*")
	print("\n| Date | Host | By | Notes |")
	print("|------|------|----|-------|")
	for line in file:
		split = line.split()
		print("| " + time.ctime(int(split[-1])) + " | `" + split[-3] + "` | " + split[-2] + " |   |")
