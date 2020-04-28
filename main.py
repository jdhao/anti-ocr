import numpy as np
from PIL import Image, ImageDraw, ImageFont


def main():
    text = "联系我们请不要犹豫，发给我们你的问题，评论和建议－我们会认真阅读每封邮件，期待着您的回复。 很抱歉，目前我们只能回复用英文书写的消息。support@16personalities.com"

    print(f"text length: {len(text)}")
    char_num_per_slope = 20
    font_size = 20
    text_len = len(text)

    one_slope_x = char_num_per_slope * font_size

    m = np.pi / (2*one_slope_x)
    k = char_num_per_slope * font_size

    x_max = np.ceil(text_len / char_num_per_slope) * one_slope_x
    x_min = 0

    x_coord = np.linspace(x_min, x_max, text_len)
    y_coord = k * np.sin(m * x_coord)

    x_offset = 50
    x_coord = [x+x_offset for x in x_coord]
    print(max(y_coord))

    ratio = 1.1
    y_offset = np.abs(max(y_coord)) * ratio
    print(y_offset)
    y_coord = [y_offset-x for x in y_coord]
    print(min(y_coord))

    coord = list(zip(x_coord, y_coord))
    print(len(coord))

    width = int(max(x_coord)*ratio)
    h_offset = 100
    height = int(max(y_coord)) + h_offset

    img = Image.new("RGB", size=(width, height), color=(255, 255, 255))

    text_color = (255, 0, 0)
    font = ImageFont.truetype("simhei.ttf", font_size)
    drawer = ImageDraw.Draw(img)
    for point, char in zip(coord, text):
        print(point, char)
        drawer.text(point, char, font=font, fill=text_color)

    img.show()


if __name__ == "__main__":
    main()
