# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.


import random
import math

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""

import array

def fuzzit(content):
# Write a random fuzzer for a simulated text viewer application
    FuzzFactor = 250
    num_tests = 10000

    buf = bytearray(content, "utf-8")
    strlst = []
    for i in range(num_tests):
        numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1
        for j in range(numwrites):
            rbyte = random.randrange(256)
            rn = random.randrange(len(buf))
            buf[rn] = rbyte
            strlst.append(str(buf))
    return strlst

