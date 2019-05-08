"""
动态进度条。
"""


def progressbar(cur_num, total_num, gap=5, width=50):
	head = "[{}/{}]".format(cur_num, total_num)
	finish = int(width*cur_num/total_num)
	underway = width - finish
	tail = ">"
	if finish == width:
		tail = ""
	middle = "[" + finish * "=" + tail + underway * "-" + "]" + "\r"
	print(head, middle, end="")


if __name__ == "__main__":
	import time, random

	for i in range(100):
		time.sleep(random.random())
		progressbar(i+1, 100)