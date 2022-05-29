if __name__ == '__main__':
    try:
        a = 1 / 0
    except:
        print("Division by zero")

    try:
        x = 1
    finally:
        print("finally")
