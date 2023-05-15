#!/bin/bash

# Check if the script is being run with sudo
if [ "$UID" -ne 0 ]
	then
		echo "Please run this script with sudo"
		exit 1
fi

# Check if a URL has been provided as an argument
if [ -z "$1" ]
	then
		echo "Please provide the URL of the chromedriver zip file"
		exit 1
fi

# Download the chromedriver zip file
wget "$1"

# Unzip the chromedriver file
unzip chromedriver_linux64.zip

# Move the chromedriver file to the /usr/bin directory
mv chromedriver /usr/bin/chromedriver

# Set ownership to root and group to root
chown root:root /usr/bin/chromedriver

# Add execute permissions to the chromedriver file
chmod +x /usr/bin/chromedriver

# Clean up
rm chromedriver_linux64.zip LICENSE.chromedriver
echo "Chromedriver downloaded and installed"
