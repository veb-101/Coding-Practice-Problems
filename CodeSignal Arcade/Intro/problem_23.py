# https: // app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
'''
Last night you partied a little too hard. Now there's a black and white photo of
you that's about to go viral! You can't let this ruin your reputation, so you
want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm
distorts the input image in the following way: Every pixel x in the output image
has a value equal to the average value of the pixel values from the 3 × 3 square
that has its center at x, including x itself. All the pixels on the border of x
are then removed.

Return the blurred image as an integer, with the fractions rounded down.
Example
For
image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square:
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1.
The border pixels are cropped from the final result.

For
image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]
the output should be

boxBlur(image) = [[5, 4],
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four
integers in the blurred output. To get the first value:
(7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three
integers are obtained the same way, then the surrounding integers are cropped
from the final result.
'''


def boxBlur(image):
    r = []
    for i in range(len(image) - 2):
        r.append([])
        for j in range(len(image[0]) - 2):
            r[i].append(sum(image[i][j:j + 3] + image[i + 1][j:j + 3] + image[i + 2][j:j + 3]) // 9)

    return r


image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

print(boxBlur(image))

image = [[0, 18, 9],
         [27, 9, 0],
         [81, 63, 45]]

print(boxBlur(image))

image = [[36, 0, 18, 9],
         [27, 54, 9, 0],
         [81, 63, 72, 45]]
print(boxBlur(image))


image = [[36, 0, 18, 9, 9, 45, 27],
         [27, 0, 254, 9, 0, 63, 90],
         [81, 255, 72, 45, 18, 27, 0],
         [0, 0, 9, 81, 27, 18, 45],
         [45, 45, 227, 227, 90, 81, 72],
         [45, 18, 9, 255, 9, 18, 45],
         [27, 81, 36, 127, 255, 72, 81]]

print(boxBlur(image))
