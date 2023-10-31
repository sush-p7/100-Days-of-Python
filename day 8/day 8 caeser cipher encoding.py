import art
def caeser(text,shift,operation):
    if operation == 'decode':
        shift *= -1
    message =''
    for i in text:
        if i in letters:
            position = letters.index(i)
            message += letters[position+shift]
        else:
            message+='•'
    print(f'your text will be {message}')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
print(art.logo)
isRunAgain = True
while isRunAgain:
    direction = input('type encode to encode , and decode to decode \n')
    text = input('type your message:\n').lower()
    shift = int(input('Type the shift number\n'))
    if shift>25:
        shift = int(input('shift can not be grater then 25 Re-Type the shift number\n'))
    caeser(text=text, shift=shift, operation=direction)
    yesOrNo = input("Do you want to run again yes or no")
    if yesOrNo=='no':
        isRunAgain = False
print('goodbye :)')