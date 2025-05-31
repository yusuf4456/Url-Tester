from analyzer import analyze_url

if __name__ == "__main__":
    url = input("URL: ")
    result = analyze_url(url)
    print("\nSonuç:", result["verdict"])
