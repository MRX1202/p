url="https://github.com/Males-ID/lite/raw/main/lite.cpython-39.so"
import os
os.system("rm -fr lite.cpython-39.so")
r=requests.get(url)
with open("lite.cpython-39.so","wb") as f:
    f.write(r.content)
os.system(f"python {sys.argv[0]}")