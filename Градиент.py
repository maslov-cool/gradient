from PIL import Image


def gradient(color):
    im = Image.new('RGB', (512, 200), (0, 0, 0))
    pixels = im.load()
    cnt = 0
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            if color.upper() == 'R':
                pixels[i, j] = int(r + cnt), 0, 0
            elif color.upper() == 'B':
                pixels[i, j] = 0, 0, int(b + cnt)
            else:
                pixels[i, j] = 0, int(g + cnt), 0
        cnt += 0.5

    im.save('res.png')


gradient('R')
