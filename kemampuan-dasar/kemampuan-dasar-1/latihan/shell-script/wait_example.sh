#!/bin/bash
echo "Wait command" &
process id=$!
wait $process_id
echo "Exited with status $?"
