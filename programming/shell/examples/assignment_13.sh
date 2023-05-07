# !/bin/bash
# Jaroslav Langer
# 22/05/2019

jfind () {
        out=$(egrep -n "$word" $filename | cut -f1 -d:)
        if [[ $out != '' ]]; then
                echo "Slovo se nachází na řádku/cích:"
                return 0
        else
                out=$(echo "Slovo se v souboru nenachází.")
                return 1
        fi
}

jmerge () {
        if [[ -f $file1 && -f $file2 && -r $file1 && -r $file2 ]]; then
                sed -n 'w soubor' $file1 $file2
                echo "Výsledný soubor má název:"
                out=$(echo "soubor")
                return 0
        else
                out=$(echo "Soubory nebylo možné spojit")
                return 1
        fi
}

echo "Pro nalezení slova v souboru stiskněte jedničku..."

select opt in NajdiSlovo SpojSoubory Konec; do
        case $opt in
                NajdiSlovo)
                        read -p "Zadej požadavek ve formátu \"JménoSouboru HledanéSlovo\": " filename word
                        jfind
                        echo $out
                ;;
                SpojSoubory)
                        read -p "Zadej požadavek ve formátu \"JménoSouboru1 JménoSouboru2\": " file1 file2
                        jmerge;
                        echo $out
                ;;
                Konec) echo "Na shledanou.";
                break;
                ;;
                *) echo "Nesprávný vstup.";
                break;
                ;;
        esac
        echo "
Vyberte další operaci.
Pro odchod zmáčkněte trojku.
"
done
