s = input()

# "   Alexandr    Sergeevich   Pushkin   "
#          => "Alexandr Sergeevich Pushkin"

words = s.split()
new_s = ' '.join(words)

print(new_s)