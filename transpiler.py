from __future__ import annotations

import io
import sys
import tokenize
from typing import Dict

HOLY: Dict[str, str] = {

	"proclaim": "def",
	"say": "print",
	"if_thou": "if",
	"else_if_thou": "elif",
	"otherwise": "else",
	"let_be": "pass",
	"whilst": "while",
	"carry_on": "continue",
	"amen": "True",
	"heresy": "False",
	"void": "None",
	"deny": "not"
}

def transpile(source):
	out_tokens = []

	reader = io.BytesIO(source.encode("utf-8")).readline
	for token in tokenize.tokenize(reader):
		if token.type == tokenize.NAME and token.string in HOLY:
			token = token._replace(string=HOLY[token.string])
		out_tokens.append(token)
	return tokenize.untokenize(out_tokens).decode("utf-8")

def main():
	if len(sys.argv) != 3:
		print("Usage: transpile.py input.hpy output.py")
		return 2

	inpath, outpath = sys.argv[1], sys.argv[2]
	src = open(inpath, 'r', encoding="utf-8").read()
	py = transpile(src)
	open(outpath, 'w', encoding="utf-8").write(py)
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
