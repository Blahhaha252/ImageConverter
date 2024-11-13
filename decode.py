from PIL import Image
import os
def main():
    output_dir = "files"
    path = input("What is the original file name? (if going based on images, provide name of it, minus the _<number>.png)\n")
    num_digits = int(input("What is the length of the digits of the images? (example) <path>_001.png (3 digits)\n"))

    def find_last_nonzero_index(data):
        for i in range(len(data) - 1, -1, -1):
            if data[i] != 0:
                return i
        return -1

    total_file_data = bytearray()
    index = 1
    print(f"{path}_{str(index).zfill(num_digits)}")
    while os.path.exists(f"images/{path}_{str(index).zfill(num_digits)}.png"):
        print(f"Processing image {index}")
        image = Image.open(f"images/{path}_{str(index).zfill(num_digits)}.png")
        pixels = list(image.getdata())
        for pixel in pixels:
            total_file_data.extend(pixel)
        index += 1

    header = f"<FILE:{path}>".encode('utf-8')
    footer = f"</FILE:{path}>".encode('utf-8')
    header_index = total_file_data.find(header)
    footer_index = total_file_data.rfind(footer)
    new_data = bytearray()

    if header_index != -1 and footer_index != -1:
        new_data = total_file_data[header_index + len(header):footer_index]
    else:
        print("Header or footer not found")

    last_nonzero_index = find_last_nonzero_index(new_data)
    if last_nonzero_index != -1:
        new_data = new_data[:last_nonzero_index + 1]
        
    os.makedirs(output_dir, exist_ok=True)
    with open(f"files/{path}", 'wb') as file:
        file.write(new_data)
if __name__ == "__main__":
    main()