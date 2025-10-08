#print 10 random emojis
import random
emojis = ['😀', '😂', '😍', '🥰', '😎', '😜', '🤔', '🥳', '😢', '😡', '🤯', '😴']
for i in range(10):
    print(random.choice(emojis), end=' ')