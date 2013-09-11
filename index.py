import urllib2
from HTMLParser import HTMLParser
import re
from random import randint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        pass
    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        pass
    def handle_data(self, data):
        # remove whitespace, short words, and uppercase
        word = re.sub(r"\W", "", data)
        if (len(word) > 1 and word.islower()):
            self.verbs.append(word)
            #print "Encountered a word: ", word


#### Helper Functions

# Takes a list of words and filters out short words and uppercase
def clean_list(raw):
    clean = []
    for el in raw:
        if(len(el) > 1 and el.islower()):
            clean.append(el)
    return clean



#### Verbs

res = urllib2.urlopen("http://www.webresume.com/resumes/verbs.shtml").read()

f = open('verbs.html', 'w')
f.write(res)
f.close()

verbs = open('verbs.html', 'r').read()

parser = MyHTMLParser()
parser.verbs = []
parser.feed(verbs)


#### Adjectives

adj_text = open('adj.txt', 'r').read()

adjs_raw_list = adj_text.split()

adjs = clean_list(adjs_raw_list)

        
#### Nouns

nouns_text = open('noun.txt', 'r').read()

nouns_raw_list = nouns_text.split()

nouns = clean_list(nouns_raw_list)


#### Parables

## Simple Version, outputs a parable in format (verb/adj/adj/noun)
"""
for verb in parser.verbs:
    r1 = randint(0, len(adjs) -1)
    r2 = randint(0, len(adjs) -1)
    r3 = randint(0, len(nouns) -1)
    parable = "A computer has never %s %s %s %s \n" % (verb, adjs[r1], adjs[r2], nouns[r3])
    p.write(parable)
p.close()
"""

## Advanced Version, outputs a parable in format(verb/adj*n/noun)
## allows user to manipulate how many adjectives in a row

# creates parables for every verb, outputs to parables.txt
def gen_parables(adj_number):
    p = open('parables.txt', 'w')
    for verb in parser.verbs:
        p.write(gen_parable(verb, adj_number))
    p.close()

# creates a parable from a base string and a random phrase
def gen_parable(verb, adj_number):
    args = []
    args.append(verb)
    for i in range (0, adj_number):
        args.append(adjs[randint(0, len(adjs) -1)])
    args.append(nouns[randint(0, len(nouns) -1)])
    parable = "A computer has never " + gen_phrase(*args) + '\n'
    return parable

# efficient string concat for our random phrase
def gen_phrase(*args):
    return ' '.join([arg for arg in args])

gen_parables(2)