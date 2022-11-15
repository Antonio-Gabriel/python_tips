if __name__ == "__main__":    
    username, email = 'António Gabriel', 'antoniogabriel@gmail.com'

    if user := username or email:
        print(user)
        print('Success')
    else:
        print('No user found...')
