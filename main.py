import os

#sends message word by word (separate text per word)
def get_words(file_path):
    words = []
    with open(file_path, 'r') as f:
        for line in f:
            # reading each word
            for word in line.split():
                # displaying the words
                words.append(word)
    return words


#sends message line by line
def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text


def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))


if __name__ == '__main__':
    # put your phone number into the string!
    # if your number is (123)456-7890, the next line should look like this: phone_number = '1234567890'

    phone_number2 = ''
    words = get_words('miracle.txt')
    for word in words:
        send_message(phone_number2, word)
