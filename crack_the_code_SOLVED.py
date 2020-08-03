# don't print anything in the console, because it will take to much time
import hashlib
def crack(hash):
    for i in range(100000):
        hashhex = hashlib.md5(f"{str(i).zfill(5)}".encode("utf-8")).hexdigest()
        if hashhex == hash:
            return str(i).zfill(5)



crack("827ccb0eea8a706c4c34a16891f84e7b")

print(f"{str(12345).zfill(5)}")