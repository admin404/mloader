import validators


class URL:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        validation = validators.url(self.url)
        if validation:
<<<<<<< HEAD
            return validation
        else:
            return "URL Not Correct"


def main():
    url_validity = URL("https://google.com").check_url()
    # url_validity = URL("").check_url()
=======
            return True
        else:
            return False


def main():
    url_validity = URL("https://www.google.com").check_url()
>>>>>>> 68e3d6f456754c3a0ad598849af0b7afcfa2ec5f
    print(url_validity)


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 68e3d6f456754c3a0ad598849af0b7afcfa2ec5f
