from Crypto.Hash import SHA
import time

salt = "ld"
password_hash = "5E0C53EA821401B9A4ED480E0F5C6510E84FDA3E"

start_time = time.time()

for pin in xrange(9999):
    pin_string = str(pin).zfill(4)
    salted_pin = salt + pin_string
    hasher = SHA.new(salted_pin)
    hash_result = hasher.hexdigest().upper()
    if hash_result == password_hash:
        print "Cracked PIN!"
        print pin_string
        break

end_time = time.time()
time_elapsed = end_time - start_time

print "Time Elapsed: " + str(time_elapsed)
