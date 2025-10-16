from textnode import TextNode, TextType

def main():
    textnode1 = TextNode("hello", TextType.BOLD)
    print(repr(textnode1))


if __name__ == "__main__":
    main()
