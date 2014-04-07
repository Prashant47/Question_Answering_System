#!/bin/bash

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' wordnet|grep "install ok installed")
echo Checking for package: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No wordnet. Setting up wordnet."
  sudo apt-get --force-yes --yes install wordnet
fi

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python|grep "install ok installed")
echo Checking for package: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No python. Setting up python."
  sudo apt-get --force-yes --yes install python
fi

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python-nltk|grep "install ok installed")
echo Checking for package: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No python-nltk. Setting up python-nltk."
  sudo apt-get --force-yes --yes install python-nltk
fi

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' python-gtk2|grep "install ok installed")
echo Checking for package: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No python-gtk2. Setting up python-gtk2."
  sudo apt-get --force-yes --yes install python-gtk2
fi



python -m nltk.downloader all
