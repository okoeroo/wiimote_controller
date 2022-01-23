# wiimote_controller

Install build essentials:
```
sudo apt install autoconf
sudo apt install automake
sudo apt install build-essential
sudo apt install flex
sudo apt install bison
```

# Install bluetooth library and dev sources:
```sudo apt install libbluetooth-dev libbluetooth3-dev```

Clone this repo:
```git clone https://github.com/azzra/python3-wiimote.git```

or the backup:
https://github.com/okoeroo/python3-wiimote


Install the cwiid Python library
```sudo pip3 install cwiid```


Goto python3-wiimote directory:
```
aclocal
autoconf
./configure
make
sudo make install
```


Then you can go back to this library.
