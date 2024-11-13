from PIL import Image
import os
def main():
    output_dir = "images"
    path = input("What file would you like to convert?\n")
    width = int(input("at what resolution (single number, used for height and width)\n"))
    height = width
    os.makedirs(output_dir, exist_ok=True)
    with open(path, 'rb') as file:
        raw_data = file.read()
    header = f"<FILE:{path}>".encode('utf-8')
    footer = f"</FILE:{path}>".encode('utf-8')
    data = header + raw_data + footer
    split_data = []

    # Determine the total number of chunks
    total_chunks = (len(data) + (width * height * 3 -1)) // (width * height * 3)

    # Calculate the number of digits required to represent the total number of chunks
    num_digits = len(str(total_chunks))

    for i in range(0, len(data), width * height * 3):
        chunk = data[i:i + width * height * 3]
        split_data.append(chunk)
        

    for i, chunk in enumerate(split_data):
        image = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                index = (y * width + x) * 3
                r = 0 if index >= len(chunk) else chunk[index]
                g = 0 if index + 1 >= len(chunk) else chunk[index + 1]
                b = 0 if index + 2 >= len(chunk) else chunk[index + 2]
                image.putpixel((x, y), (r, g, b))
        
        # Format the index with leading zeros
        index_formatted = str(i+1).zfill(num_digits)
        
        image.save(f"images/{path}_{index_formatted}.png")

if __name__ == "__main__":
    main()