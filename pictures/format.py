import glob
import os
import random

l = glob.glob('*.jpg')
l = l + glob.glob('*.jpeg')
l = l + glob.glob('*.JPEG')
l = l + glob.glob('*.JPG')

for f in l:
    os.rename(f, f"{random.randint(100,2000)}.jpeg")

l = glob.glob('*.jpg')
l = l + glob.glob('*.jpeg')

i = 0
for f in l:
    while f"{i}.jpeg" in l:
        i += 1
    os.rename(f, f"{i}.jpeg")
    i += 1

print(f"Numer of pictures: {len(l)}")
