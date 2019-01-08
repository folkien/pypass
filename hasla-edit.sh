
# Check kwrite existence
kwrite --version
if [ $? -eq 0 ]; then
    EDITOR=kwrite
else
    # Check kate existence
    kate --version
    if [ $? -eq 0 ]; then
        EDITOR=kate
    else
        # Check gedit existence
        gedit --version
        if [ $? -eq 0 ]; then
            EDITOR=gedit
        else
            echo "No editor exists!"
            return -1
        fi
    fi
fi


# Uzyskujemy katalog skryptu
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

#wczytujemy pozycje hasel i kluczy
source $SCRIPTDIR/settings.sh


#tworzymy plik tymczasowy
TMPFILE=`mktemp`

#odszyfrowujemy plik z haslami
pypass -i $HASLA -k $KEY -c  > $TMPFILE
$EDITOR $TMPFILE &
wait
# Zabezpieczenie przed nadpisanie pliku pustymi zmiennymi
if [ -f $TMPFILE ] ; then
    filesize=$(stat --printf="%s"  $TMPFILE)
    if [ $filesize -ne 0 ] ; then
        if [ -w $HASLA ] ; then
            pypass -i $TMPFILE -k $KEY -c -o $HASLA
            echo "Plik poprawnie zapisano."
        else
            echo "Plik nie ma uprawnien do zapisu. Probuje to zmienic."
            chmod u+w $HASLA
            if [ -w $HASLA ] ; then
                pypass -i $TMPFILE -k $KEY -c -o $HASLA
                echo "Plik poprawnie zapisano."
            else
                echo "Nie potrafię zmienić uprawnień pliku."
            fi
        fi
        #poprawiamy uprawnienia do pliku hasel
    else
        echo "Rozmiar pliku to zero."
    fi
else
    echo "Plik nie istnieje."
fi
rm $TMPFILE
