#Skrypt instalujacy pypass w systemie
SCRIPTDIR=`pwd`
#Zmiana dowiazania do /bin/dash
cd /bin
sudo rm sh
sudo ln -s bash sh
#Instalacja
cd /usr/bin
sudo ln -s $SCRIPTDIR/pypass.py pypass 
sudo ln -s $SCRIPTDIR/hasla.sh hasla
sudo ln -s $SCRIPTDIR/hasla-edit.sh hasla-edit 
sudo ln -s $SCRIPTDIR/hasla-add.sh hasla-add
sudo ln -s $SCRIPTDIR/get-haslo.sh get-haslo
