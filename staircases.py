bricks_init = 200

def number_of_staircases(bricks):
    count = 0
    for i in range(2,21):
        print(i*(i+1)/2)
        if i*(i+1)/2 > bricks:
            return count
        rem_bricks = bricks-(i*(i+1)/2)
        count+= (rem_bricks//2 +1)

print(number_of_staircases(bricks_init))