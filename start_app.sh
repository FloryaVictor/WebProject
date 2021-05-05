source ./conf.sh
cd db || exit
./init_db.sh
./start_db.sh
cd ..
