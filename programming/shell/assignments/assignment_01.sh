# Vyberte si libovolný příkaz shellu (1 bod). Pomocí informací z nápovědy k příkazu zjistěte a napište (česky), k čemu příkaz slouží (1 bod). Využijte voleb (tzv. options) vybraného příkazu a uveďte tři různé příklady jeho použití, a popište, co zvolená volba konkrétně provádí (3 body).
# 
#                 Příkaz	'declare'
# 
#     Příkazem můžeme deklarovat proměnné a funkce, nastavovat jejich atributy, případně ukazovat jejich hodnoty.
# Příklady použití a přepínačů:
#     -p  - ukáže všechny atributy a hodnoty daného jména.    
#             př.$ declare -p
#     -r  - nastaví proměnnou jako read-only                   
#             př.$ declare -r mojePromenna='Moje promenna je super nepromenna'
#     -i  - nastaví aby proměnná měla atribut typu integer
#             př.$ declare -i mojePromenna=666
# 