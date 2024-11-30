import numpy as np
# import torch


if __name__ == "__main__":

    # Image

    image_width = 256
    image_height = 256

    # render code

    with open("fade.ppm", "w") as f:
        header_string = f"P3\n{image_width} {image_height}\n255\n"
        f.write(header_string)

        # dumb method
        #for j in range(image_height):
            #for i in range(image_width):
                #r = int(255.999 * i / (image_width - 1.0))
                #g = int(255.999 * j / (image_height - 1.0))
                #b = int(255.99 * 0.0)
                #pixel_string = f"{r} {g} 0\n"
                #f.write(pixel_string)

        
        # go blazingly fast (not correct at the moment):
        r = np.linspace(0, 256, 256)/(image_width - 1.0) * 255.999
        g = np.linspace(0, 256, 256)/(image_width - 1.0) * 255.999

        print(r.shape)
        R, G = np.meshgrid(r, g)
        
        r_row = R.flatten()
        g_row = G.flatten()

        for row in range(256 * 256):
            pixel_string = f"{int(r_row[row])} {int(g_row[row])} 0\n"
            f.write(pixel_string)

    print("Image generated!")
