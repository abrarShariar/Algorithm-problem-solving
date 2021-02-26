# SOLVED
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    front_row = redShirtHeights;
    back_row = blueShirtHeights;

    if front_row[0] > back_row[0]:
        back_row = redShirtHeights
        front_row = blueShirtHeights

    for i in range(len(front_row)):
        if front_row[i] >= back_row[i]:
            return False
    
    return True
