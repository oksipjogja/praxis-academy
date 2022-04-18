#!/bin/bash
Recipient="admin@example.com"
Subjects="Greeting"
Message="Welcome to our site"
`mail -s $Subject $Recipient <<< $Message`
