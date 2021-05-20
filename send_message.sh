#!/bin/bash

TOKEN="1898906802:AAHkASvca63CCKlmKIC-xe2rJKOgzGTqAIU"
ID="1158986483"
MENSAJE="Esto es un Mensaje de Prueba"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"