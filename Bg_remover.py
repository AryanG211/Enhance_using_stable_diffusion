from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    with open(input_path, "rb") as inp_file:
        input_data = inp_file.read()
        output_data = remove(input_data)
    with open(output_path, "wb") as out_file:
        out_file.write(output_data)

# Example Usage
remove_background("inputs/model1.png", "outputs/model1_clean.png")
