phone=input('>')
dictionary={
    '1' : 'One',
    '2' :'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '10': 'Ten'
}
output=""
for ch in phone:
    output+=dictionary.get(ch)
    print(output)
