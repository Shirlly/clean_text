# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:41:06 2016

@author: Zheng Xin
"""

import re


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# -- Remove punctuations except: e.g. "'" in "don't"; "-" in "pre-train"
def remove_pun(text):
    if type(text) is str and len(text.split()) > 0:
        text = text.decode('iso-8859-1').encode('utf-8').strip()
        word = text.split()
        __sen = []
        for w in word:
            if w.endswith((',', '.', ';', ':', '?', '!', ')', '>', '\'', '"', '&', '-', '|')):
                w = w[:-1]

            if w.startswith((',', '.', ';', ':', '?', '!', '(', '<', '\'', '"', '&', '-', '|')):
                w = w[1:]

            if w.strip():
                __sen.append(w)

        __msg = ' '.join(__sen)
        __msg = re.sub(r"\(", ' ', __msg)
        __msg = re.sub(r"\)", ' ', __msg)
        __msg = re.sub(r"\[", ' ', __msg)
        __msg = re.sub(r"\]", ' ', __msg)
        __msg = re.sub(r"<", ' ', __msg)
        __msg = re.sub(r">", ' ', __msg)
        __msg = re.sub(r",", ' ', __msg)
        __msg = re.sub(r";", ' ', __msg)
        __msg = re.sub(r"!", ' ', __msg)
        __msg = re.sub(r"$", ' ', __msg)
        __msg = re.sub(r"&", ' ', __msg)
        __msg = re.sub(r"\*", ' ', __msg)
        __msg = re.sub(r"\+", ' ', __msg)
        __msg = re.sub(r"_{2,}", ' ', __msg)
        __msg = re.sub(r"={1,}", ' ', __msg)
        __msg = re.sub(r"-{2,}", ' ', __msg)
        __msg = re.sub(r"~{1,}", ' ', __msg)
        __msg = re.sub(r"\.{2,}", ' ', __msg)
        __msg = re.sub(r"\?{1,}", ' ', __msg)
        __msg = re.sub(r"\{1,}", ' ', __msg)
        __msg = re.sub(r"\"", ' ', __msg)
        __msg = re.sub(r"/", ' ', __msg)
        __msg = re.sub(r"\\", ' ', __msg)
        word = __msg.split()
        __sen = []
        for w in word:
            if w.endswith((',', '.', ';', ':', '?', '!', ')', '>', '\'', '"', '&', '-', '|')):
                w = w[:-1]
            if w.startswith((',', '.', ';', ':', '?', '!', '(', '<', '\'', '"', '&', '-', '|')):
                w = w[1:]
            if w.strip():
                __sen.append(w)

        text = ' '.join(__sen)

    else:
        print text
    return text


# -- Remove urls --
def remove_urls(text):
    urlRegex1 = "^(http|https|ftp|file)://.*"
    urlRegex2 = ".*[/]*.*(.html)"
    left_word = []
    for w in text.split():
        if isEnglish(w) and not (re.match(urlRegex1, w, re.M | re.I)
                                 or re.match(urlRegex2, w, re.M | re.I)):
            left_word.append(w)
    text = " ".join(left_word)
    return text

# -- Remove following automatically generated symbols --
def remove_retweet_sign(text):
    text = re.sub(r"Retweet", "", text)
    text = re.sub(r"retweet", "", text)
    text = re.sub(r"gf", "", text)
    text = re.sub(r"gt", "", text)
    text = re.sub(r"RT", "", text)
    text = re.sub(r"rt", "", text)
    text = text.strip()
    return text


# -- Remove account --
def remove_account(text):
    words = text.split()
    left_word = [word for word in words if "@" not in word]
    text = " ".join(left_word)
    return text


# -- Process various cleaning for input text --
def clean_text(text_iterator, args):
    clean_text = []
    for text in text_iterator:
        if text.strip():
            if args.rm_retweet == 'True':
                text = remove_retweet_sign(text)

            if args.rm_hashtag_sign == 'True':
                text = re.sub(r"#", "", text)

            if args.rm_account_sign == 'True':
                text = re.sub(r"@", "", text)
            elif args.rm_account == 'True':
                text = remove_account(text)

            if args.rm_urls == "True":
                text = remove_urls(text)

            text = remove_pun(text)
            clean_text.append(text)
        else:
            clean_text.append(text)
    return clean_text
