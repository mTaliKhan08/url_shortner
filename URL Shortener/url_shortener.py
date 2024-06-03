import pyshorteners
import validators

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

def main():
    print("Welcome to the URL Shortener")

    while True:
        long_url = input("Enter the URL to shorten (or type 'exit' to quit): ").strip()

        if long_url.lower() == 'exit':
            break

        if not validators.url(long_url):
            print("Invalid URL. Please enter a valid URL.")
            continue

        try:
            short_url = shorten_url(long_url)
            print(f"Shortened URL: {short_url}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
