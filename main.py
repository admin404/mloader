import validators


class URL:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        validation = validators.url(self.url)
        if validation:
            return validation
        else:
            return "URL Not Correct"


def main():
    url_validity = URL("https://google.com").check_url()
    # url_validity = URL("").check_url()
    print(url_validity)


if __name__ == "__main__":
    main()
