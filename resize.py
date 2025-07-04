from PIL import Image
def make_square(input_path, output_path, size=1024):
    img = Image.open(input_path).convert("RGBA")
    # Make canvas square
    max_side = max(img.size)
    square_img = Image.new("RGBA", (max_side, max_side), (255, 255, 255, 0))
    square_img.paste(img, ((max_side - img.width) // 2, (max_side - img.height) // 2))
    # Resize to target size
    square_img = square_img.resize((size, size))
    square_img.save(output_path)

make_square("outputs/Saree_4_clean.png", "outputs/Saree_4_clean_resize.png")

