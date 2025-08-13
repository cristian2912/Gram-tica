import re

def check_grammar(grammar_id, input_string):
    patterns = {
        'G1': r'^(0|1)((0|1)*\1)?$',  # Palíndromos binarios (ej: 010, 11011)
        'G2': r'^a*b+$',              # a^n b^{n+1} (ej: ab, aabbb)
        'G3': r'^abb$',               # Solo "abb"
        'G4': r'^(ab|abb)$',          # "ab" o "abb"
        'G5': r'^a(ab)*b$'            # a(ab)^n b (ej: ab, aababb)
    }
    
    if grammar_id not in patterns:
        return False
    
    return bool(re.fullmatch(patterns[grammar_id], input_string))

if __name__ == "__main__":
    grammar_id = "G1"  # Fijamos la gramática para este caso
    file_path = "g1.txt"  # Archivo a leer
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Quitar comentarios y espacios
            line = line.split("#")[0].strip()
            if not line:
                continue
            result = "acepta" if check_grammar(grammar_id, line) else "NO acepta"
            print(f"{line} -> {result}")
