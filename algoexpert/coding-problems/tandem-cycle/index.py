# SOLVED
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # if fastest, sort one in reverse otherwise same way
    if fastest:
        redShirtSpeeds.sort(reverse = True)
    else:
        redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed

print(tandemBicycle([5,5,3,9,2], [3,6,7,2,1], True))
