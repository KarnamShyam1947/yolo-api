import base64


encoded = "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"
def encode_image(img_path):
    b64_encoded = ''
    with open(img_path, 'rb') as f:
        b64_encoded = base64.b64encode(f.read())
        # print(b64_encoded)

    return b64_encoded

def decode_image(encoded_image, output_path):
    with open(output_path, 'wb') as file:
        file.write(base64.b64decode(encoded_image))

def main():
    img_path = 'images/test5.jpg'
    encoded_image = encode_image(img_path)
    
    output_path = 'decoded_image.jpeg'
    decode_image(encoded, output_path)

if __name__ == '__main__' : 
    main()