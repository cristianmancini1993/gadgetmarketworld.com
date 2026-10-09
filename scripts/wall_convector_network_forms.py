# -*- coding: utf-8 -*-
"""Adrice Network form credentials — Heaterax / AirCurtain GEO offers."""
UID = "018e3961-c73a-7965-8fc1-b1d91c869a42"
WEBHOOK = "https://hook.eu2.make.com/i7pmea9fmpnepx94e5z6dxfwvl1bnnlh"
ACTION = "https://offers.adricenetwork.com/forms/html/"
SCRIPT = "https://offers.adricenetwork.com/forms/html/js-v2/"

# lp + form _key: fill when Adrice provides (offer id is set in each landing HTML)
FORMS: dict[str, dict[str, str]] = {
    "1244": {"lp": "1244", "key": ""},
    "1673": {"lp": "1673", "key": ""},
    "1739": {"lp": "1739", "key": ""},
    "2283": {"lp": "2283", "key": ""},
    "2285": {"lp": "2285", "key": ""},
    "2919": {"lp": "2919", "key": ""},
}

CPA: dict[str, float] = {
    "1244": 14.0,
    "1673": 13.0,
    "1739": 13.0,
    "2283": 13.0,
    "2285": 14.0,
    "2919": 14.0,
}
