import pyperclip

t = []


def excelCol(n):
    result = ""
    while True:
        if n > 26:
            n, r = divmod(n - 1, 26)
            result = chr(r + ord('A')) + result
        else:
            return chr(n + ord('A') - 1) + result


flag = False
for i in range(0, 10000):
    if excelCol(i) == 'EJ'.upper() or flag:
        flag = True
        t.append(f"=SUM('Phase 4.1'!{excelCol(i)}2)")
    if excelCol(i) == 'EW'.upper():
        break
print(t[0], t[-1])
pyperclip.copy('\n'.join(t))