import sys
import time

'''
context = """
It was awesome idea to proceed this party today
but some guys was disagree with our goal
and we left them at home!
    =)  """

f = open('poem.txt', 'w')
# Write text to file
f.write(context)
f.close()

f = open('poem.txt', 'r')
result = f.read()
print(result)
'''


#f = None
try:
    f = open("poem.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press Crtl+C")
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("Clear up: Closed the file...")

