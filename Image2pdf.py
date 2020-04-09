import os
from PIL import Image

is_save_once = False
list_of_name = None
index = 0

home = os.path.expanduser("~")
path_to_comics = home + '/Downloads/Comics'
save_path = home + '/Downloads/in_pdf'


def save_image_pdf(name, image_directory, list_of_images):
    image_list = []
    list_of_images.sort()
    for x in range(0, len(list_of_images)):
        complete_image_directory = image_directory + "/" + list_of_images[x]
        image = Image.open(complete_image_directory)
        image_list.append(image)
    pdf_directory = save_path + "/" + name + ".pdf"
    image_list[0].save(pdf_directory, save_all=True, append_images=image_list[1:])


for root, d_names, f_names in os.walk(path_to_comics):
    if not is_save_once:
        is_save_once = True
        list_of_name = d_names
    elif index < len(list_of_name):
        print(list_of_name[index] + " has " + str(len(f_names)) + " elements.")
        if not f_names:
            index = index + 1
            continue
        save_image_pdf(list_of_name[index], root, f_names)
        print("Comics number = " + str(index + 1) + ", name = " + list_of_name[index] + ".pdf, is Finished!!\n")
        index = index + 1
