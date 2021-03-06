TEXTTOADD=$@
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
echo $TEXTTOADD >> $TMPFILE
pypass -i $TMPFILE -k $KEY -c  > $HASLA
rm $TMPFILE
