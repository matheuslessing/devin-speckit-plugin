import os
import sys

def main():
    print("[HOOK] Validando integridade do Spec-Driven Development (SDD)...")
    
    if not os.path.exists("specs"):
        print("[WARNING] ATENÇÃO: A pasta 'specs/' nao existe!")
        print("          Voce esta tentando programar sem especificacao previa.")
        print("          Recomenda-se invocar o comando /speckit-specify imediatamente.")
        sys.exit(0) # Saída sem erro duro para não quebrar a UI, mas loga o warning.
        
    md_files = [f for f in os.listdir("specs") if f.endswith(".md")]
    if not md_files:
        print("[WARNING] A pasta 'specs/' esta vazia! Pare e faca o planejamento (Plan) primeiro.")
    else:
        print(f"[OK] {len(md_files)} documentos de especificacao/arquitetura encontrados. O caminho esta livre para codar.")

if __name__ == "__main__":
    main()
