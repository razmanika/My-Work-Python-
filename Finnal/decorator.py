def main(func):
  def wrapper(*args):
    print(f'Arguments for args: {args}')
    func(*args)
  return wrapper

@main
def dec(arg1, arg2):
  integer_list = []
  str_list_arg1= []
  str_list_arg2= []
  # checking id arguments are integers
  try:
    arg1= int(arg1)
  except:
    print('first argument is not integer please wait ...')
  else:
    integer_list.append(arg1)
  try:
    arg2= int(arg2)
  except:
    print('the second argument is not integer please wait ...')
  else:
    integer_list.append(arg2)
  # if arguments are not integer,than we split them
  try:
    arg1.split()
    arg2.split()
  except:
    pass
  # checking in splited argument(s) if there are integers inside
  try:
    for letter in arg1:
      try:
        letter=int(letter)
      except:
        str_list_arg1.append(letter)
      else:
        integer_list.append(letter)
  except:
    pass
  try:
    for letter1 in arg2:
      try:
        letter1=int(letter1)
      except:
        str_list_arg2.append(letter1)
      else:
        integer_list.append(letter1)
  except:
    pass
  # list to str
  str_list_to_str_arg1= ''.join(str_list_arg1)
  str_list_to_str_arg2= ''.join(str_list_arg2)
  if str_list_to_str_arg1 == '' and str_list_to_str_arg2 == '':
    print(f'integer arguments: {integer_list}\nstr arguments: None')
  else:
    print(f'integer arguments: {integer_list}\nstr arguments: {str_list_to_str_arg1} {str_list_to_str_arg2}')


dec(7,'po90')
