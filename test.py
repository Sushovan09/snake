snake_array = [[25,0],[0,0],[25,0],[0,0],[25,0],[0,0]]

snake_array.append([0,0])
snake_array[len(snake_array)-1][0] = snake_array[len(snake_array)-2][0]
snake_array[len(snake_array)-1][1] = snake_array[len(snake_array)-2][1]
print(snake_array,'01')


for i in range(len(snake_array)-1):
    s = len(snake_array)-1
    snake_array[s-i][0] = snake_array[s-i-1][0]
    snake_array[s-i][1] = snake_array[s-i-1][1]
print(snake_array,'02')




snake_array.append(snake_array[len(snake_array)-1])
print(snake_array,"11")


for i in range(len(snake_array)-1):
    s = len(snake_array)-1
    snake_array[s-i][0] = snake_array[s-i-1][0]
    snake_array[s-i][1] = snake_array[s-i-1][1]
print(snake_array,"12")