from blog.posts.posts import Post


def main():
    print("I'm a command!")
    name = input('Please type your name')
    print(f"Hi {name}")
    ps = Post('title_name', 'author_name', 'text_name')
    ps.some_function()
    ps.new_function()


if __name__ == '__main__':
    main()
