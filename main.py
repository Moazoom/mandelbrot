# Mandelbrot fractal
from PIL import Image
import timeit

# code from c++
import main

# image size
imgx = 1000
imgy = 1000
image = Image.new("RGB", (imgx, imgy))

def mandelbrot():
    # drawing area, a bit off center
    xa = -0.8
    xb = -0.78
    ya = 0.17
    yb = 0.15

    # max iterations allowed    
    maxIt = 255

    for y in range(imgy):
        # getting the y coord to calculate
        zy = y * (yb - ya) / (imgy - 1)  + ya

        for x in range(imgx):
            # getting the x coord to calculate
            zx = x * (xb - xa) / (imgx - 1)  + xa

            z = zx + zy * 1j
            c = z

            for i in range(maxIt):
                if abs(z) > 2.0: break
                z = z * z + c

            image.putpixel((x, y), (i, i, i))

    image.show()

def mandelbrot_but_fast():
    # drawing area, a bit off center
    xa = -0.8
    xb = -0.78
    ya = 0.17
    yb = 0.15

    # max iterations allowed    
    maxIt = 255

    for y in range(imgy):
        # getting the y coord to calculate
        zy = y * (yb - ya) / (imgy - 1)  + ya

        for x in range(imgx):
            # getting the x coord to calculate
            zx = x * (xb - xa) / (imgx - 1)  + xa

            z = zx + zy * 1j
            c = z

            i = main.iterate(maxIt, z, c)

            image.putpixel((x, y), (i, i, i))

    image.show()

print("time taken: "+ str(timeit.timeit(mandelbrot, number=1)) + "seconds")
print("time taken: "+ str(timeit.timeit(mandelbrot_but_fast, number=1)) + "seconds")
