from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


output = Path(__file__).resolve().parents[1] / "assets" / "image-test.png"
output.parent.mkdir(parents=True, exist_ok=True)

image = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image)
draw.rounded_rectangle((24, 24, 176, 176), radius=12, fill="#1976D2")

font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 88)
text = "7"
bbox = draw.textbbox((0, 0), text, font=font)
x = (200 - (bbox[2] - bbox[0])) / 2
y = (200 - (bbox[3] - bbox[1])) / 2 - bbox[1]
draw.text((x, y), text, fill="white", font=font)

image.save(output)
print(output)

