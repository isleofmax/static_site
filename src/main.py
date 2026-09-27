from textnode import TextNode, TextType


def main():
    txt = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev") 
    print(txt)


if __name__ == "__main__":
    main()
