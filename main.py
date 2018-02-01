# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:35:21 2017

@author: Zheng Xin
"""

"""
This is used to clean text with special symbols, expecially for tweets.

Input: text file in directory
Output: cleaned text with the same format as input data in new folder.
"""
import os
import argparse
import cPickle

from clean import clean_text


parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", help='Input directory')
parser.add_argument("--output_dir", help='Output directory')
parser.add_argument("--binary", default=False, help='Output data is binary format or not')
parser.add_argument("--rm_retweet", default=False, help='Remove "retweet" words in text')
parser.add_argument("--rm_hashtag_sign", default=False, help='Remove hashtag sign #')
parser.add_argument("--rm_account_sign", default=False, help='Remove account sign @')
parser.add_argument("--rm_account", default=False, help='Remove account, e.g. @cnn')
parser.add_argument("--rm_urls", default=False, help='Remove urls')
args = parser.parse_args()


def writeFile(text, out):
    output = ''
    for line in text:
        output += line + '\n'
    output = output.strip()
    out.write(output)
    out.close()


def Data(file_in, file_out):
    text = []
    for line in file_in:
        text.append(line)
    # -- Clean text --
    cleaned_text = clean_text(text, args)

    out = open(file_out, 'wb')
    if args.binary == "True":
        cPickle.dump(cleaned_text, out)
    else:
        writeFile(cleaned_text, out)


# Reading files from directory
def File():
    input_dir = args.input_dir
    output_dir = args.output_dir
    for filename in sorted(os.listdir(input_dir)):
        abs_file = os.path.join(input_dir, filename)
        print 'Reading file ', abs_file
        if os.path.isfile(abs_file):
            file_in = open(abs_file, 'r')
            file_out = os.path.join(output_dir, filename)
            Data(file_in, file_out)
            print '==== Data cleaning for {} is done! === '.format(filename)



# -- Main --
if __name__ == '__main__':
    # Reading files from directory and parse data into required format
    File()
