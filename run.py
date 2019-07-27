from twitterbotpython import TwitterBot


if __name__ == "__main__":
    twi = TwitterBot()
    print("Starting")
    choices = {
        1: twi.likebykeyword,
        10: quit
    }

    choices[int(1)]()