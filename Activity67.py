#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for a in range(0,7):
    if weather[a]==0:
        sunny += 1
    else:
        rainy += 1
if sunny>rainy:
    print('THE WEATHER IS AWESOME GO OUTSIDE!')
else:
    print('IT IS VERY BAD WEATHER DO NOT TRY TO GO OUTSIDE!')
