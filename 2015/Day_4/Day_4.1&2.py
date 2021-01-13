import hashlib

puzzle_input = 'yzbqklnj'


def find_lowest_hash(input, n):
  number = 0
  while 1 == 1:
    new_hash = hashlib.md5((input + str(number)).encode("utf-8")).hexdigest()
    if new_hash[:n] == '0' * n:
      print(new_hash)
      return number
    else:
      number += 1

print(find_lowest_hash(puzzle_input, 6))