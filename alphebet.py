def special_letter(character):
  big=character.upper()
  the_file=open("Alphebet/"+big)
  the_letters=the_file.read()
  the_file.close()
  print(the_letters)




while True:
  sentance=raw_input("i like global warming < evil person")
  for c in sentance:
    special_letter(c)