def dec(plain):
    output = ""
    originString = plain
    strTarget = len(originString) % 3;
    for i in range(0, len(originString)):
        output += chr(ord(originString[i]) - 0x3 - strTarget);
    return output

def enc(password):
    output = ""
    encryptedString = password
    strTarget = len(encryptedString) % 3
    for i in range(0, len(encryptedString)):
        output += chr(ord(encryptedString[i]) + 0x3 + strTarget);
    return output

data = "USER:10303118ABYPASS_1000Limits:0TryToFixMemoryList:0TryToFixCRC32_ToBYPASS:0AbleToInput1000_OnTextBox:0"
