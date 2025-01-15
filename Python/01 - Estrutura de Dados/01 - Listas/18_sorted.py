linguagens = ["delphi", "java", "js", "cSharp", "python"]

print(sorted(linguagens, key=lambda x: len(x)))

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
