# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
combined_names = combined_names.lower()

true = 0
love = 0

for letter in combined_names:
  if letter in 'true':
    true += 1
  elif letter in 'love':
    love += 1

score = int(str(true) + str(love))

if score < 20 or score > 90:
  print(f'"Your score is {score}, you go together like coke and mentos."')
elif score >= 40 and score <= 50:
  print(f'Your score is {score}, you are alright together.')
else: print(f'Your score is {score}')
