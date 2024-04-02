from collections import defaultdict

# İşlem tablosu
opcode_table = {
    "ADD": "18", "ADDF": "58", "ADDR": "90", "AND": "40", "CLEAR": "B4",
    "COMP": "28", "COMPF": "88", "COMPR": "A0", "DIV": "24", "DIVF": "64",
    "DIVR": "9C", "FIX": "C4", "FLOAT": "C0", "HIO": "F4", "J": "3C", "JEQ": "30",
    "JGT": "34", "JLT": "38", "JSUB": "48", "LDA": "00", "LDB": "68", "LDCH": "50", "LDF": "70",
    "LDL": "08", "LDS": "6C", "LDT": "74", "LDX": "04", "LPS": "D0", "MUL": "20", "MULF": "60", "MULR": "98",
    "STL": "14", "STS": "7C", "STSW": "E8", "STT": "84", "STX": "10", "SUB": "1C", "SUBF": "5C",
    "SUBR": "94", "SVC": "B0", "TD": "E0", "TIO": "F8", "TIX": "2C", "TIXR": "B8", "WD": "DC",
    "NORM": "C8", "OR": "44", "RD": "D8", "RMO": "AC", "RSUB": "4C", "SHIFTL": "A4", "SHIFTR": "A8",
    "SIO": "F0", "SSK": "EC", "STA": "0C", "STB": "78", "STCH": "54", "STF": "80", "STI": "D4"
}

# Direktifler listesi
DIRECTIVES = ['START', 'END', 'BYTE', 'WORD', 'RESB', 'RESW', 'BASE']

# Hata mesajlarını listesi
errors = []

# Sembol tablosu ve adres tablosu
SYMTAB = defaultdict(int)
ADDRESS_TABLE = defaultdict(str)

# Giriş ve ara dosya 
input_file = "input.txt"
intermediate_file = "intermediate.txt"

# Pass 1 işlemi
def pass_1(input_file, intermediate_file):
    # Başlangıç adres sayacı
    LOCCTR = 0
    # Başlangıç adresini varsayılan olarak None al
    start_address = None

    # Dosyaları açıyoruz. source: kaynak kod dosyası, intermediate: ara dosya.
    with open(input_file, 'r') as source, open(intermediate_file, 'w') as intermediate:
        for line in source:
            # Satırları temizliyoruz ve boş ve yorum satırlarını atlıyoruz.
            line = line.strip()
            if not line or line.startswith('.'):
                continue

            # Satırı analiz edip etiket, opcode ve operand'ı alıyoruz.
            parts = line.split()
            label = parts[0] if parts and parts[0] not in opcode_table else ''
            opcode = parts[1] if len(parts) > 1 else parts[0] if parts else ''
            operand = parts[2] if len(parts) > 2 else ''

            # 'START' direktifiyle işleme başlıyoruz.
            if opcode == 'START':
                # Başlangıç adresini ayarlıyoruz.
                start_address = int(operand, 16)
                LOCCTR = start_address
                # Ara dosyaya yazıyoruz.
                intermediate.write(f"{LOCCTR:04X}\t{line}\n")
            else:
                # Diğer tüm işlemler burada gerçekleşecek.
                # Eğer program 'START' direktifiyle başlamamışsa varsayılan bir adresle başlayacak.
                if start_address is None:
                    start_address = 0x1000  # Varsayılan başlangıç adresi
                    LOCCTR = start_address

                if label:
                    # Etiket kontrolü yapıyoruz.
                    if label in SYMTAB:
                        errors.append(f"Hata: {label} etiketi zaten mevcut.")
                    else:
                        SYMTAB[label] = LOCCTR

                # Opcode'a göre talimat uzunluğunu hesaplıyoruz.
                LOCCTR += calculate_byte_size(opcode, operand)

                # İşlenmiş satırı ara dosyaya yazıyoruz.
                intermediate.write(f"{LOCCTR:04X}\t{line}\n")

        # Eğer 'START' direktifi yoksa hata veriyoruz.
        if start_address is None:
            raise ValueError("Hata: Başlangıç direktifi (START) bulunamadı.")

        # Program uzunluğunu hesaplayıp ara dosyaya yazıyoruz.
        program_length = LOCCTR - start_address
        intermediate.write(f"Program Uzunluğu: {program_length}\n")

# Byte büyüklüğünü hesaplama fonksiyonu.
def calculate_byte_size(opcode, operand):
    if opcode == 'WORD':
        return 3
    elif opcode == 'RESW':
        return 3 * int(operand)
    elif opcode == 'RESB':
        return int(operand)
    elif opcode == 'BYTE':
        # 'BYTE' için uzunluk hesabı yapıyoruz.
        if operand.startswith('C') or operand.startswith('X'):
            return len(operand) - 3
        else:
            errors.append("Hata: BYTE için bilinmeyen format.")
            return 0
    else:
        # Opcode tablosunda yoksa varsayılan uzunluk olarak 3 dönüyoruz.
        return 3

# Ana program. Gerekli fonksiyonları çağırarak işlemi başlatıyoruz.
pass_1(input_file, intermediate_file)

# Sembol tablosunu ve varsa hataları yazdırıyoruz.
print("Sembol Tablosu:")
for label, address in SYMTAB.items():
    print(f"{label} - {address:04X}")

if errors:
    print("\nHatalar:")
    for error in errors:
        print(error)
