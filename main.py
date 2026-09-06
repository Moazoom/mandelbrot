# Mandelbrot fractal
from PIL import Image
import timeit

# drawing area, a bit off center
xa = -0.8
xb = -0.78
ya = 0.17
yb = 0.15

# max iterations allowed
maxIt = 255

# image size
imgx = 1000
imgy = 1000
image = Image.new("RGB", (imgx, imgy))

def mandelbrot():
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

            #if (i < 250): image.putpixel((x, y), (0,0,0))
            #else: image.putpixel((x, y), (255, 255, 255))
            image.putpixel((x, y), (i, i, i))
            #image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

print("time taken: "+ str(timeit.timeit(mandelbrot, number=1)) + "seconds")

image.show()