#!/bin/bash

IFS=:
PY4FUN_PY=imgresize.py:pdfextract.py:pdfmerge.py:picalc.py:prime.py:scpfile.py:sshcmd.py:tk_loan.py:tk_saving.py:tk_tax.py:tk_hash.py:check_cert.py:check_cipher.py:netscan.py:oui.map

CWD=$(pwd)
pushd $HOME/bin

for i in ${PY4FUN_PY}
do
	if [ -e $CWD/$i ]; then
		echo ln -sf $CWD/$i $i
		ln -sf $CWD/$i $i
	fi
done

popd
