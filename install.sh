#Skrypt instalujacy pypass w systemie
SCRIPTDIR=`pwd`
cd /usr/bin
sudo ln -s $SCRIPTDIR/pypass.py pypass 
sudo ln -s $SCRIPTDIR/hasla.sh hasla
sudo ln -s $SCRIPTDIR/hasla-edit.sh hasla-edit 
sudo ln -s $SCRIPTDIR/hasla-add.sh hasla-add
