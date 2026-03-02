from PIL import Image, ImageEnhance
from os import path


def main():

    frames = []

    gif_file = gif_creater(frames)
    print(gif_file)

def open_image():
    load_image = path.join("files", "a.JPG")

    image = Image.open(load_image)

    return image

def gif_creater(frames):

    for value in range(7):
        enhancer = ImageEnhance.Contrast(open_image())
        frame = enhancer.enhance(0.6+value*0.3)
        frames.append(frame)

        frames[0].save("newImage.gif",
                       save_all = True,
                       append_images= frames[1:],
                       duration = 300,
                       loop = 0)
    return "gif file created "




if __name__ == "__main__":
    main()