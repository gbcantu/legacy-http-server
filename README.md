# Legacy HTTP Server

Servidor HTTP local simples para abrir arquivos antigos no navegador.

Este projeto nasceu como uma solucao crua para casos em que uma pagina, manual ou pacote HTML antigo nao funciona bem quando aberto diretamente pelo sistema de arquivos, usando `file://`.

Algumas arquiteturas antigas dependem de caminhos relativos, arquivos `.htm`, codificacao `windows-1252`, SVG/SVGZ ou comportamentos que navegadores modernos tratam melhor quando o conteudo e servido via HTTP local.

## Para que serve

- Servir uma pasta local em `http://127.0.0.1:8000`.
- Abrir automaticamente uma pagina inicial, por padrao `index.htm`.
- Facilitar o acesso a conteudo legado sem precisar configurar Apache, Nginx ou outro servidor completo.
- Preservar compatibilidade basica com `.htm`, `.html`, `.svg` e `.svgz`.

## O que este projeto nao e

- Nao e um servidor para producao.
- Nao e uma solucao de seguranca.
- Nao substitui uma migracao real de sistemas antigos.
- Nao deve ser exposto na internet.

A ideia e ser uma ferramenta pequena e direta para uso local.

## Arquivos

```text
main.py    Servidor HTTP local
README.md             Documentacao do projeto
```

As versoes empacotadas, como `.exe` para Windows e `.sh` para Linux, foram removidas para manter o repositorio simples e focado no codigo-fonte.

## Requisitos

- Python 3
- Um navegador
- Uma pasta contendo o arquivo que voce quer abrir, por exemplo `index.htm`

## Como usar

Coloque o arquivo `main.py` na pasta do conteudo antigo ou execute apontando para essa pasta.

Para servir a pasta atual:

```bash
python main.py
```

Depois disso, o navegador deve abrir:

```text
http://127.0.0.1:8000/index.htm
```

## Opcoes

Alterar a porta:

```bash
python main.py --port 8080
```

Servir outra pasta:

```bash
python main.py --directory caminho/da/pasta
```

Abrir outra pagina inicial:

```bash
python main.py --page manual.htm
```

Iniciar sem abrir o navegador automaticamente:

```bash
python main.py --no-browser
```

Combinar opcoes:

```bash
python main.py --directory caminho/da/pasta --port 8080 --page manual.htm
```

## Como encerrar

No terminal onde o servidor estiver rodando, pressione:

```text
Ctrl+C
```

## Observacoes

- O servidor escuta apenas em `127.0.0.1` por padrao.
- A porta padrao e `8000`.
- Arquivos `.htm` e `.html` sao servidos com `charset=windows-1252`.
- Arquivos `.svgz` sao servidos com `Content-Encoding: gzip`.
- Se a porta ja estiver em uso, escolha outra com `--port`.

## Licenca

Uso livre permitido.

Voce pode usar, copiar, modificar e adaptar este projeto para fins pessoais, profissionais ou educacionais.

Se o projeto, uma versao modificada dele ou uma ideia diretamente derivada for redistribuida, publicada, divulgada ou usada como meio de propagacao, os creditos ao autor original devem ser mantidos.

Autor original: Gabriel.

Veja o arquivo `LICENSE` para os termos completos.
