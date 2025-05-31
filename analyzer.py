import re
import urllib.parse
import tldextract
import socket
import whois

def analyze_url(url):
    result = {
        "url": url,
        "features": {},
        "score": 0,
        "verdict": ""
    }

    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    ext = tldextract.extract(url)
    full_domain = f"{ext.domain}.{ext.suffix}"

    try:
        socket.inet_aton(domain)
        result["features"]["uses_ip"] = True
        result["score"] += 2
    except socket.error:
        result["features"]["uses_ip"] = False

    result["features"]["long_url"] = len(url) > 75
    if result["features"]["long_url"]:
        result["score"] += 1

    suspicious_chars = ["@", "-", "%", "=", "&"]
    result["features"]["suspicious_chars"] = any(c in url for c in suspicious_chars)
    if result["features"]["suspicious_chars"]:
        result["score"] += 1

    result["features"]["uses_https"] = parsed_url.scheme == "https"
    if not result["features"]["uses_https"]:
        result["score"] += 1

    try:
        whois.whois(full_domain)
        result["features"]["whois_found"] = True
    except:
        result["features"]["whois_found"] = False
        result["score"] += 1

    keywords = ["login", "secure", "account", "update", "bank", "verify"]
    result["features"]["has_suspicious_keywords"] = any(k in url.lower() for k in keywords)
    if result["features"]["has_suspicious_keywords"]:
        result["score"] += 1

    if result["score"] >= 4:
        result["verdict"] = "Phishing olabilir"
    elif result["score"] >= 2:
        result["verdict"] = "Şüpheli"
    else:
        result["verdict"] = "Güvenli"

    return result
