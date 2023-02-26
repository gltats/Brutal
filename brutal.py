import zipfile

def extract_zip(zip_file, password):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode())
        print(f"[+] Password found: {password}")
    except:
        pass

def main():
    zip_file = 'x/x.zip'
    with open('x/x.txt') as f:
        for line in f:
            password = line.strip()
            extract_zip(zip_file, password)

if __name__ == '__main__':
    main()