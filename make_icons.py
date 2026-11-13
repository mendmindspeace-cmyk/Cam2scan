from PIL import Image, ImageDraw


def make(size, maskable, path):
    S = size * 4
    im = Image.new("RGBA", (S, S), (26, 115, 232, 255))
    if not maskable:
        mask = Image.new("L", (S, S), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
        bg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        bg.paste(im, (0, 0), mask)
        im = bg
    d = ImageDraw.Draw(im)
    k = 0.58 if maskable else 0.72
    ch = S * k
    cw = ch * 0.74
    cx = cy = S / 2
    x0, y0, x1, y1 = cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2
    fold = cw * 0.3
    d.polygon([(x0, y0), (x1 - fold, y0), (x1, y0 + fold), (x1, y1), (x0, y1)], fill=(255, 255, 255, 255))
    d.polygon([(x1 - fold, y0), (x1, y0 + fold), (x1 - fold, y0 + fold)], fill=(196, 212, 240, 255))
    for i, frac in enumerate((0.40, 0.55, 0.70)):
        y = y0 + ch * frac
        end = x1 - cw * (0.14 if i < 2 else 0.40)
        d.rounded_rectangle([x0 + cw * 0.14, y, end, y + ch * 0.045], radius=int(ch * 0.02), fill=(170, 186, 214, 255))
    # scan bar
    yb = y0 + ch * 0.30
    d.rounded_rectangle([x0 - cw * 0.10, yb, x1 + cw * 0.10, yb + ch * 0.05], radius=int(ch * 0.025), fill=(255, 152, 0, 255))
    im = im.resize((size, size), Image.LANCZOS)
    im.save(path)


make(192, False, "icon-192.png")
make(512, False, "icon-512.png")
make(512, True, "icon-512-maskable.png")
print("ok")
