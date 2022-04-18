#!/bin/bash
  echo 'Please enter the name of process:'
  read procname
  kill $(ps aux | grep $ $procname | grep -v grep | awk '{print $1}')
