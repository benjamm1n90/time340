from timespan import TimeSpan

dur1 = TimeSpan(3, 67)
dur2 = TimeSpan(74, -5, 8)
print(dur1)
print("^ should be 1 hours, 7 minutes, 3 seconds")
print(dur2)
print("^ should be 7 hours, 56 minutes, 14 seconds")
print(dur1 + dur2)
print("^ should be 9 hours, 3 minutes, 17 seconds")
print(dur1 - dur2)
print(dur2 - dur1)
dur2 += dur1
print(dur2)
dur3 = -dur2
print(dur3)
print("^ neg should be -9, -3, -17")
dur4 = TimeSpan(6,7,8)
dur5 = TimeSpan()
durE = dur4
dur5.set_time(6, 5, 8)
print("dur4: " + str(dur4))
print("dur5: " + str(dur5))
if dur4 >= dur5:
    print("dur4 is >= than dur5")
else:
    print("dur4 is not >= than dur5")
    
if dur4 <= dur5:
    print("dur4 is <= than dur5")
else:
    print("dur4 is not <= than dur5")
if dur4 == dur5:
    print("dur4 is equal to dur5")
else:
    print("dur4 is not equal to dur5")
if dur4 > dur5:
    print("dur4 is > than dur5")
else:
    print("dur4 is not > than dur5")
if dur4 < dur5:
    print("dur4 is < than dur5")
else:
    print("dur4 is not < than dur5")
if durE == dur4:
    print("durE is == to dur4")
else:
    print("durE is not == to dur4")
if durE != dur4:
    print("durE is not == to dur4")
else:
    print("durE is == to dur4")                   
dur6 = TimeSpan(9, 78, -7)
print(dur6)
print(dur6.get_hours(), dur6.get_minutes(), dur6.get_seconds())
dur6 = -dur6
print(dur6)
print("^ neg should be 6, -18, -9")

