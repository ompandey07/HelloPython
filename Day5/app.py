# ANYTHING THAT IMPORTED TO USE IN CODE IS CALLED A MODULE , PACKAGE IS A COLLECTION OF MODULES

from rembg import remove
from PIL import Image
import io

# Open the original image
input_path = "input_image.png"
output_path = "output_image.png"

with open(input_path, "rb") as i:
    input_data = i.read()

# Remove background
output_data = remove(input_data)

# Save the result
output_image = Image.open(io.BytesIO(output_data))
output_image.save(output_path)
