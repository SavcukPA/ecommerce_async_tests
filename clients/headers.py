class Headers:

    basic = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
    }

    form_urlencoded = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
    }
