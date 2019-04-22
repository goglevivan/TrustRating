import math
def get_rating(size_of_worker,p=0.0001,level=1,size_of_relationships=0):
    level = int(level)
    size_of_worker = int(size_of_worker)
    temp = size_of_worker * p / level
    TrustRating = temp * math.exp(-temp)
    pr = size_of_relationships/size_of_worker
    TrustRating = TrustRating + TrustRating*pr
    return TrustRating
