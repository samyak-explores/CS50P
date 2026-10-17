def main():
    text = input("File Name: ").strip().lower()

    print(type_identifier(text))

def type_identifier(text):

        if text.endswith(".gif"):
                return "image/gif"
        elif text.endswith(".jpg"):
                return "image/jpeg"
        elif text.endswith(".jpeg"):
                return "image/jpeg"
        elif text.endswith(".png") :
                return "image/png"
        elif text.endswith(".pdf") :
                return "application/pdf"
        elif text.endswith(".txt") :
                return "text/txt"
        elif text.endswith(".zip") :
                return "application/zip"
        else:
               return "application/octet-stream"

main()
