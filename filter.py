# BASIC FITLER APPLICATION
# SEE filter.py -h for more information

# START IMPORTS
from PIL import Image
import math
import random
import argparse
# END IMPORTS

choices = []
for i in range(0,256):
    choices.append(str(i))
choices2 = []
for i in range(0,101):
    choices2.append(str(i))
choices3 = ["horizontal", "vertical", "both"]
#choices3 = []    
#for i in range(0,10001):
#    choices3.append(str(i))

# ADD arguments for command line
parser = argparse.ArgumentParser(description="Filter JPEG images.")
parser.add_argument('-input',help='The JPEG image that is to be filtered.',required=True)
parser.add_argument('-output',help='The file that the filtered image should be saved to.',required=True)
parser.add_argument('-filter',help='The filter that should be applied to the image (gray/sepia/red/orange/yellow/green/cyan/blue/purple/rainbow).',required=False)
parser.add_argument('-invert',help='The flag that inverts an image.',required=False,action='store_true')
parser.add_argument('-bw',help='The flag that converts an image to black/white. (black if pixel argument <= 127 and white if pixel argument is > 127)',required=False,choices=choices)
parser.add_argument('-dither',help='This flag effectively generates white noise. (0-100)',required=False,choices=choices,)
parser.add_argument('-blur',help='Blurs the image via the Guassian blur filter. The blur is input times strong',required=False,)
parser.add_argument('-reflect', help='Reflects the image (horizontal, vertical, both) are options.',required=False,choices=choices3)

args = parser.parse_args()

args = vars(args)

output = args["output"]

image = Image.open(args["input"])

size = image.size

# ALL filters below translate to a specific color palette via focusing specific colors in ( additive color mixing ?)
# ------ START BASE COLOR FILTERS ------ #
def gray_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            new_pixel_value = math.floor((pixel[0] + pixel[1] + pixel[2]) / 3)

            new_pixel = (new_pixel_value, new_pixel_value, new_pixel_value) # add , pixel[3] if using PNGS

            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def sepia_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            new_red = math.floor((pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189))
            new_green = math.floor((pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168))
            new_blue = math.floor((pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131))

            new_pixel = (new_red, new_green, new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def red_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_green = 0
            new_blue = 0

            new_pixel = (pixel[0], new_green, new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def orange_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_green = math.floor(pixel[1] / 2)
            new_blue = 0

            new_pixel = (pixel[0], new_green, new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def yellow_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_green = math.floor(pixel[1])
            new_blue = 0

            new_pixel = (pixel[0], new_green, new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def green_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))

            new_red = 0
            new_blue = 0

            new_pixel = (new_red, pixel[1], new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def cyan_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))

            new_red = 0
            new_blue = pixel[2]

            new_pixel = (new_red, pixel[1], new_blue)
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def blue_filter(image):
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_red = 0
            new_green = 0

            new_pixel = (new_red, new_green, pixel[2])
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def purple_filter(image):

    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_red = pixel[0]
            new_green = 0

            new_pixel = (new_red, new_green, pixel[2])
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

def rainbow_filter(image):
    # ALGO I made for fun. SLOW (probably)
    counter = 0
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))

            if counter == 0:
                new_pixel = (pixel[0],0,0)
                counter += 1
            elif counter == 1:
                new_pixel = (pixel[0],math.floor(pixel[1]/2),0)
                counter += 1
            elif counter == 2:
                new_pixel = (pixel[0],pixel[1],0)
                counter += 1
            elif counter == 3:
                new_pixel = (0,pixel[1],0)
                counter += 1
            elif counter == 4:
                new_pixel = (0,pixel[1],pixel[2])
                counter += 1
            elif counter == 5:
                new_pixel = (0,0,pixel[2])
                counter += 1
            elif counter == 6:
                new_pixel = (pixel[0],0,pixel[2])
                counter = 0

            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")

# ------ END BASE COLOR FILTERS ----- #

def invert_filter(pixel):
    # Simply inverts
    if args["invert"]:
        pixel = (255 - pixel[0],255 - pixel[1],255 - pixel[2])

    return pixel

def black_white_filter(pixel):
    # IF a average of pixel <= args["bw"]: BLACK ELSE: WHITE
    if int(args["bw"]) in range(0,256):
        if math.floor((pixel[0] + pixel[1] + pixel[2])/3) <= int(args["bw"]):
            return (0,0,0)
        return (255,255,255)
    return pixel

def dither(pixel):
    # DITHERS, rest of the algo is under if args["filter"]: around lines 350-380
    dither_change = int(args["dither"])
    Dither = math.floor(random.randint(0,dither_change) - dither_change/2)
    R = pixel[0] + Dither
    if R > 255: R = 255
    if R < 0: R = 0
    G = pixel[1] + Dither
    if G > 255: G = 255
    if G < 0: G = 0
    B = pixel[2] + Dither
    if B > 255: B = 255
    if B < 0: B = 0

    return (R,G,B)
    #dither_multiplier = 1
    #dither_change_range = range(-(math.floor(dither_change*dither_multiplier)), (math.floor((dither_change*dither_multiplier)+1)))

    #current_pixel_gray = math.floor((pixel[0]+pixel[1]+pixel[2])/3)

    #current_pixel_gray = current_pixel_gray + int(current_pixel_gray*(random.choice(dither_change_range)/100))
        
    #if current_pixel_gray > 255:current_pixel_gray = 255
    #if current_pixel_gray < 0:current_pixel_gray = 0


    #new_pixel_color = (current_pixel_gray,current_pixel_gray,current_pixel_gray)


    #print(current_pixel_gray,"     ",new_pixel_gray)
    return new_pixel_color

def blur(image):
    # Blur via increasing kernel size 
    new_image = image
    size_of_kernel = int(args["blur"])
    print(image.getpixel((1198,733)))
    for x in range(size[0]):
        for y in range(size[1]):
            current_pixel = image.getpixel((x,y))
            current_av = [0,0,0]
            count = 0
            numbers = []
            # I dont know why this works
            for x1 in range(size_of_kernel):
                if x - x1 > 0:
                    count += 1
                    new_pixel = image.getpixel((x-x1,y))
                    current_av[0] += new_pixel[0]
                    current_av[1] += new_pixel[1]
                    current_av[2] += new_pixel[2]
                
                if x + x1 < size[0]:
                    count += 1
                    new_pixel = image.getpixel((x+x1,y))
                    current_av[0] += new_pixel[0]
                    current_av[1] += new_pixel[1]
                    current_av[2] += new_pixel[2]
                
                for y1 in range(size_of_kernel):
                    if y - y1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y + y1 < size[1]:
                        count += 1
                        new_pixel = image.getpixel((x,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    
                    if y + y1 < size[1] and x + x1 < size[0]:
                        count += 1
                        new_pixel = image.getpixel((x+x1,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y + y1 < size[1] and x - x1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x-x1,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y - y1 > 0 and x + x1 < size[0]:
                        count += 1
                        new_pixel = image.getpixel((x+x1,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y - y1 > 0 and x - x1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x-x1,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
            count += 1
            current_av[0] = math.floor((current_av[0] + current_pixel[0]) / count)
            current_av[1] = math.floor((current_av[1] + current_pixel[1]) / count)
            current_av[2] = math.floor((current_av[2] + current_pixel[2]) / count)
            count = 0


                    #if count > 60:
                    #    print(len(numbers))

                        #print(numbers)
            new_image.putpixel((x,y),(current_av[0],current_av[1],current_av[2]))
            #print(count)
        print(f"Line {x}/{size[0]} completed!",end='\r')
    print(f"Line {size[0]}/{size[0]} completed!")
    return new_image

def reflect(image):
    new_image = image
    if args["reflect"] in ["horizontal", "both"]:
        for y in range(size[1]):
            left = 0
            right = size[0] - 1
            while (left != right) and (right-left != 1):
                new_pixel = image.getpixel((left,y))
                other_new_pixel = image.getpixel((right,y))

                new_image.putpixel((right,y),new_pixel)
                new_image.putpixel((left,y),other_new_pixel)

                left += 1
                right -= 1
            print(f"Column {y} completed!",end='\r')
    image = new_image
    if args["reflect"] in ["vertical", "both"]:
        for x in range(size[0]):
            left = 0
            right = size[1] - 1
            while (left != right) and (right-left != 1):
                new_pixel = image.getpixel((x,left))
                other_new_pixel = image.getpixel((x,right))

                new_image.putpixel((x,right),new_pixel)
                new_image.putpixel((x,left),other_new_pixel)

                left += 1
                right -= 1
            print(f"Column {x} completed!",end='\r')
        
    return new_image
if args["reflect"]:
    image = reflect(image)
    image.save(output)
if args["blur"]:
    image = blur(image)
    image.save(output)
if args["dither"]:
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            new_pixel = dither(pixel)


            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {x+1}/{size[0]} completed!", end="\r")
    image.save(output)
if args["filter"] == "gray":
    gray_filter(image)
    image.save(output)
elif args["filter"] == "sepia":
    sepia_filter(image)
    image.save(output)
elif args["filter"] == "red":
    red_filter(image)
    image.save(output)
elif args["filter"] == "orange":
    orange_filter(image)
    image.save(output)
elif args["filter"] == "yellow":
    yellow_filter(image)
    image.save(output)
elif args["filter"] == "green":
    green_filter(image)
    image.save(output)
elif args["filter"] == "cyan":
    cyan_filter(image)
    image.save(output)
elif args["filter"] == "blue":
    blue_filter(image)
    image.save(output)
elif args["filter"] == "purple":
    purple_filter(image)
    image.save(output)
elif args["filter"] == "rainbow":
    rainbow_filter(image)
    image.save(output)
if args["bw"]:
    print("Transferring image to Black/White!")
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_red = pixel[0]
            new_green = pixel[1]

            new_pixel = black_white_filter((new_red, new_green, pixel[2]))
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")
    image.save(output)
if args["invert"]:
    print("Inverting!")
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_red = pixel[0]
            new_green = pixel[1]

            new_pixel = invert_filter((new_red, new_green, pixel[2]))
            image.putpixel((x,y),new_pixel)
        print(f"Line {x}/{size[0]} completed!", end="\r")
    print(f"Line {size[0]}/{size[0]} completed!")
    image.save(output)

image.close()
