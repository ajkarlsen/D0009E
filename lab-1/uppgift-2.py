def recept(antal):
    ingredienser = [f"{round(3/4*antal)} ägg",
                    f"{3/4*antal} dl strösocker",
                    f"{3/4*antal} dl vetemjöl",
                    f"{2/4*antal} tsk vaniljsocker",
                    f"{2/4*antal} tsk bakpulver",
                    f"{75/4*antal} g smör",
                    f"{1/4*antal} dl vatten"]
    
    print(f"Ingredienser som behövs för en sockerkaka för {antal} personer:")
    for ingrediens in ingredienser:
        print(f"{ingrediens},")
    
def tid_blanda(antal):
    return 10+antal

def tid_grädda(antal):
    return 30+(antal*3)

def sockerkaka(antal):
    recept(antal)
    print(f"\nDet tar totalt {tid_blanda(antal) + tid_grädda(antal)} minuter att göra kakan\n")

sockerkaka(4)
print()
sockerkaka(7)
