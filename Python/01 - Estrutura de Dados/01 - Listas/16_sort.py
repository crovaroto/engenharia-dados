linguagens = ["delphi", "java", "js", "cSharp", "python"]
linguagens.sort()
print(linguagens)

linguagens = ["delphi", "java", "js", "cSharp", "python"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["delphi", "java", "js", "cSharp", "python"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["delphi", "java", "js", "cSharp", "python"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)