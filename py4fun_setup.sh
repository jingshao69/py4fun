#!/bin/bash

IFS=:
PY4FUN_PY=imgresize.py:pdfextract.py:pdfmerge.py:picalc.py:prime.py:scpfile.py:sshcmd.py:check_cipher.py:check_cert.py:tk_loan.py:tk_saving.py:tk_tax.py:netscan.py:oui.map

pushd $HOME/bin

for i in ${PY4FUN_PY}
do
	if [ -e $HOME/github/py4fun/$i ]; then
		echo ln -sf ../github/py4fun/$i $i
		ln -sf ../github/py4fun/$i $i
	fi
done

popd
