from PIL import Image
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

image_dir = input("Please enter the path to the directory containing the images: ").strip()

if not os.path.isdir(image_dir):
    print(f"The directory {image_dir} does not exist.")
else:
    image_files = []
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_files.append(os.path.join(image_dir, filename))
    if image_files:
        output_path = 'output.pdf'
        c = canvas.Canvas(output_path, pagesize=letter)
        for image_file in image_files:
            img = Image.open(image_file)
            img_width, img_height = img.size
            aspect_ratio = img_height / img_width

            c.setPageSize((img_width, img_height))
            c.drawImage(image_file, 0, 0, img_width, img_height)
            c.showPage()
        
        c.save()
        print('PDF created successfully!')
        print('\nThank you for using this script!')
        print('Check out my GitHub: https://github.com/Praga866')
        
    else:
        print('No images found to create PDF.')
