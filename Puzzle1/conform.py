'''Your job is to get a queue of people waiting to enter a stadium
to orient their caps the same way. Challenge: do with the fewest 
requests [commands]
'''
# ten people in the line
# the correct way is backward
# who wear forward needs to change to backward
F = "forward"
B = "backward"
lineCap = [F, B, B, F, F, B, B, B, F, F]
for person in lineCap:
    if person == F:
        person = B
    else: 
        person = B
    print(person, sep= " % ", end=" ")
        


