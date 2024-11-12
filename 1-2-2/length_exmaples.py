#list of items
animels_list = ["dog", "cat", "mouse", "bird", "monkey", "honeybadger", "cheetah", "deer"]

index = 0
while (index < len(animels_list)):
    if(index == 3):
        animels_list[3] = "dog"
    print(animels_list[index])
    index += 1
