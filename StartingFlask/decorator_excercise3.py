class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


new_user = User("Taha")
print(new_user.is_logged_in)


def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")

create_blog_post(new_user)