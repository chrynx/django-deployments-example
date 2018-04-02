def register(func):
    first = 'ralph'
    last = 'wendt'
    age = 25
    def complete_profile():
        x = func()
        print(x + first + last + str(age))
    return complete_profile

@register
def profile():
    x = 'profile: '
    return x


profile()
