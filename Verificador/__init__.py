# ******************************************************************************
# __init__.py e .cs50.yaml
#
# Por: Abrantes Araújo Silva Filho
#      abrantesasf@computacaoraiz.com.br | abrantesasf@pm.me
#
# EXERCÍCIO: "contar_palavras"
# LINGUAGEM: C


import check50
import check50.c
import subprocess as sp


@check50.check()
def existe():
    """O arquivo contar_palavras.c existe?"""
    check50.exists("contar_palavras.c")
    check50.include("1palavra.txt", "10palavras.txt", "1091palavras.txt",
                    "simbolos.txt", "vazio.txt")


#@check50.check(existe)
def estilo():
    """Verifica se o estilo de escrita do código está ok:"""
    s = sp.run("style50 contar_palavras.c -o score", shell=True,
               capture_output=True, text=True).stdout
    s = ''.join(i for i in s if i.isdigit() or i in '-.')
    s = str(round(float(s), 1))
    check50.run("echo -n " + s).stdout("1.0")


@check50.check(existe)
def compila():
    """Verifica se o arquivo contar_palavras.c compila:"""
    check50.c.CFLAGS = {'ggdb': True, 'lm': True, 'std': 'c17', 'Wall': True, 'Wpedantic': True}
    check50.c.compile("contar_palavras.c", exe_name="contar_palavras",
                      cc="gcc", max_log_lines=50, lcs50=True)


@check50.check(compila)
def arquivo1():
    """Testa arquivo com 1 palavra"""
    check50.run("./contar_palavras").stdin("1palavra.txt", prompt=True).stdout("1").exit(0)

@check50.check(compila)
def arquivo10():
    """Testa arquivo com 10 palavras"""
    check50.run("./contar_palavras").stdin("10palavras.txt", prompt=True).stdout("10").exit(0)

@check50.check(compila)
def arquivo1091():
    """Testa arquivo com 1091 palavras"""
    check50.run("./contar_palavras").stdin("1091palavras.txt", prompt=True).stdout("1091").exit(0)

@check50.check(compila)
def arquivo0():
    """Testa arquivo vazio"""
    check50.run("./contar_palavras").stdin("vazio.txt", prompt=True).stdout("0").exit(0)

@check50.check(compila)
def arquivoS():
    """Testa arquivo com símbolos"""
    check50.run("./contar_palavras").stdin("simbolos.txt", prompt=True).stdout("0").exit(0)

