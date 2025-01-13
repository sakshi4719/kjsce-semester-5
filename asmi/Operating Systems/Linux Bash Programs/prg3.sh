#!/bin/bash

read -p "Enter username: " username
read -p "Enter password: " password
useradd -m -p "$password" "$username"
[ $? -eq 0 ] && echo "User added!" || echo "Failed to add user!"

