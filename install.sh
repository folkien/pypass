#Skrypt instalujacy pypass w systemie
SCRIPTDIR=`pwd`
#Zmiana dowiazania do /bin/dash
cd /bin
sudo rm sh
sudo ln -s bash sh
#Instalacja
cd /usr/bin
sudo ln -sf $SCRIPTDIR/pypass.py pypass 
sudo ln -sf $SCRIPTDIR/hasla.sh hasla
sudo ln -sf $SCRIPTDIR/hasla-edit.sh hasla-edit 
sudo ln -sf $SCRIPTDIR/hasla-add.sh hasla-add
sudo ln -sf $SCRIPTDIR/get-haslo.sh get-haslo
