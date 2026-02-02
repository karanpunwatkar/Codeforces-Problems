username = input().strip()
distinct_char = set(username)
count = len(distinct_char)

if count % 2 ==0:
  print("CHAT WITH HER")
else:
  print("IGNORE HIM!")
