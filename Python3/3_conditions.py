text = "example testing text"
word = "testing"

### simple conditions

if True != False: print("Yes")

if text == word:
    print('if text is equal word')
else:
    print('else show this')

if text != word:
    print('if text is different word')
elif not text == word:
    print('else if is text not equal word')
else:
    print('else show this')


# check if contain word in text

# text = example testing text
# word =        -^^^^^^^
if word in text:
    print('word contain in testing')

### less/greater than

if 3 > 2:
    print('greater than')
elif 1 < 2:
    print('less than')

if 1 < 2 < 3:
    # Equivalent
    if 1 < 2 and 2 < 3:
        print('less than')

    if 3 > 2 & 2 > 1:
        print('greater than')

### ternary

#  if 3 > 2:
#      print(3)
#  else:
#      print(1)

# Equivalent
print(3 if 3 > 2 else 1)
