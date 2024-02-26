# ShowCount.py
""" Shows how to use a for-loop for counting."""

# Assign to N th enumber of integers bewteen and including 1 and 1000000
# that are divisible by 2,3, and 5.
N = 0
for k in range(1,1000001):
    if k%2==0 and k%3==0 and k%5==0 :
        N = N+1
print N
