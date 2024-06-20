vocab = []
definition = []
menu = 0

# functions
def print_out_cards(): # prints out the list vertically starting with 1
  for i in range(len(vocab)):
    i += 1
    print(str(i) + ". " + vocab[i - 1] + "\n" + "Definition: " + definition[i - 1])


def swap_cards(card1_position, card2_position):
  card1_position -= 1
  card2_position -= 1
  temp_vocab = vocab[card1_position]
  vocab[card1_position] = vocab[card2_position]
  vocab[card2_position] = temp_vocab

  temp_def = definition[card1_position]
  definition[card1_position] = definition[card2_position]
  definition[card2_position] = temp_def


def study_cards(study_vocab_or_def):
  score = 0
  if study_vocab_or_def == 1:
    for i in range(len(vocab)):
      print(vocab[i])
      answer = input("Definition: ")
      if answer.lower() == definition[i]:
        score += 1
        print("Correct!")
        print()
      else:
        print("Wrong! The correct answer is", definition[i])
        print()
        
  elif study_vocab_or_def == 2:
    for i in range(len(vocab)):
      print(definition[i])
      answer = input("Vocabulary: ")
      if answer.lower() == vocab[i]:
        score += 1
        print("Correct!")
        print()
      else:
        print("Wrong! The correct answer is", vocab[i])
        print()

  print("You got " + str(score) + "/" + str(len(vocab)) + " correct!")
      
    
# MAIN PROGRAM
print("Welcome to PyFlashcard!")

while menu != 4:
  print()
  menu = int(input("Options:\n[1] Add card\n[2] Remove card\n[3] Swap cards\n[4] Study flashcards\nWhat would you like to do? "))
  print()

  # add card
  if menu == 1:
    add_word = 0
    print("Enter 'q*' to stop adding word.")
    
    while add_word != "q*":
      add_word = input("Vocabulary: ")
      if add_word == "q*":
        break
      else:
        vocab.append(add_word.lower())
        add_meaning = input("Definition: ")
        definition.append(add_meaning.lower())
      print()

  # remove card
  elif menu == 2:
    if len(vocab) == 0:
      print("There is no card to remove!")
    else:
      print_out_cards()
      print()
      remove_card = int(input("Which card would you like to remove? (Enter the number) "))
      vocab.pop(remove_card - 1)
      definition.pop(remove_card - 1)
      print("Your cards:")
      print_out_cards()

  # swap cards
  elif menu == 3:
    print_out_cards()
    card1 = int(input("Enter the position of the card you want to swap: "))
    card2 = int(input("Enter the position you would like to the card to swap to: "))
    print()
    swap_cards(card1, card2)
    print_out_cards()

  # study
  elif menu == 4:
    study = True
    while study == True:
      vocab_or_def = int(input("Quiz on:\n[1] Vocabulary\n[2] Definition\n"))
      print()
      study_cards(vocab_or_def)
      print()
      study_again = input("Do you want to study again? (Yes/No) ")
      if study_again.lower() == "yes":
        study = True
      elif study_again.lower() == "no":
        study = False