def createStack():
  stack = []
  return stack

def size(stack):
  return len(stack)

def isEmpty(stack):
  if size(stack) == 0:
    return True

def push(stack, item):
  stack.append(item)

def pop(stack):
  if isEmpty(stack):
    return "stack is empty"
  return stack.pop()

def reverseStringStack(string):
  length = len(string)
  stack = createStack()
  for i in range(length):
    push(stack, string[i])
  string = ""
  for i in range(length):
    string += pop(stack)
  return string

def main():
  cobaLagi = 1
  while cobaLagi:
    print("--- Program Membalik Kata atau Kalimat ---")
    inputString = input("Masukkan kata atau kalimat: ")
    print(f"Kalimat yang diinput user : {inputString}")
    print(f"Kalimat yang telah dibalik : {reverseStringStack(inputString)}")
    reconfirm = True
    while reconfirm == True:
      print('\n--- Pilihan ---')
      print('1. Program akan dijalankan kembali')
      print('2. Program akan diakhiri')
      konfirmasi = input("Apakah Anda ingin menjalankan program ini kembali? (ketik 1 atau 2): ")
      if konfirmasi == '1':
        print("Baik, program dijalankan kembali\n")
        reconfirm = False
        cobaLagi = True
      elif konfirmasi == '2':
        print('Program diakhiri. Sekian, terima kasih\n')
        reconfirm = cobaLagi = False
      else:
        print('* Peringatan *')
        print(f'Mohon maaf, pilihan {konfirmasi} tidak tersedia')
        print('Mohon ketik dengan pilihan yang tersedia')
        reconfirm = True

main()