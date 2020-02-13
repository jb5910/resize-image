from PIL import Image

Link = input("Please enter the path to an image: ")
image = Image.open(Link)
new_image = image.resize((400, 400))
image.close()
new_image.save(Link)
new_image.close()
