WORDS_BANK=[]
def load_data():
    print('loading...⏳')
    try:
        with open('words_bank.txt','r') as f:
            big_text=f.read()
            words=big_text.split('\n')
            for i in range(0,len(words),2):
                WORDS_BANK.append({'en':words[i],'pr':words[i+1]})
        print('loaded📑')
    except:
        print("An Error Occurred While Opening File!🚫")

def translate_en2pr(input_text):
    user_words = input_text.split(' ')
    output_text = ""
    for uw in user_words:
        for word in WORDS_BANK:
            if uw == word['en']:
                output_text += word['pr'] + ' '
                break
        else:
            output_text += uw + ' '
    return output_text

def translate_pr2en(input_text):
    user_words = input_text.split(' ')
    output_text = ""
    for uw in user_words:
        for word in WORDS_BANK:
            if uw == word['pr']:
                output_text += word['en'] + ' '
                break
        else:
            output_text += uw + ' '
    return output_text

def Add_new_word():
    while True:
        e_word = input('English : ')
        check = False
        for ew in WORDS_BANK:
            if e_word == ew['en']:
                check = True
                print('This word is already stored in the list📄')
        if check == False:
            break

    p_word = input('Persian : ')
    WORDS_BANK.append({'en': e_word, 'pr': p_word})

def save():
    with open("words_bank.txt","w") as f:
        for word in WORDS_BANK:
            f.write(word['en']+'\n')
            f.write(word['pr'] + '\n')
    print('saved📦')        

load_data()
while True :
    print('choose : \n 1.translate english to persian\n 2.translate persian to english\n 3.add new word\n 4.exit ')
    ch=int(input())
    if ch==1:
        c=int(input('If your text is longer than one sentence, press 1, otherwise 2  \n'))
        if c==1:
            user_text = input('Please write your text : ')
            user_sentence = user_text.split('.')
            for sen in user_sentence:
                output_text = translate_en2pr(user_text)
            print(output_text)

        elif c==2:
            user_text = input('Please write your text : ')
            output_text = translate_en2pr(user_text)
            print(output_text)

    elif ch==2:
        c = int(input('If your text is longer than one sentence, press 1, otherwise 2  \n'))
        if c == 1:
            user_text = input('Please write your text : ')
            user_sentence = user_text.split('.')
            for sen in user_sentence:
                output_text = translate_pr2en(user_text)
            print(output_text)

        elif c == 2:
            user_text = input('Please write your text : ')
            output_text = translate_pr2en(user_text)
            print(output_text)

    elif ch==3:
        Add_new_word()

    elif ch==4:
        s=input('do you wanna save📥 y/n :')
        if s=='y':
            save()
            exit()
        elif s=='n':
            exit()
