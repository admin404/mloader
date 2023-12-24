import validators


class URL:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        validation = validators.url(self.url)
        if validation:
            return True
        else:
            return False


def main():
    url_validity = URL("https://www.google.com").check_url()
    print(url_validity)


if __name__ == "__main__":
    main()