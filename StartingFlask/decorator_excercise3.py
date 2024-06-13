class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


new_user = User("Taha")
print(new_user.is_logged_in)


def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("This user is not Logged in, thus not allowed to create a blog post")

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


create_blog_post(new_user)
new_user.is_logged_in = True
create_blog_post(new_user)
