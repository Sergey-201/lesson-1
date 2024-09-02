text = 'Python Community'

delete = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

cleaned_text = ''.join(i for i in text if i not in delete)

new_text = cleaned_text.split()

capitalized_new_text = [word.capitalize() for word in new_text]

hashtag = '#' + ''.join(capitalized_new_text)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
#####
text = 't!e@s#t t%e^s&t'

delete = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

cleaned_text = ''.join(i for i in text if i not in delete)

new_text = cleaned_text.split()

capitalized_new_text = [word.capitalize() for word in new_text]

hashtag = '#' + ''.join(capitalized_new_text)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)