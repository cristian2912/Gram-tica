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
    grammar_id = input("Ingrese el ID de la gramática (G1-G5): ").strip()
    input_string = input("Ingrese la cadena a evaluar: ").strip()
    print("acepta" if check_grammar(grammar_id, input_string) else "NO acepta")