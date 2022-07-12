#!/bin/bash

BASE=`gp url 7474`
echo "Hello DevSpaces+Neo4j Users"
echo ""
echo "For Neo4j console, go to:"
echo "$BASE/browser"
echo ""
echo "For connect url:"
B2=`gp url 7687`
echo "$B2:443"