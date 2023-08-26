import time

exam_st_date = (11, 12, 2014)
# time.strptime("11, 12,2014")
# print(time)

date = time.strftime("%y-%m-%d %H:%M:%S:")
new_date = (date - exam_st_date)

print(new_date)