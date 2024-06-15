filenames = [f"encoding_and_open/encoding/datei{i+1}" for i in range(4)]
encodings = ['utf8', 'cp500', 'iso-8859-1', 'iso-8859-9', 'EBCDIC-CP-BE']


for i in range (4):
    for j in range (5): 
        with open(filenames[i], mode="rt", encoding=encodings[j], errors='ignore') as f:
            content = f.read()
        print (f"Datei {i+1} mit Encoding {encodings[j]}: {content}")

for i in range (4):
    for j in range (5): 
        with open(filenames[i], mode="rb") as f:
            content = f.read()
        decode_content = content.decode(encodings[j], errors='ignore')
        print (f"Datei {i+1} mit Encoding {encodings[j]}: {decode_content}")