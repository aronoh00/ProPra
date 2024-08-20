import subprocess

#A3
args = ['ps', 'aux']
stdout = subprocess.PIPE
shell = False

proc = subprocess.Popen(args, stdout=stdout, shell=shell)
try:
    outs, errs = proc.communicate(timeout=15)
except subprocess.TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()

#A4
c = 0
for i in outs.split(b"\n"):
    decode = i.decode("utf-8")
    if decode.endswith(" -bash"):
        c += 1
    print(decode)

#A5
print(f"Zeilen mit Endung ' -bash': {c}")
