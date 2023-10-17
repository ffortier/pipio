from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker, ParserRuleContext  # type:ignore
from antlr_grammars_v4.glsl import GLSLLexer, GLSLParser, GLSLParserListener
from pathlib import Path


class PrintListener(GLSLParserListener):
    def enterDeclaration(self, ctx: GLSLParser.DeclarationContext):
        print("declaration")
        print(ctx.PRECISION)


class Interpreter:
    def __init__(self, source_file: str | Path) -> None:
        with open(source_file) as f:
            source = f.read()

        lexer = GLSLLexer(InputStream(source))
        tokens = CommonTokenStream(lexer)
        parser = GLSLParser(tokens)
        printer = PrintListener()
        walker = ParseTreeWalker()
        walker.walk(printer, parser.translation_unit())
