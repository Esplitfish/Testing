from PIL import Image
import io

# Load your Little Mac stock icon image
img = Image.open("611ac089-6231-4717-a62d-2a8cb4913232.png").convert("RGBA")

# Create a letter-size page (8.5 x 11 inches at 300 DPI)
dpi = 300
page_width, page_height = int(8.5 * dpi), int(11 * dpi)

# Create a transparent canvas for the page
canvas = Image.new("RGBA", (page_width, page_height), (255, 255, 255, 0))

# Scale the icon proportionally to about half the page width
target_width = page_width // 2
scale_factor = target_width / img.width
target_height = int(img.height * scale_factor)

# Center the image
x = (page_width - target_width) // 2
y = (page_height - target_height) // 2

# Resize and paste onto canvas
resized_img = img.resize((target_width, target_height), Image.LANCZOS)
canvas.paste(resized_img, (x, y), resized_img)

# Save as PDF (transparent)
canvas.save("LittleMac_centered.pdf", format="PDF", resolution=dpi)

print("✅ PDF created: LittleMac_centered.pdf")