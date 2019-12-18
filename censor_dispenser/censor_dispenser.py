# These are the emails you will be censoring. The open() function is opening
# the text file that the emails are contained in and the .read() method
# is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]


def censor(phrase, stop_word='learning algorithms'):
    position = phrase.find(stop_word)
    return phrase.replace(
        phrase[position:position+len(stop_word)], "#"*len(stop_word))
# print(censor(email_two))


def censor_list(phrase, stop_words=[]):
    phrase_split = phrase.split(' ')
    phrase_split = [x.replace(
        x, '#'*len(x)) if x in stop_words else x for x in phrase_split]

    return ' '.join(phrase_split)


print(censor_list(email_two, proprietary_terms))
