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
# Checks
if [ ! -e $HASLA ]; then
    echo "Passwords file not exists!"
    exit -1
fi
if [ ! -e $KEY ]; then
    echo "Key file not exists!"
    exit -1
fi
#odszyfrowujemy plik z haslami
echo "Used $(basename $KEY) key with file $(basename $HASLA)."
pypass -i $HASLA -k $KEY -c
