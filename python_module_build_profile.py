# 8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                              location ='princeton',
                              field='physics')

print(user_profile)

my_user_profile = build_profile('michael', 'jones',
                                location='london',
                                field='computer science/AI',
                                current_learning='python',
                                passion='music')